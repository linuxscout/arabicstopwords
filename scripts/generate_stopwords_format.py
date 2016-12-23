#!/usr/bin/python
# -*- coding=utf-8 -*-
##from analex import *

import sys
import re
import  getopt
import os
import string
from pyarabic.araby import *
import pyarabic.arabrepr 
arabicrepr = pyarabic.arabrepr.ArabicRepr()
from ar_stowords import *
scriptname = os.path.splitext(os.path.basename(sys.argv[0]))[0]
scriptversion = '0.1'
AuthorName="Taha Zerrouki"
def usage():
# "Display usage options"
    print "(C) CopyLeft 2007,  %s"%AuthorName
    print "Usage: %s -f filename [OPTIONS]" % scriptname
#"Display usage options"
    print "\t[-h | --help]\t\toutputs this usage message"
    print "\t[-V | --version]\tprogram version"
    print "\t[-f | --file= filename]\tinput file to %s"%scriptname
    print "\t[-o | --out= output format]\toutput format(csv, python, sql)"
    
    print "\r\nThis program is licensed under the GPL License\n"

def grabargs():
#  "Grab command-line arguments"
    fname = ''
    outputformat = 'csv'
    allforms = True

    if not sys.argv[1:]:
        usage()
        sys.exit(0)
    try:
        opts,  args = getopt.getopt(sys.argv[1:],  "AhV:f:o:", 
                               ["help",  "version", 'notall', 
                                 "file=",  "out="], )
    except getopt.GetoptError:
        usage()
        sys.exit(0)
    for o,  val in opts:
        if o in ("-h",  "--help"):
            usage()
            sys.exit(0)
        if o in ("-A",  "--notall"):
            allforms = False;
        if o in ("-V",  "--version"):
            print scriptversion
            sys.exit(0)
        if o in ("-f",  "--file"):
            fname = val
        if o in ("-o",  "--out"):
            outputformat = val;
        else:
            outputformat = 'csv';    
    return (fname, outputformat,  allforms)

def main():

    filename, outputformat,  allforms=grabargs()

    outputformat = string.lower(outputformat)
    if outputformat not in ('csv', 'python', 'sql'):
        outputformat='csv';
    print "--~# generated format", outputformat
    print "--~#file name ", filename
    print "--~#output format", outputformat
    #~sys.exit()
    if outputformat=='python':
        print "STOPWORDS={}";
    elif outputformat=='sql':
        if not allforms:
            print u'''create TABLE classedstopwords
                (
                ID INT UNIQUE NOT NULL, 
                WORD TEXT NOT NULL, 
                vocalized TEXT NOT NULL, 
                word_type TEXT NOT NULL,

                word_class TEXT NOT NULL,
                conjonction int(1) default 0, 
                definition int(1) default 0,  
                preposition int(1) default 0,

                pronoun int(1) default 0, 
                interrog int(1) default 0,
                conjugation int(1) default 0,                     
                qasam int(1) default 0,
                
                defined int(1) default 0,
                is_inflected  int(1) default 0,
                tanwin int(1) default 0,
                action varchar(10) default '', 

                object_type  varchar(10) default '',
                need  varchar(10) default ''                
                );
            ''';
        else:
            print u'''create TABLE STOPWORDS
                (
                ID INT UNIQUE NOT NULL,
                UNVOCALIZED TEXT NOT NULL,
                PROCLETIC TEXT,
                TAGS TEXT,
                VOCALIZED TEXT,
                STEM TEXT,
                TYPE TEXT,
                ORIGINAL TEXT,
                ENCLETIC TEXT
                );
            ''';            
            


#ToDo1 ref
    if (not filename):
        usage()
        sys.exit(0)
    option="";
    try:
        fl=open(filename);
    except :
        print " Error :No such file or directory: %s" % filename
        return None;
    line=fl.readline().decode("utf8");
    text=u""
    limit=1000;
    counter=0;
    counter_generated=1;

    while line and counter<limit:
##        text=" ".join([text, chomp(line)])
        line=fl.readline().decode("utf8");
        line=chomp(line);
        if not line.startswith("#"):
            listword=line.split(";");
            if len(listword)>=9:
                vocalized = listword[0].strip()
                word=strip_tashkeel(vocalized);
                type_word=listword[1];
                class_word=listword[2];
                
                has_conjuction = 0 if listword[3]  == "*" else  1 
                has_definition = 0 if listword[4]  == "*" else  1 
                has_preposition = 0 if listword[5]  == "*" else  1 
                has_pronoun = 0 if listword[6]  == "*" else  1 
                
                has_interrog = 0 if listword[7]  == "*" else  1 
                has_conjugation = 0 if listword[8]  == "*" else  1                 
                has_qasam = 0 if listword[9]  == "*" else  1 
                is_defined = 0 if listword[10]  == "*" else  1 
                
                is_inflected = 0 if listword[11] == "*" else 1
                tanwin = 0 if listword[12] == "*" else 1
                action = "" if listword[13] == "" else listword[13]                
                object_type = "" if listword[14] == "" else listword[14]                
                need = "" if listword[15] == "" else listword[15]                
                if allforms: 
                    list0=generate_allforms(word,type_word, class_word, has_pronoun, has_conjuction,has_preposition,has_definition,has_interrog,has_conjugation, has_qasam,is_defined);
                    for item in list0:
                        l=item['vocalized'];
                        counter_generated+=1;
                        stemmed=l;
                        item['vocalized']=standardize_form(item['vocalized']);
                        item['word']=standardize_form(item['word']);
                        standard=ar_strip_marks(item['word']);
                        
                        if outputformat=='sql':
                            line=u"insert into STOPWORDS values (%d,'%s', '%s', '%s', '%s','%s', '%s', '%s', '%s');"%(
                                counter_generated,
                                standard, 
                                item['procletic'],
                                item['tags'],
                                item['vocalized'],
                                item['stem'],
                                item['type'],
                                item['original'],
                                item['encletic'],													
                                );
                        elif outputformat=='python':
                            fields=u"";
                            for key in item.keys():
                                onefield=u"'%s':u'%s',"%(key,item[key]);
                                fields+=onefield;
                            line= u"STOPWORDS[u'"+standard+"']={"+fields+u"}";							
                        else:
                            line=u'\t'.join([standard, stemmed])
                        print line.encode('utf8');
                else:
                    result ={
                    'counter':counter,
                    'word': word,
                    'vocalized': vocalized, 
                    'word_type': type_word,
                    
                    'word_class': class_word,
                    'conj': has_conjuction, 
                    'defin': has_definition,  
                    'prep': has_preposition, 

                    'pron': has_pronoun, 
                    'interrog': has_interrog,
                    'conjug': has_conjugation,                     
                    'qasam': has_qasam,

                    'defined': is_defined,  
                    "is_inflected" : is_inflected,
                    "tanwin" : tanwin, 
                    "action" : action, 
                    
                    "object_type" : object_type,
                    "need" : need,                  
                    }
                    if outputformat=='sql':
                            line=u"insert into classedstopwords values (%d, '%s', '%s', '%s',  '%s', %d, %d, %d,    %d, %d, %d, %d,   %d,%d, %d, '%s',    '%s', '%s');"%(
                                result['counter'],
                                result['word'],
                                result['vocalized'],
                                result['word_type'],
                                
                                result['word_class'],
                                result['conj'],
                                result['defin'],
                                result['prep'],
                                
                                result['pron'],
                                result['interrog'],
                                result['conjug'],
                                result['qasam'],

                                result["defined"],
                                result["is_inflected"] ,
                                result["tanwin"], 
                                result["action"], 
                                
                                result["object_type"] ,
                                result["need"] ,                                                        
                                );
                    elif outputformat=='python':
                        line = arabicrepr.repr(result)
                    else:
                        line = u'\t'.join([result['word'],  result['vocalized']])
                    print line.encode('utf8');                    
        counter+=1
if __name__ == "__main__":
  main()








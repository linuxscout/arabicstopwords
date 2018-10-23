#!/usr/bin/python
# -*- coding=utf-8 -*-
##from analex import *

import sys
import re
import  getopt
import os
import string
#~ import pyarabic.araby as araby
from ar_stowords import *
scriptname = os.path.splitext(os.path.basename(sys.argv[0]))[0]
scriptversion = '0.1'
AuthorName="Taha Zerrouki"
def usage():
# "Display usage options"
    print "(C) CopyLeft 2007, %s"%AuthorName
    print "Usage: %s -f filename [OPTIONS]" % scriptname
#"Display usage options"
    print "\t[-h | --help]\t\toutputs this usage message"
    print "\t[-V | --version]\tprogram version"

    print "\t[-f | --file= filename]\tinput file to %s"%scriptname
    print "\t[-o | --out= output format]\toutput format(csv,python,sql)"
    print "\t[-A | --notall]\t don't generate all forms"
    print "\r\nThis program is licensed under the GPL License\n"


def grabargs():
    parser = argparse.ArgumentParser(description='Convert Quran Corpus into CSV format.')
    # add file name to import and filename to export
    
    parser.add_argument("-f", dest="filename", required=True,
    help="input file to convert", metavar="FILE")
    
    parser.add_argument("-o", dest="outformat", nargs='?',
    help="output format(csv, sql, py)", metavar="FORMAT")
    
    parser.add_argument("--all", type=bool, nargs='?',
                        const=True, 
                        help="Generate all stopwords forms")
    args = parser.parse_args()
    return args
def grabargs2():
#  "Grab command-line arguments"
    fname = ''
    outputformat = 'csv'
    allforms = True

    if not sys.argv[1:]:
        usage()
        sys.exit(0)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "AhV:f:o:",
                               ["help", "version","notall"
                                 "file=", "out="],)
    except getopt.GetoptError:
        usage()
        sys.exit(0)
    for o, val in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(0)
        if o in ("-V", "--version"):
            print scriptversion
            sys.exit(0)
        if o in ("-A", "--notall"):
            allforms = False            
        if o in ("-f", "--file"):
            fname = val
        if o in ("-o", "--out"):
            outputformat = val;
        else:
            outputformat = 'csv';   
    return (fname,outputformat, allforms)

def main():
    
    #~ filename,outputformat, allforms =grabargs()
    args = grabargs()
    

    outputformat = string.lower(args.get)
    filename = args.filename
    outputformat = string.lower(args.outformat)
    allforms = args.all


    if outputformat not in ('csv','python','sql'):
        outputformat='csv';
    print "# generated format",outputformat
    print "#file name ",filename
    if outputformat=='python':
        print "STOPWORDS={}";
    elif outputformat=='sql':
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
##      text=" ".join([text,chomp(line)])
        line=fl.readline().decode("utf8");
        line=chomp(line);
        if not line.startswith("#"):
            listword=line.split(";");
            if len(listword)>=9:
                #word=ar_strip_marks(listword[0].strip());
                word=listword[0].strip();
                type_word=listword[1];
                class_word=listword[2];
                has_conjuction=listword[3];
                has_definition=listword[4];
                has_preposition=listword[5];
                has_pronoun=listword[6];
                has_interrog=listword[7];
                has_conjugation=listword[8];                
                has_qasam=listword[9];
                is_defined=listword[10];
                has_conjuction  = False if has_conjuction == "*"  else True
                has_definition  = False if has_definition == "*"  else True
                has_preposition = False if has_preposition == "*" else True
                has_pronoun     = False if has_pronoun == "*"     else True;
                has_interrog    = False if has_interrog == "*"    else False;
                has_conjugation = False if has_conjugation == "*" else True;                    
                has_qasam = True if has_qasam==u"ل" else False;
                is_defined = True if is_defined==u"ف" else False;                
                #~if has_conjuction=="*":
                    #~has_conjuction=False;
                #~else:
                    #~has_conjuction=True;
                #~if has_definition=="*":
                    #~has_definition=False;
                #~else:
                    #~has_definition=True;
#~
                #~if has_preposition=="*":
                    #~has_preposition=False;
                #~else:
                    #~has_preposition=True;
#~
                #~if has_pronoun=="*":
                    #~has_pronoun=False;
                #~else:
                    #~has_pronoun=True;
                #~if has_interrog=="*":
                    #~has_interrog=False;
                #~else:
                    #~has_interrog=True;
                #~if has_conjugation=="*":
                    #~has_conjugation=False;
                #~else:
                    #~has_conjugation=True;                 
                #~if has_qasam==u"ل":
                    #~has_qasam=True;
                #~else:
                    #~has_qasam=False;
                #~if is_defined==u"ف":
                    #~is_defined=True;
                #~else:
                    #~is_defined=False;                   
                list0=generate_allforms(word,type_word, class_word,has_pronoun,has_conjuction,has_preposition,has_definition,has_interrog,has_conjugation, has_qasam,is_defined);
                for item in list0:
                    l=item['vocalized'];
                    counter_generated+=1;
                    stemmed=l;
                    item['vocalized'] = standardize_form(item['vocalized']);
                    item['word'] = standardize_form(item['word']);
                    standard = ar_strip_marks(item['word']);
                    
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
                    elif outputformat in ('python','py'):
                        fields=u"";
                        for key in item.keys():
                            onefield=u"'%s':u'%s',"%(key,item[key]);
                            fields+=onefield;
                        line= u"STOPWORDS[u'"+standard+"']={"+fields+u"}";                          
                    else:
                        line=u'\t'.join([standard, stemmed])
                    print line.encode('utf8');
        counter+=1
if __name__ == "__main__":
  main()








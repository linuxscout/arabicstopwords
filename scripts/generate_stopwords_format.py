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
    print "\t[-v | --version=]\tprogram version"
    print "\t[-f | --file= filename]\tinput file to %s"%scriptname
    print "\t[-o | --out= output format]\toutput format(csv, python, sql)"
    
    print "\r\nThis program is licensed under the GPL License\n"

def grabargs():
#  "Grab command-line arguments"
    fname = ''
    outputformat = 'csv'
    allforms = True
    version = "N/A"
    if not sys.argv[1:]:
        usage()
        sys.exit(0)
    try:
        opts,  args = getopt.getopt(sys.argv[1:],  "AhV:f:o:", 
                               ["help",  "version=", 'notall', 
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
        if o in ("-v",  "--version"):
            version = val
        if o in ("-f",  "--file"):
            fname = val
        if o in ("-o",  "--out"):
            outputformat = val;
        else:
            outputformat = 'csv';    
    return (fname, outputformat,  allforms, version)

def main():

    filename, outputformat,  allforms, version=grabargs()

    outputformat = string.lower(outputformat)
    if outputformat not in ('csv', 'python', 'sql'):
        outputformat='csv';
    print "--~# generated format", outputformat
    print "--~#file name ", filename
    print "--~#output format", outputformat
    #~sys.exit()
    if outputformat=='python':
        import pydict
        mydict = pydict.PyDict(allforms, version)
    elif outputformat=='sql':
        import sqldict
        mydict = sqldict.SqlDict(allforms, version)
    else:
        import csvdict
        mydict = csvdict.CsvDict(allforms, version)

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
    limit=10000;
    nb_fields = 9
    stop_table =[]
    while line :
        line= line.strip('\n').strip()
        if not line.startswith("#"):
            liste=line.split("\t");
            if len(liste) >= nb_fields:
                stop_table.append(liste);

        line=fl.readline().decode("utf8");
    fl.close();
    # create header
    line =  mydict.add_header().encode('utf8')
    if line:  print line
    for tuple_stop in stop_table[:limit]:
        line = mydict.add_record(tuple_stop).encode('utf8')
        if line: 
            print line
    # create footer
    line = mydict.add_footer().encode('utf8')                  
    if line:  print line
if __name__ == "__main__":
  main()








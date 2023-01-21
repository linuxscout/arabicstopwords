#!/usr/bin/python
# -*- coding=utf-8 -*-
##from analex import *

import sys
import re
import  getopt
import os
import string
import argparse
from pyarabic.araby import *
import pyarabic.arabrepr 
arabicrepr = pyarabic.arabrepr.ArabicRepr()
from ar_stowords import *
scriptname = os.path.splitext(os.path.basename(sys.argv[0]))[0]
scriptversion = '0.1'
AuthorName="Taha Zerrouki"


def grabargs():
    parser = argparse.ArgumentParser(description='Convert Quran Corpus into CSV format.')
    # add file name to import and filename to export
    
    parser.add_argument("-f", dest="filename", required=True,
    help="input file to convert", metavar="FILE")
    
    parser.add_argument("-o", dest="outformat", nargs='?',
    help="output format(csv, sql, py)", metavar="FORMAT")

    parser.add_argument("-v", dest="version", nargs='?',
    help="PRelease version", metavar="Version")
    
    parser.add_argument("-a",dest="all", type=bool, nargs='?',
                        const=True, 
                        help="Generate all stopwords forms")
    args = parser.parse_args()
    return args

def main():

    args = grabargs()
    #~ filename, outputformat,  allforms, version=grabargs()
    filename = args.filename
    outputformat = args.outformat
    allforms = True if args.all else False
    version = args.version if args.version else ""
    #~ print(filename, outputformat, allforms, version)
    #~ sys.exit()

    outputformat = outputformat.lower()
    if outputformat not in ('csv', 'python', 'py', 'sql'):
        outputformat='csv';
        #~ print "--~# generated format", outputformat
        #~ print "--~#file name ", filename
        #~ print "--~#output format", outputformat
    
    #~sys.exit()
    if outputformat in ('python', 'py'):
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
        print(" Error :No such file or directory: %s" % filename)
        return None;
    line=fl.readline()#.decode("utf8");
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

        line=fl.readline()#.decode("utf8");
    fl.close();
    # create header
    line =  mydict.add_header()#.encode('utf8')
    if line:  print(line)
    for tuple_stop in stop_table[:limit]:
        line = mydict.add_record(tuple_stop)#.encode('utf8')
        if line: 
            print(line)
    # create footer
    line = mydict.add_footer()#.encode('utf8')                  
    if line:  print(line)
if __name__ == "__main__":
  main()








#!/usr/bin/python
# -*- coding=utf-8 -*-
#
import re,  string, sys
from arabic_const import *

def chomp(s):
  if (s.endswith('\n')):
    return s[:-1]
  else:
    return s

#-----------------------------------------------
#
#
#-----------------------------------------------
pronouns=(
YEH, 
KAF, 
HEH, 
YEH, 
KAF+MEEM, 
KAF+NOON, 
HEH+ALEF, 
HEH+MEEM, 
HEH+NOON, 
NOON+ALEF, 
KAF+MEEM+ALEF, 
HEH+MEEM+ALEF, 

);
jonction=(WAW, FEH);
prepositions=(BEH, KAF, LAM);
definition=(u''.join([ALEF, LAM]));

def generate_allforms(word, has_pronouns=False, has_jonction=False, has_preposition=False, has_definition=False, has_interrog=False, has_conjugation=False, has_qasam=False, is_defined=False):
	mylist=[word];
	temp=[];
	if has_preposition :
		for w in mylist:
			for pr in prepositions:
				temp.append("-".join([pr, w]));
	if has_qasam :
		temp.append("-".join([LAM, word]));					
	mylist+=temp;
	temp=[];
	if has_jonction :
		for w in mylist:
#			temp.append(w)
			for jo in jonction:
				temp.append(jo+"-"+w);
	mylist+=temp;
	temp=[];
	if has_interrog :
		for w in mylist:
#			temp.append(w)
			temp.append(ALEF_HAMZA_ABOVE+"-"+w);
	mylist+=temp;
	temp=[];
	
	if has_pronouns:
		for word in mylist:
			for p in pronouns:
				temp.append(word+"-"+p);			
			# add alef lam ta3rif
			if has_definition:
				temp.append(ALEF+LAM+"-"+word)
	mylist+=temp;
	return mylist;


def standardize_form(word):
    word=re.sub(u"%s-%s"%(ALEF_MAKSURA, YEH), YEH, word)
    word=re.sub(u"%s-"%ALEF_MAKSURA, YEH, word)	
    word=re.sub(u"%s-"%TEH_MARBUTA, TEH, word)
    word=re.sub(u"%s-%s%s%s"%(LAM, ALEF, LAM, LAM), LAM+LAM, word)
    word=re.sub(u"%s-%s%s"%(LAM, ALEF, LAM), LAM+LAM, word)
    word=re.sub(u"-", '',  word);
    return word;

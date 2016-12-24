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
def generate_allforms2(word,type_word, class_word, has_pronoun, has_conjuction,has_preposition,has_definition,has_interrog,has_conjugation, has_qasam,is_defined):
    fields = {}

    fields['word'] = word
    fields['type_word'] = type_word
    fields['class_word'] = class_word
    fields['has_pronoun'] = has_pronoun
    
    fields['has_conjuction'] = has_conjuction
    fields['has_preposition'] = has_preposition
    fields['has_definition'] = has_definition
    fields['has_interrog'] = has_interrog

    fields['has_conjugation'] = has_conjugation 
    fields['has_qasam'] = has_qasam
    fields['is_defined'] = is_defined 

    return generate_allforms(fields)
    
def generate_allforms(fields):
    """ Conjugate the stop words with affixes"""
    word = fields['word']
    if not word:
        return []
    mylist=[word, ];
    temp=[];
    if fields['has_preposition'] :
        for w in mylist:
            for pr in prepositions:
                try:
                    temp.append("-".join([pr, w]));
                except:
                    print (u"'%s', '%s"%(pr,w)).encode('utf8'), 
                    sys.exit()
    if fields['has_qasam'] :
        temp.append("-".join([LAM, word]));                 
    mylist+=temp;
    temp=[];
    if fields['has_conjuction'] :
        for w in mylist:
#           temp.append(w)
            for jo in jonction:
                temp.append(jo+"-"+w);
    mylist+=temp;
    temp=[];
    if fields['has_interrog'] :
        for w in mylist:
#           temp.append(w)
            temp.append(ALEF_HAMZA_ABOVE+"-"+w);
    mylist += temp;
    temp=[];
    
    if fields['has_pronoun']:
        for word in mylist:
            for p in pronouns:
                temp.append(word+"-"+p);            
            # add alef lam ta3rif
            if fields['has_definition']:
                temp.append(ALEF+LAM+"-"+word)
    mylist += temp;
    return mylist;


def standardize_form(word):
    word=re.sub(u"%s-%s"%(ALEF_MAKSURA, YEH), YEH, word)
    word=re.sub(u"%s-"%ALEF_MAKSURA, YEH, word) 
    word=re.sub(u"%s-"%TEH_MARBUTA, TEH, word)
    word=re.sub(u"%s-%s%s%s"%(LAM, ALEF, LAM, LAM), LAM+LAM, word)
    word=re.sub(u"%s-%s%s"%(LAM, ALEF, LAM), LAM+LAM, word)
    word=re.sub(u"-", '',  word);
    return word;

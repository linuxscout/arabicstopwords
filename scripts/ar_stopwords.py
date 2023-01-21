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

def generate_allforms(fields):
    """ Conjugate the stop words with affixes"""
    word = u";%s;"%fields['word']
    if not word:
        return []
    tag = fields['type_word']+";"+fields['class_word']
    mylist=[(word, tag), ];
    temp=[];
    
    if not fields['has_pronoun']: # to avoid adding Al-ta3rif with pronoun
        # add alef lam ta3rif
        for word, t in mylist:
            if fields['has_definition']:
                temp.append((ALEF+LAM+"-"+word, t+u";تعريف"))       
    if fields['has_preposition'] :
        for w, t in mylist:
            for pr in prepositions:
                try:
                    temp.append(("-".join([pr, w]),t+u";مجرور"));
                except:
                    print (u"'%s', '%s"%(pr,w)).encode('utf8'), 
                    sys.exit()
    if fields['has_qasam'] :
        temp.append(("-".join([LAM, word]),u";قسم"));                 
    mylist+=temp;
    temp=[];
    if fields['has_conjuction'] :
        for w,t in mylist:
#           temp.append(w)
            for jo in jonction:
                temp.append((jo+"-"+w,t+u";عطف"));
    mylist+=temp;
    temp=[];
    if fields['has_interrog'] :
        for w,t in mylist:
#           temp.append(w)
            temp.append((ALEF_HAMZA_ABOVE+"-"+w, t+u";استفهام"));
    mylist += temp;
    temp=[];
    
    if fields['has_pronoun']:
        for word, t in mylist:
            for p in pronouns:
                temp.append((word+"-"+p,t+u";ضمير"));            
                if p == YEH  and fields['type_word'] == u"فعل":
                    temp.append((word+"-"+NOON+p,t+u";ضمير"));                 

                        
            # add alef lam ta3rif
            if fields['has_definition']:
                temp.append((ALEF+LAM+"-"+word, t+u";تعريف"))
     
        
    mylist += temp;
    return mylist;
    


def standardize_form(word):
    word = word.replace(';','')
    # حالة سوى
    word=re.sub(u"سوى-","سوا", word)    
    word=re.sub(u"%s-%s"%(ALEF_MAKSURA, YEH), YEH, word)
    word=re.sub(u"%s-%s"%(ALEF_MAKSURA, YEH), YEH, word)
    word=re.sub(u"%s-%s"%(YEH, YEH), YEH, word)

    word=re.sub(u"%s-"%ALEF_MAKSURA, YEH, word)
    word=re.sub(u"%s-"%TEH_MARBUTA, TEH, word)
    word=re.sub(u"%s-%s%s%s"%(LAM, ALEF, LAM, LAM), LAM+LAM, word)
    word=re.sub(u"%s-%s%s"%(LAM, ALEF, LAM), LAM+LAM, word)
    
    # Hamza on finale position
    word = re.sub(r"([%s]-)?([%s])-(.+)%s-(.+)"%(WAW+FEH, KAF+LAM+BEH, HAMZA),r"\1\2-\3%s-\4"%YEH_HAMZA,word)
    
    word=re.sub(u"-", '',  word);
    return word;

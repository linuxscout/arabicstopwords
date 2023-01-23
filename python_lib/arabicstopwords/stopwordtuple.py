#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stopwordtuple.py
#  
#  Copyright 2018 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import pyarabic.araby as araby
try:
    from stopwordsallforms import STOPWORDS, STOPWORDS_INDEX
    from stopwords_classified import STOPWORDS as classed_STOPWORDS
except:
    from .stopwordsallforms import STOPWORDS, STOPWORDS_INDEX
    from .stopwords_classified import STOPWORDS as classed_STOPWORDS  

class stopwordTuple:
    """
    A object to handle the stopword tuple in two types: classified, or stemmed
    """
    def __init__(self, stop_dict = {}):
        """
        Init stopword tuples
        """
        self.stop_dict = stop_dict
        
    #---------------------------
    # Stopwords features
    #---------------------------
     # ~ {'word': 'إن',
     
     # ~ 'vocalized': 'إِنْ',
     # ~ 'type_word': 'حرف',
     # ~ 'class_word': 'حرف جزم',
        
     
     
    def get_features_dict(self,):
        """
         return the all features for  a stopword
        """
        return self.stop_dict


    def get_feature(self,feature):
        """
         return the asked feature form  a stopword
        """
        return self.stop_dict.get(feature,'')
        
    def get_vocalized(self,):
        """
         return the vocalized form fo a stopword
        """
        return self.stop_dict.get('vocalized','')

    def get_unvocalized(self,):
        """
         return the unvocalized form fo a stopword
        """
        return self.stop_dict.get('word','')


    def get_wordtype(self,):
        """
         return the wordtype form fo a stopword
        """
        # return type or word_type 
        return self.stop_dict.get('type',self.stop_dict.get('type_word',''))       



    def get_wordclass(self,):
        """
        return the word sub class form fo a stopword
        """
        return self.stop_dict.get('class_word','')
        
    # ~ 'has_conjuction': 1,
     # ~ 'has_definition': 0,
     # ~ 'has_preposition': 0,
     # ~ 'has_pronoun': 0,
     # ~ 'has_interrog': 0,
     # ~ 'has_conjugation': 0,
     # ~ 'has_qasam': 0,
     # ~ 'is_defined': 0,
     # ~ 'is_inflected': 0,
     # ~ 'tanwin': 0,
     # ~ 'action': 'جازم',
     # ~ 'object_type': 'فعل',
     # ~ 'need': ''},

    def accept_conjuction(self,):
        """
         return True if the word  accept conjuctions, Asked only for classified stopwords
        """
        return bool(self.stop_dict.get('has_conjuction',0))
        
        
    def accept_definition(self,):
        """
        return True if the word  accept definitions, Asked only for classified stopwords
        """
        return bool(self.stop_dict.get('has_definition',0))

        
        
    def accept_preposition(self,):
        """
         return True if the word  accept prepositions, Asked only for classified stopwords
        """
        return bool(self.stop_dict.get('has_preposition',0))



    def accept_pronoun(self,):
        """
         return True if the word  accept pronouns, Asked only for classified stopwords
        """
        return bool(self.stop_dict.get('has_pronoun',0))


    def accept_interrog(self, ):
        """
         return True if the word  accept interrogs, Asked only for classified stopwords
        """
        return bool(self.stop_dict.get('has_interrog',0))


    def accept_conjugation(self,):
        """
         return True if the word  accept conjugations, Asked only for classified stopwords
        """
        return bool(self.stop_dict.get('has_conjugation',0))


    def accept_qasam(self,):
        """
         return True if the word  accept qasams, Asked only for classified stopwords
        """
        return bool(self.stop_dict.get('has_qasam',0))


    def is_defined(self,):
        """
         return True if the word  is defined , Asked only for classified stopwords
        """
        return bool(self.stop_dict.get('is_defined',0))


    def accept_inflection(self,):
        """
         return True if the word  accept inflections, Asked only for classified stopwords
        """
        return bool(self.stop_dict.get('is_inflected',0))


    def accept_tanwin(self,):
        """
         return True if the word  accept tanwins, Asked only for classified stopwords
        """
        return bool(self.stop_dict.get('tanwin',0))


    def get_action(self,):
        """
         return  get action, Asked only for classified stopwords
        """
        return self.stop_dict.get('action',"")


    def get_object_type(self,):
        """
        return   get object_type, Asked only for classified stopwords
        """
        return self.stop_dict.get('object_type',"")


    def get_need(self,):
        """
         return  get need, Asked only for classified stopwords
        """
        return self.stop_dict.get('need',"")

    def get_tags(self,):
        """
         return True if the word  get tags, 
        """
        return self.stop_dict.get('tags',"")

    def get_stem(self,):
        """
         return True if the word  get stems, 
        """
        return self.stop_dict.get('stem',"")
    

    def get_enclitic(self,):
        """
         return get encletic, 
        """
        return self.stop_dict.get('encletic',"")        

    

    def get_procletic(self,):
        """
         return  get procletic, 
        """
        return self.stop_dict.get('procletic','')
    

    def get_lemma(self,):
        """
         return   get lemma, 
        """
        return self.stop_dict.get('original','')

    def __str__(self):
        """
        return tuple as string
        """
        return self.stop_dict.__str__()


    def __getitem__(self, key):
        """
        return attribute
        """
        return self.stop_dict.get(key,None)
        
    def get(self, key, default):
        """
        return attribute
        """
        return self.stop_dict.get(key,default)
    
def main(args):
    word = u"لعلهم"
    print(stop_stem(word))
    return 0
    
if __name__ == '__main__':
    import sys
    from pyarabic.arabrepr import arepr
    words = [(u'منكم', True),
            (u'ممكن', False),
            (u'عندما', True),
            (u'حينئذ', True),
]
    for w, rep  in words:
        result = is_stop(w)
        if result != rep:
            print((u"Error %s is %swhere must be %s"%(w, result, rep)).encode('utf8'))

    print(len(stopwords_list()))
    print(len(classed_stopwords_list()))
    print(arepr(stopword_forms(u'حتى')))
    print(arepr(stopword_forms(u'جميع')))
    print(arepr(stop_stem(u'لجميعهم')))
    print(arepr(stop_stem(u'لجم')))

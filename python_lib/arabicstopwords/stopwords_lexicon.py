#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stopwords_lexicon.py
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

__version__ = '0.4.3'
__author__ = 'Taha Zerrouki'

import pyarabic.araby as araby
try:
    from stopwordsallforms import STOPWORDS, STOPWORDS_INDEX
    from stopwords_classified import STOPWORDS as classed_STOPWORDS
except:
    from .stopwordsallforms import STOPWORDS, STOPWORDS_INDEX
    from .stopwords_classified import STOPWORDS as classed_STOPWORDS
try:
    from stopwordtuple import stopwordTuple
except:
    from .stopwordtuple import stopwordTuple

class stopwords_lexicon:
    """
    A lexicon class for stopwords extracttion features
    """
    def __init__(self, ):
        self.forms_dict  = STOPWORDS
        self.lemmas_dict = classed_STOPWORDS
        self.vocalized_lemmas_dict = self.create_vocalized_index(self.lemmas_dict)
        self.vocalized_forms_dict  = self.create_vocalized_index(self.forms_dict)
        self.categories = self.create_categories_index()
        
    def create_vocalized_index(self, table):
        """
        Create index of vocalized lemmas
        """
        voca_dict = {}
        for unvoc_key in table:
            for item in table[unvoc_key]:
                vocalized = item.get('vocalized',"")
                if vocalized:
                    if vocalized in voca_dict:
                        voca_dict[vocalized].append(item)
                    voca_dict[vocalized] = [item,]
        return voca_dict

    def create_categories_index(self,):
        """
        Create index of categories
        """
        index_dict = {}
        for table, table_type in [(self.forms_dict, "forms"), (self.lemmas_dict, "lemmas"),]:
            for unvoc_key in table:
                for item in table[unvoc_key]:
                    vocalized = item.get('vocalized',"")
                    category  = item.get('type_word',item.get('type',""))
                    if category:
                        if category not in index_dict:
                            index_dict[category] = {}
                        if table_type not in index_dict[category]:
                            index_dict[category][table_type] = []
                            index_dict[category][table_type+'_vocalized'] = []

                        index_dict[category][table_type].append(unvoc_key)
                        index_dict[category][table_type+'_vocalized'].append(vocalized)
        return index_dict
    #---------------------------
    # Stopwords lookup
    #---------------------------
    def is_stop(self, word):
        """ test if word is a stop"""
        return word in self.forms_dict

    def stop_stemlist(self, word):
        """ return all stems for a word"""
        return self.get_stems(word)


    def stop_stem(self, word):
        """ retrun a stem of a stop word """
        stemlist = self.get_stems(word)
        if stemlist:
            return stemlist[0]
        else:
            return ""
        
    def stopwords_list(self, vocalized=False):
        """ return all arabic stopwords"""
        if not vocalized:
            return list(self.forms_dict.keys())
        else:
            vocalized_list = []
            for x in self.forms_dict.keys():
                vocalized_list.extend(self.get_vocalizeds(x))
            return vocalized_list
            
        
    def classed_stopwords_list(self, vocalized=False):
        """ return all arabic classified  stopwords"""
        if not vocalized:
            return list(self.lemmas_dict.keys())
        else:
            vocalized_list = []
            for x in self.lemmas_dict.keys():
                vocalized_list.extend(self.get_vocalizeds(x))
            return vocalized_list

        
    def stopword_forms(self, word):
        """ return all forms for a stop word"""
        if word in STOPWORDS_INDEX:
            return [d for d in STOPWORDS_INDEX[word] ]
        else:
            return []
     
     
    def get_features_dict(self, word, lemma=False):
        """
         return the all features for  a stopword
        """
        if not lemma:
            stemlist = self.forms_dict.get(word,{})
        else:
            stemlist = self.lemmas_dict.get(word,{})
        return stemlist
        
    def get_stopwordtuples(self, word, lemma=False, vocalized=False):
        """
         return the all features for  a stopword
        """
        if not lemma:
            if vocalized:
                stemlist = self.vocalized_forms_dict.get(word, [])  
            else:
                stemlist = self.forms_dict.get(word, [])

        else:
            if vocalized:
                stemlist = self.vocalized_lemmas_dict.get(word, [])
            else:
                stemlist = self.lemmas_dict.get(word, [])                
        stoptuple_list = []
        for item in stemlist:
           stoptuple_list.append(stopwordTuple(item)) 
        return stoptuple_list
    
    
    def get_categories(self):
        """
        Get all categories (wordtypes available in the lexicon)
        """
        return list(self.categories.keys())


    def get_by_category(self, category="", lemma=False, vocalized=False):
        """
        Get all stopwords  (wordtypes available in the lexicon)
        """
        secondkey = ""
        if lemma:
            secondkey = "lemmas"
        else:
            secondkey = "forms"
        
        if vocalized:
            secondkey += "_vocalized"
       
        return self.categories.get(category, {}).get(secondkey, [])
        
        
    #---------------------------
    # Stopwords features
    #---------------------------

    def get_feature(self, word, feature, lemma=False):
        """
         return the asked feature form  a stopword
        """
        if not lemma:
            stemlist = [d.get(feature,'') for d in self.forms_dict.get(word,{}) if d.get(feature,'')]    
        else:
            stemlist = [d.get(feature,'') for d in self.lemmas_dict.get(word,{}) if d.get(feature,'')]
        stemlist = list(set(stemlist))                  
        return stemlist
        
    def get_vocalizeds(self, word, lemma=False):
        """
         return the vocalized form fo a stopword
        """
        if not lemma:
            stemlist = [d.get('vocalized','') for d in self.forms_dict.get(word,{}) if d.get('vocalized','')]    
        else:
            stemlist = [d.get('vocalized','') for d in self.lemmas_dict.get(word,{}) if d.get('vocalized','') ]                
        stemlist = list(set(stemlist))   
        return stemlist


    def get_wordtypes(self, word, lemma=False):
        """
         return the wordtype form fo a stopword
        """
        if not lemma:
            stemlist = [d.get('type','') for d in self.forms_dict.get(word,{}) if d.get('type','')]    
        else:
            stemlist = [d.get('type_word','') for d in self.lemmas_dict.get(word,{}) if d.get('type_word','')]
        stemlist = list(set(stemlist))
        return stemlist


    def get_wordclass(self, word):
        """
        return the word sub class form fo a stopword
        """
        stemlist = [d.get('class_word','') for d in self.lemmas_dict.get(word,{}) if d.get('class_word','')]    
        stemlist = list(set(stemlist))
        return stemlist
        
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

    # ~ def accept_conjuction(self, word):
        # ~ """
         # ~ return True if the word  accept conjuctions, Asked only for classified stopwords
        # ~ """
        # ~ return bool(self.vocalized_lemmas_dict.get(word,{}).get('has_conjuction',0))
        
        
    # ~ def accept_definition(self, word):
        # ~ """
        # ~ return True if the word  accept definitions, Asked only for classified stopwords
        # ~ """
        # ~ return bool(self.vocalized_lemmas_dict.get(word,{}).get('has_definition',0))

        
        
    # ~ def accept_preposition(self, word):
        # ~ """
         # ~ return True if the word  accept prepositions, Asked only for classified stopwords
        # ~ """
        # ~ return bool(self.vocalized_lemmas_dict.get(word,{}).get('has_preposition',0))



    # ~ def accept_pronoun(self, word):
        # ~ """
         # ~ return True if the word  accept pronouns, Asked only for classified stopwords
        # ~ """
        # ~ return bool(self.vocalized_lemmas_dict.get(word,{}).get('has_pronoun',0))


    # ~ def accept_interrog(self, word):
        # ~ """
         # ~ return True if the word  accept interrogs, Asked only for classified stopwords
        # ~ """
        # ~ return bool(self.vocalized_lemmas_dict.get(word,{}).get('has_interrog',0))


    # ~ def accept_conjugation(self, word):
        # ~ """
         # ~ return True if the word  accept conjugations, Asked only for classified stopwords
        # ~ """
        # ~ return bool(self.vocalized_lemmas_dict.get(word,{}).get('has_conjugation',0))


    # ~ def accept_qasam(self, word):
        # ~ """
         # ~ return True if the word  accept qasams, Asked only for classified stopwords
        # ~ """
        # ~ return bool(self.vocalized_lemmas_dict.get(word,{}).get('has_qasam',0))


    # ~ def is_defined(self, word):
        # ~ """
         # ~ return True if the word  is defined , Asked only for classified stopwords
        # ~ """
        # ~ return bool(self.vocalized_lemmas_dict.get(word,{}).get('is_defined',0))


    # ~ def accept_inflection(self, word):
        # ~ """
         # ~ return True if the word  accept inflections, Asked only for classified stopwords
        # ~ """
        # ~ return bool(self.vocalized_lemmas_dict.get(word,{}).get('is_inflected',0))


    # ~ def accept_tanwin(self, word):
        # ~ """
         # ~ return True if the word  accept tanwins, Asked only for classified stopwords
        # ~ """
        # ~ return bool(self.vocalized_lemmas_dict.get(word,{}).get('tanwin',0))


    # ~ def get_action(self, word):
        # ~ """
         # ~ return  get action, Asked only for classified stopwords
        # ~ """
        # ~ return self.vocalized_lemmas_dict.get(word,{}).get('action',"")


    # ~ def get_object_type(self, word):
        # ~ """
        # ~ return   get object_type, Asked only for classified stopwords
        # ~ """
        # ~ return self.vocalized_lemmas_dict.get(word,{}).get('object_type',"")


    # ~ def get_need(self, word):
        # ~ """
         # ~ return  get need, Asked only for classified stopwords
        # ~ """
        # ~ return self.vocalized_lemmas_dict.get(word,{}).get('need',"")

    def get_tags(self, word):
        """
         return True if the word  get tags, 
        """
        stemlist = [d.get('tags','') for d in self.forms_dict.get(word,{}) if d.get('tags','')] 
        stemlist = list(set(stemlist))           
        return stemlist
    

    def get_stems(self, word):
        """
         return True if the word  get stems, 
        """
        stemlist = [d.get('stem','') for d in self.forms_dict.get(word,{}) if d.get('stem','')]    
        stemlist = list(set(stemlist))
        return stemlist
    

    def get_enclitics(self, word):
        """
         return get encletic, 
        """
        stemlist = [d.get('encletic','') for d in self.forms_dict.get(word,{}) if d.get('encletic','')]  
        stemlist = list(set(stemlist))
        return stemlist
    

    def get_procletics(self, word):
        """
         return  get procletic, 
        """
        stemlist = [d.get('procletic','') for d in self.forms_dict.get(word,{}) if d.get('procletic','')]
        stemlist = list(set(stemlist))
        return stemlist
    

    def get_lemmas(self, word):
        """
         return   get lemma, 
        """
        stemlist = [d.get('original','') for d in self.forms_dict.get(word,{}) if d.get('original','')] 
        stemlist = list(set(stemlist))           
        return stemlist
    
    
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

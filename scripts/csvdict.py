#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  csvdict.py
#  
#  Copyright 2016 zerrouki <zerrouki@majd4>
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

import time
import pyarabic.araby as araby
import ar_stopwords 
import sys

class CsvDict:
    """ a virtual converter of data from table to specific format
    the data is big, then every function print string """
    def __init__(self,  allforms = True, version = "N/A"):
        """
        initiate the dict
        """
        self.id = 0
        self.version = version
        #~ self.generate_all_forms = True
        self.generate_all_forms = allforms
        #generic Header for project
        self.headerlines = [ "*************************************",
        "Arabic Stop word list for morphology analysis and information retrival",
                    "Version        : %s"%self.version,
                    "Generated at   : %s "%time.strftime("%Y/%m/%d:%H:%M"),                    
                    "Author         : Taha Zerrouki", 
                    "Web            : http://arabicstopwords.sf.net",
                    "Source         : http://github.com/linuxscout/arabicstopwords",
                    "*************************************",
                    ] 
        self.field_id={
                'vocalized': 0, 
                'type_word': 1,
                'class_word': 2,
                'has_conjuction' : 3 ,
                'has_definition' : 4 ,
                'has_preposition' : 5 ,
                'has_pronoun' : 6 ,
                'has_interrog' : 7 ,
                'has_conjugation' : 8 ,
                'has_qasam' : 9 ,
                'is_defined' : 10 ,
                'is_inflected' : 11,
                'tanwin' : 12,
                'action' : 13,              
                'object_type' : 14,            
                'need' : 15,
        }
        #give the display order for text format display
        self.display_order= {}
        self.display_order[True] =[
                'vocalized',
                'stemmed',
                #~ 'word',
                #~ 'standard',
                ]
        self.display_order[False] =[
                'vocalized', 
                'type_word',
                'class_word',
                'has_conjuction' ,
                'has_definition' ,
                'has_preposition' ,
                'has_pronoun'  ,
                'has_interrog' ,
                'has_conjugation',                 
                'has_qasam' ,
                'is_defined' ,
                'is_inflected' ,
                'tanwin' ,
                'action' ,              
                'object_type' ,            
                'need',
                ]
                
        self.boolean_fields=[
                'has_conjuction' , 
                'has_definition' ,
                'has_preposition' , 
                'has_pronoun' ,
                'has_interrog',
                'has_conjugation' ,                
                'has_qasam' , 
                'is_defined' ,
                'is_inflected' ,
                'tanwin',
                ]       
    def add_header(self,):
        """
        add the header for new dict
        """
        line = "#" + "\n#".join(self.headerlines) + "\n"
        #~ line += u"\t".join(["id", "word", "unvocalized" , "root" , "future_type" ,"triliteral"  , "transitive"  , "double_trans"  , "think_trans"  , "unthink_trans"  , "reflexive_trans"  , "past"  , "future"  ,  "imperative"  ," passive"  , " future_moode"  , "confirmed"])
        return line
         
    def add_record(self, stop_row):
        """
        Add a new to the dict
        """
        self.id += 1
        fields_table = self.treat_tuple(stop_row) 
        lines = []
        # display
        for fields in fields_table:
            items=[];
            for k in range(len(self.display_order[self.generate_all_forms])):
                key = self.display_order[self.generate_all_forms][k];
                # some fields are integer, than we use str
                try:
                    items.append(unicode(fields[key]))
                except:
                    print fields
            lines.append(u"\t".join(items))
        
        return u"\n".join(lines)
        
    def add_footer(self):
        """close the data set, used for ending xml, or sql"""
        return ""
        
    def __str__(self,):
        """ return string to  """
        pass;

    def treat_tuple(self,tuple_stop):
        """ convert row data to specific fields
        return a dict of fields"""
        #~ self.id+=1;
        fields = {"id": self.id,}  # verb dict of fields
        # word  tri root    future_type transitive  nb_trans    object_type reflexive_type  tenses  model   nb_case verb_cat    suggest
                
        #extract field from the stowprds tuple
        for key in self.field_id.keys():
            try:
                fields[key] = tuple_stop[self.field_id[key]].strip();
            except IndexError:
                print "#"*5, "key error [%s],"%key, self.field_id[key], len(tuple_stop);
                print (u"\t".join(tuple_stop)).encode('utf8')
                sys.exit()
        # treat special tuples
        fields['word'] = araby.strip_tashkeel(fields['vocalized'])
        # change boolean fields
        for key in self.boolean_fields:
            if not fields[key]: 
                fields[key] = 0
            elif fields[key] == "*":
                fields[key] = 0
            else:
                fields[key] = 1  
        # generate all forms if requested
        fields_table =[]
        if not self.generate_all_forms:
            return [fields, ];
        else:
            tuple_table = ar_stopwords.generate_allforms(fields);

            for conj  in tuple_table:
                fields = {} 
                """
                UNVOCALIZED TEXT NOT NULL,
                PROCLETIC TEXT,
                TAGS TEXT,
                VOCALIZED TEXT,
                STEM TEXT,
                TYPE TEXT,
                ORIGINAL TEXT,
                ENCLETIC TEXT
                """               
                fields['stemmed'] = conj;
                fields['vocalized'] = ar_stopwords.standardize_form(fields['stemmed']);
                fields['word']      = ar_stopwords.standardize_form(fields['stemmed']);
                fields['standard']  = araby.strip_tashkeel(fields['vocalized']);
                
                fields_table.append(fields)
            return fields_table
            

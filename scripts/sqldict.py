#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  verbdict_functions.py
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
import csvdict

class SqlDict(csvdict.CsvDict):
    """ a virtual converter of data from table to specific format
    the data is big, then every function print string """
    def __init__(self,  allforms = True,  version = "N/A"):
        """
        initiate the dict
        """
        csvdict.CsvDict.__init__(self, allforms, version)
        
    def add_header(self,):
        """
        add the header for new dict
        """
        line = "--" + "\n--".join(self.headerlines) +"\n"
        if self.generate_all_forms:      
            line +=  u'''create TABLE STOPWORDS
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
        else:
            line +=  u'''create TABLE classedstopwords
                (
                ID INT UNIQUE NOT NULL, 
                WORD TEXT NOT NULL, 
                vocalized TEXT NOT NULL, 
                word_type TEXT NOT NULL,

                word_class TEXT NOT NULL,
                conjonction tinyint(1) default 0, 
                definition tinyint(1) default 0,  
                preposition tinyint(1) default 0,

                pronoun tinyint(1) default 0, 
                interrog tinyint(1) default 0,
                conjugation tinyint(1) default 0,                     
                qasam tinyint(1) default 0,
                
                defined tinyint(1) default 0,
                is_inflected  int(1) default 0,
                tanwin int(1) default 0,
                action varchar(10) default '', 

                object_type  varchar(10) default '',
                need  varchar(10) default ''                
                );
            ''';            
        return line
               
    def add_record(self, stop_row):
        """
        Add a new to the dict
        """

        lines  = []
        fields_table = self.treat_tuple(stop_row)
        # to reduce the sql file size, 
        # doesn't work with multiple files
        for fields in fields_table:
            self.id +=1
            fields['id'] = self.id
            items=[];
            items.append(u"%d"%fields['id']);                   
            for k in range(len(self.display_order[self.generate_all_forms])):
                key = self.display_order[self.generate_all_forms][k];
                if key in self.boolean_fields:
                    items.append(u"%d"%fields.get(key, 0));
                else:
                    items.append(u"'%s'"%fields.get(key, ""));

            if self.generate_all_forms:
                lines.append("insert into STOPWORDS values (%s);"%u', '.join(items))
            else:
                lines.append("insert into classedstopwords values (%s);"%u', '.join(items))                
        return u"\n".join(lines)
        

    def add_footer(self):
        """close the data set, used for ending xml, or sql"""
        
        return """"""

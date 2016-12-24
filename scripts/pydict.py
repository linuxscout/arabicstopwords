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

class PyDict(csvdict.CsvDict):
    """ a virtual converter of data from table to specific format
    the data is big, then every function print string """
    def __init__(self,  allforms = True, version = "N/A"):
        """
        initiate the dict
        """
        csvdict.CsvDict.__init__(self, allforms, version)
        
    def add_header(self,):
        """
        add the header for new dict
        """
        line = "##" + "\n##".join(self.headerlines) +"\n"
        line += "STOPWORDS={}";
        return line
               
    def add_record(self, stop_row):
        """
        Add a new to the dict
        """
        self.id +=1
        lines = []
        fields_table = self.treat_tuple(stop_row)

        for fields in fields_table:
            #~ fields['id'] = self.id
            items=[];
            #~ items.append(u"%d"%fields['id']);                   
            for k in range(len(self.display_order[self.generate_all_forms])):
                key = self.display_order[self.generate_all_forms][k];
                if key in self.boolean_fields:
                    items.append(u"'%s':%d"%(key, fields[key]));
                else:
                    items.append(u"'%s':u'%s'"%(key, fields[key]));
            lines.append(u"STOPWORDS[u'%s']= {%s}"%(fields['word'], u', '.join(items)));
        return u"\n".join(lines)         
        

    def add_footer(self):
        """close the data set, used for ending xml, or sql"""
        
        return """"""

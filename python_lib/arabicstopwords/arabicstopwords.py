#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stopclass.py
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
from stopwordsallforms import STOPWORDS, STOPWORDS_INDEX
from stopwords_classified import STOPWORDS as classed_STOPWORDS
def is_stop(word):
    """ test if word is a stop"""
    return word in STOPWORDS

def stop_stemlist(word):
    """ test if word is a stop"""
    stemlist = []
    if word in STOPWORDS:
        stemlist = [d.get('stem','') for d in STOPWORDS[word] ]    
    return stemlist
def stop_stem(word):
    """ retrun a stem of a stop word """
    stemlist = stop_stemlist(word)
    if stemlist:
        return stemlist[0]
    else:
        return ""
    
def stopwords_list():
    """ return all arabic stopwords"""
    return STOPWORDS.keys()
    
def classed_stopwords_list():
    """ return all arabic classified  stopwords"""
    return classed_STOPWORDS.keys()
    
def stopword_forms(word):
    """ return all forms for a stop word"""
    if word in STOPWORDS_INDEX:
        return [d for d in STOPWORDS_INDEX[word] ]
    else:
        return []
    
def main(args):
    word = u"لعلهم"
    print stop_stem(word)
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

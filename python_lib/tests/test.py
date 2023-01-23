#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_stopwords.py
#  
#  Copyright 2020 zerrouki <zerrouki@majd4>
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

from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
    division,
    )
import unittest
import sys
sys.path.append('arabicstopwords')
import arabicstopwords.arabicstopwords as stp

class StopWordsTestCase(unittest.TestCase):
    """Tests for `Stopwords.py`."""

    def test_is_stopword(self):
        """Test is_stop"""
        self.assertEqual(stp.is_stop(u'ممكن'), False)
        self.assertEqual(stp.is_stop(u'منكم'), True)
        self.assertEqual(stp.is_stop(u'عندما'), True)
        self.assertEqual(stp.is_stop(u'حينئذ'), True)
    def test_stop_stem(self):
        """Test stem stop"""
        word = u"لعلهم"
        self.assertEqual(stp.stop_stem(word), u"لعل")
    def test_stop_stem(self):
        """Test stem stop"""
        word = u"لعلهم"
        self.assertEqual(stp.stop_stem(word), u"لعل")
    def test_stop_list(self):
        """Test stop list"""
        self.assertEqual(len(stp.stopwords_list()), 13572)
        self.assertEqual(len(stp.classed_stopwords_list()), 508)

    def test_stopword_forms(self):
        """Test stopord forms"""
        ala_forms = [u'فلعليه',  u'أفلعليكما',  u'ولعليكن',  u'ولعليهما',  u'أفعليكن',  u'أوعليهن',  u'أفعلينا',  u'ولعليهم',  u'فلعليهن',  u'أفعليه',  u'وعليكن',  u'أوعلى',  u'لعليكما',  u'لعليه',  u'فلعلى',  u'فلعليكما',  u'وعليهم',  u'لعلي',  u'أفعليها',  u'ألعليهم',  u'أولعليهم',  u'لعلى',  u'وعلي',  u'عليهم',  u'لعليهن',  u'أعليك',  u'ألعليك',  u'أفعلي',  u'ألعليكم',  u'أوعليه',  u'فلعليهم',  u'أعلينا',  u'أولعلينا',  u'ولعليها',  u'فلعليكن',  u'أعليكم',  u'لعليها',  u'أعليكما',  u'أعلي',  u'فلعليها',  u'أولعليكما',  u'وعليكم',  u'فلعليكم',  u'أفلعليكم',  u'وعليه',  u'عليكن',  u'فلعليك',  u'أوعليكما',  u'أفعلى',  u'أفعليهن',  u'أولعليه',  u'أعليكن',  u'ولعليكم',  u'ولعليه',  u'ولعليكما',  u'فعلينا',  u'أوعليهم',  u'ألعليكما',  u'أولعلي',  u'فعليها',  u'أولعليهن',  u'أفعليهما',  u'أفعليكما',  u'على',  u'أعليهم',  u'لعليكن',  u'أوعلينا',  u'لعلينا',  u'فلعليهما',  u'فلعلينا',  u'أفعليهم',  u'علينا',  u'عليها',  u'أوعلي',  u'ألعليهن',  u'ولعلينا',  u'وعليهما',  u'فعليهم',  u'أوعليك',  u'ولعلي',  u'ألعلينا',  u'أفلعليهم',  u'ألعليكن',  u'أولعليكم',  u'أفلعلى',  u'لعليهما',  u'ألعليها',  u'أعليهن',  u'أولعليك',  u'ألعليه',  u'ألعلي',  u'أعلى',  u'عليك',  u'لعليك',  u'ولعليك',  u'أعليها',  u'عليهن',  u'أفلعلينا',  u'أوعليكن',  u'وعليها',  u'أفلعلي',  u'أفلعليها',  u'وعلى',  u'ألعلى',  u'فعليكن',  u'فعليكما',  u'لعليكم',  u'فعليكم',  u'أفلعليهن',  u'أولعلى',  u'أفلعليه',  u'أفعليكم',  u'أوعليهما',  u'فعليهن',  u'أعليه',  u'فعليك',  u'أوعليها',  u'عليكم',  u'ألعليهما',  u'فعليهما',  u'أفلعليكن',  u'وعليك',  u'فعليه',  u'فعلى',  u'عليهما',  u'فلعلي',  u'علي',  u'أولعليهما',  u'أفعليك',  u'ولعليهن',  u'ولعلى',  u'وعلينا',  u'أولعليكن',  u'وعليهن',  u'أعليهما',  u'عليه',  u'لعليهم',  u'أولعليها',  u'وعليكما',  u'عليكما',  u'أفلعليك',  u'أفلعليهما',  u'فعلي',  u'أوعليكم']

        self.assertEqual((len(stp.stopword_forms(u"على"))), len(ala_forms))


if __name__ == '__main__':
    unittest.main()

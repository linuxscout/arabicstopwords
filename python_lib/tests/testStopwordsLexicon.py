#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_stopwordslexicon.py
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
import unittest
import sys
sys.path.append('../arabicstopwords')
import stopwords_lexicon as stp


class StopWordsTestCase(unittest.TestCase):
    """Tests for `Stopwords.py`."""
    def __init__(self, *args, **kwargs):
        """
        initial autocorrector
        """
        super(StopWordsTestCase, self).__init__(*args, **kwargs)
        self.lexicon = stp.stopwords_lexicon()

    def test_is_stopword(self):
        """Test is_stop"""
        self.assertEqual(self.lexicon.is_stop(u'ممكن'), False)
        self.assertEqual(self.lexicon.is_stop(u'منكم'), True)
        self.assertEqual(self.lexicon.is_stop(u'عندما'), True)
        self.assertEqual(self.lexicon.is_stop(u'حينئذ'), True)
    def test_stop_stem(self):
        """Test stem stop"""
        word = u"لعلهم"
        self.assertEqual(self.lexicon.stop_stem(word), u"لعل")
    def test_stop_stem(self):
        """Test stem stop"""
        word = u"لعلهم"
        self.assertEqual(self.lexicon.stop_stem(word), u"لعل")
    def test_stop_list(self):
        """Test stop list"""
        self.assertEqual(len(self.lexicon.stopwords_list()), 13572)
        self.assertEqual(len(self.lexicon.classed_stopwords_list()), 508)

    def test_stopword_forms(self):
        """Test stopord forms"""
        ala_forms = [u'فلعليه',  u'أفلعليكما',  u'ولعليكن',  u'ولعليهما',  u'أفعليكن',  u'أوعليهن',  u'أفعلينا',  u'ولعليهم',  u'فلعليهن',  u'أفعليه',  u'وعليكن',  u'أوعلى',  u'لعليكما',  u'لعليه',  u'فلعلى',  u'فلعليكما',  u'وعليهم',  u'لعلي',  u'أفعليها',  u'ألعليهم',  u'أولعليهم',  u'لعلى',  u'وعلي',  u'عليهم',  u'لعليهن',  u'أعليك',  u'ألعليك',  u'أفعلي',  u'ألعليكم',  u'أوعليه',  u'فلعليهم',  u'أعلينا',  u'أولعلينا',  u'ولعليها',  u'فلعليكن',  u'أعليكم',  u'لعليها',  u'أعليكما',  u'أعلي',  u'فلعليها',  u'أولعليكما',  u'وعليكم',  u'فلعليكم',  u'أفلعليكم',  u'وعليه',  u'عليكن',  u'فلعليك',  u'أوعليكما',  u'أفعلى',  u'أفعليهن',  u'أولعليه',  u'أعليكن',  u'ولعليكم',  u'ولعليه',  u'ولعليكما',  u'فعلينا',  u'أوعليهم',  u'ألعليكما',  u'أولعلي',  u'فعليها',  u'أولعليهن',  u'أفعليهما',  u'أفعليكما',  u'على',  u'أعليهم',  u'لعليكن',  u'أوعلينا',  u'لعلينا',  u'فلعليهما',  u'فلعلينا',  u'أفعليهم',  u'علينا',  u'عليها',  u'أوعلي',  u'ألعليهن',  u'ولعلينا',  u'وعليهما',  u'فعليهم',  u'أوعليك',  u'ولعلي',  u'ألعلينا',  u'أفلعليهم',  u'ألعليكن',  u'أولعليكم',  u'أفلعلى',  u'لعليهما',  u'ألعليها',  u'أعليهن',  u'أولعليك',  u'ألعليه',  u'ألعلي',  u'أعلى',  u'عليك',  u'لعليك',  u'ولعليك',  u'أعليها',  u'عليهن',  u'أفلعلينا',  u'أوعليكن',  u'وعليها',  u'أفلعلي',  u'أفلعليها',  u'وعلى',  u'ألعلى',  u'فعليكن',  u'فعليكما',  u'لعليكم',  u'فعليكم',  u'أفلعليهن',  u'أولعلى',  u'أفلعليه',  u'أفعليكم',  u'أوعليهما',  u'فعليهن',  u'أعليه',  u'فعليك',  u'أوعليها',  u'عليكم',  u'ألعليهما',  u'فعليهما',  u'أفلعليكن',  u'وعليك',  u'فعليه',  u'فعلى',  u'عليهما',  u'فلعلي',  u'علي',  u'أولعليهما',  u'أفعليك',  u'ولعليهن',  u'ولعلى',  u'وعلينا',  u'أولعليكن',  u'وعليهن',  u'أعليهما',  u'عليه',  u'لعليهم',  u'أولعليها',  u'وعليكما',  u'عليكما',  u'أفلعليك',  u'أفلعليهما',  u'فعلي',  u'أوعليكم']

        self.assertEqual((len(self.lexicon.stopword_forms(u"على"))), len(ala_forms))
    def test_get_features(self,):
        """Test Extract Features"""
        
        stop_tuple1 = [{'word': 'لكن', 'vocalized': 'لَكِنَّ', 'type_word': 'حرف', 'class_word': 'إن و أخواتها', 'has_conjuction': 1, 'has_definition': 0, 'has_preposition': 0, 'has_pronoun': 1, 'has_interrog': 0, 'has_conjugation': 0, 'has_qasam': 0, 'is_defined': 0, 'is_inflected': 0, 'tanwin': 0, 'action': 'ناصب', 'object_type': 'اسم', 'need': ''},
 {'word': 'لكن', 'vocalized': 'لَكِنْ', 'type_word': 'حرف', 'class_word': 'حرف استدراك', 'has_conjuction': 1, 'has_definition': 0, 'has_preposition': 0, 'has_pronoun': 1, 'has_interrog': 0, 'has_conjugation': 0, 'has_qasam': 0, 'is_defined': 0, 'is_inflected': 0, 'tanwin': 0, 'action': '', 'object_type': '', 'need': ''},
 {'word': 'لكن', 'vocalized': 'لَكُنَّ', 'type_word': 'ضمير', 'class_word': 'ضمير متصل مجرور', 'has_conjuction': 1, 'has_definition': 0, 'has_preposition': 0, 'has_pronoun': 0, 'has_interrog': 1, 'has_conjugation': 0, 'has_qasam': 0, 'is_defined': 0, 'is_inflected': 0, 'tanwin': 0, 'action': '', 'object_type': '', 'need': ''}
 ]      
        # classified stopwords 
        # ~ lemma = True
        result = stop_tuple1
        word = "لكن"
        self.assertEqual(self.lexicon.get_features_dict(word, lemma=True), result)
        self.assertEqual(self.lexicon.get_feature(word, "voca", lemma=True), [])
        result = ['لَكِنَّ', 'لَكِنْ', 'لَكُنَّ']
        self.assertCountEqual(self.lexicon.get_vocalizeds(word, lemma=True), result)
        result = ['ضمير','حرف']
        self.assertCountEqual(self.lexicon.get_wordtypes(word, lemma=True), result)
        
        result = ['ضمير متصل مجرور', 'حرف استدراك', 'إن و أخواتها'] 
        self.assertCountEqual(self.lexicon.get_wordclass(word), result)
        word = "لَكِنَّ"
        self.assertEqual(self.lexicon.accept_conjuction(word), True)
        self.assertEqual(self.lexicon.accept_definition(word), False)
        self.assertEqual(self.lexicon.accept_preposition(word), False)
        self.assertEqual(self.lexicon.accept_pronoun(word), True)
        self.assertEqual(self.lexicon.accept_interrog(word), False)
        self.assertEqual(self.lexicon.accept_conjugation(word), False)
        self.assertEqual(self.lexicon.accept_qasam(word), False)
        self.assertEqual(self.lexicon.is_defined(word), False)
        self.assertEqual(self.lexicon.accept_inflection(word), False)
        self.assertEqual(self.lexicon.accept_tanwin(word), False)
        self.assertEqual(self.lexicon.get_action(word), "ناصب")
        self.assertEqual(self.lexicon.get_object_type(word), "اسم")
        self.assertEqual(self.lexicon.get_need(word), "")
    
    def test_get_features_forms(self,):
        """Test Extract Features for inflected forms"""
        word = "لكن"
        result = {'vocalized': 'لكن', 'procletic': '', 'tags': 'حرف;إن و أخواتها', 'stem': 'لكن', 'type': 'حرف', 'original': 'لكن', 'encletic': ''}
       
        # ~ self.assertCountEqual(self.lexicon.get_features_dict(word, lemma=False), result)
        self.assertCountEqual(self.lexicon.get_feature(word, "stem", lemma=False), ['لكن'])
        self.assertCountEqual(self.lexicon.get_vocalizeds(word, lemma=False),  ['لكن'])
        self.assertCountEqual(self.lexicon.get_wordtypes(word, lemma=False),  ['حرف', 'ضمير'])        
        result = ['حرف;إن و أخواتها', 'حرف;حرف استدراك', 'ضمير;ضمير متصل مجرور']
        self.assertCountEqual(self.lexicon.get_tags(word), result)
        self.assertEqual(self.lexicon.get_stems(word), ['لكن'])
        self.assertEqual(self.lexicon.get_enclitics(word), [])
        self.assertEqual(self.lexicon.get_procletics(word), [])
        self.assertEqual(self.lexicon.get_lemmas(word), ['لكن'])



if __name__ == '__main__':
    unittest.main()

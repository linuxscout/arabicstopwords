#/usr/bin/python
# -*- coding=utf-8 -*-
"""
Arabic Stop Word, provide tools to manipulate stopwords.
"""

class ArabicStopWords:
    """
    Arabic StopWord Class
    """
    def __init__(self,):
        self.source='list';
        pass;
    def is_stopword(self,word):
        pass;
    def set_source(self,source='list'):
        """
        set the source of stopwords list (database, lsit, file.

        """

        if source=='list':
            pass;
        elif source=='file':
            pass;
        elif source=='database':
            pass;
        self.source=source;
    def load_data(self, source):
        """
        load data from a source (database, list, file.

        """
        pass;
    def get_stopword_list(self):
        """
        return a list of stopwords
        """
        pass;
    def set_stopword_list(self,stopword_list):
        """
        set  a list of stopwords
        """
        pass;
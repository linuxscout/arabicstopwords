#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup

# to install type:
# python setup.py install --root=/
from io import open
def readme():
    with open('README.rst', encoding="utf8") as f:
        return f.read()
setup (name='Arabic_Stopwords', version='0.3',
      description='Arabic Stop words: list and routins',
      long_description = readme(),      
      author='Taha Zerrouki',
      author_email='taha.zerrouki@gmail.com',
      url='http://arabicstopwords.sourceforge.net/',
      license='GPL',
      Description="Arabic Stop words: list and routins",
      package_dir={'arabicstopwords': 'arabicstopwords'},
      packages=['arabicstopwords'],
      install_requires=[ 'pyarabic>=0.6.2',
      ],         
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
    );


#!/usr/bin/python
from setuptools import setup

# to install type:
# python setup.py install --root=/

setup (name='Arabic Stopwords', version='0.2',
      description='Arabic Stop words: list and routins',
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


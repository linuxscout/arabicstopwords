# Arabic Stop words
![ghalatawi logo](doc/arabicStopWordsheader.png "Arabic Stop Words logo")

![PyPI - Downloads](https://img.shields.io/pypi/dm/Arabic-Stopwords)


  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com
    
Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/linuxscout/arabicstopwords/main/AUTHORS.md)
Release  | 0.8
License  |[GPL](https://github.com/linuxscout/arabicstopwords/main/LICENSE)
Tracker  |[linuxscout/arabicstopwords/Issues](https://github.com/linuxscout/arabicstopwords/issues)
Source  |[Github](http://github.com/linuxscout/arabicstopwords)
Website  |[ArabicStopwords on SourceForge](https://arabicstopwords.sf.net)
Doc  |[package Documentaion](https://arabicstopwords.readthedocs.io/)
Download  |[Python Library](https://pypi.python.org/pypi/https://pypi.org/project/Arabic-Stopwords/)
Download  | Data set [CSV/SQL/Python](https://github.com/linuxscout/arabicstopwords/releases/latest)
Feedbacks |[Comments](https://github.com/linuxscout/arabicstopwords/)
Accounts  |[@Twitter](https://twitter.com/linuxscout))


## Citation
If you would cite it in academic work, can you use this citation
```
T. Zerrouki‏, Arabic Stop Words,  https://github.com/linuxscout/arabicstopwords/, 2010
```
Another Citation:
```
Zerrouki, Taha. "Towards An Open Platform For Arabic Language Processing." (2020).
```

or in bibtex format
```bibtex
@misc{zerrouki2010arabicstopwords,
  title={Arabic Stop Words},
  author={Zerrouki, Taha},
  url={https://github.com/linuxscout/arabicstopwords},
  year={2010}
}
@thesis{zerrouki2020towards,
  title={Towards An Open Platform For Arabic Language Processing},
  author={Zerrouki, Taha},
  year={2020}
}


```
## Description

It's not easy to detemine the stop words, and in other hand, stop words differs according to the case,
for this purpos, we propose a  classified list which can be parametered by  developper.

The Word list contains only wonds in its commun forms, and we have generated all forms by a script.

It can used as library 'see section arabicstopwords library'

## Files

* data/ : contains  data of stopwords
* data/classified/stopwords.ods: data in LibreOffice format with more valuble informations, and classified stopwords
* docs: docs files
* scripts: scripts used to generate all forms, and file formats

## Data
This project contains two parts:
- Data part, which contains classified stopwords, or all generated forms, in multiple  format
  - CSV
  - Python
  - SQL / Sqlite
- Python library for handling stopwords.

### Data Structure
Two fromats of data are given:
- classified words (lemma) with features to generate inflected froms
- Generated forms from lemmas with adding affixes.

![Stopwords Example](doc/images/stopwords.png  "Stopwords Example")
    
Minimal classified  data .ODS/CSV file 
- 1st field : unvocalised word ( في)
- 2nd field : type of the word: e.g. حرف
- 3rd field : class of word : e.g. preposition

Affixation infomration in other fields:
-    4th field : AIN in arabic , if word accept Conjuction 'العطف', '*' else
-    5th field : TEH in arabic , if word accept definate article 'ال التعريف', '*' else
-    6th field : JEEM in arabic , if word accept preposition  article 'حروف الجر المتصلة', '*' else      
-    7th field : DAD in arabic , if word accept IDAFA  articles 'الضمائر المتصلة', '*' else              
-    7th field : SAD in arabic , if word accept verb conjugation  articles 'التصريف', '*' else       
-    8th field : LAM in arabic , if word accept LAM QASAM   articles 'لام القسم', '*' else       
-    8th field : MEEM in arabic , if word has ALEF LAM as definition article 'معرف', '*' else        


All forms data CSV file
- 1st field : unvocalised word ( بأنك)
- 2nd field : vocalised inflected word with : e.g. ف-ب-خمسين-ي
- 3rd field:  word type (super class): noun, verb, tool حرف
- 4th field:  word type (sub class): إنّ وأخواتها 
- 5th field:  original or lemma: إن
- 6th field:  procletic : ب
- 7th field:  stem : أن
- 8th field:  encletic: ك
- 9th field:  tags: جر:مضاف



```csv
word	vocalized	type	category	original	procletic	stem	encletic	tags
بأنك	بِأَنّكَ	حرف	إن و أخواتها	أن	ب-		-ك	جر:مضاف
بأنكما	بِأَنّكُمَا	حرف	إن و أخواتها	أن	ب-		-كما	جر:مضاف
```
## How to customize stop word list

* check the minimal form data file (stopwords.csv)
* comment by "#" all words which you don't need
* run 
```
make
```
* catch the output of script in releases folder.


## How to update data

* check if the word doesn't exist in the minimal form data file ( classified/stopwords.ods)
* add affixation information
* run 
```
make
```
* catch the output of script in releases folder.

## Arabic Stopwords Library
### install
``` shell
pip install arabicstopwords
```
### usage
* test if a word is stop
``` python
>>> import arabicstopwords.arabicstopwords as stp
>>> # test if a word is a stop
... stp.is_stop(u'ممكن')
False
>>> stp.is_stop(u'منكم')
True
```

* stem a stopword
```python
>>> word = u"لعلهم"
>>> stp.stop_stem(word)
u'لعل'

```
* list all stop words
```
>>> stp.stopwords_list()
......
>>> len(stp.stopwords_list())
13629
>>> len(stp.classed_stopwords_list())
 507
```
* give all forms of a stopword
```python
>>> stp.stopword_forms(u"على")
....
>>> len(stp.stopword_forms(u"على"))
144
```

 
* get stopword as list of dictionaries
``` python
>>> from arabicstopwords.stopwords_lexicon import stopwords_lexicon 
>>> lexicon = stopwords_lexicon()
>>> # test if a word is a stop
... lexicon.is_stop(u'ممكن')
False
>>> lexicon.is_stop(u'منكم')
True
>>> lexicon.get_features_dict(u'منكم')
[{'vocalized': 'منكم', 'procletic': '', 'tags': 'حرف;حرف جر;ضمير', 'stem': 'من', 'type': 'حرف', 'original': 'من', 'encletic': '-كم'}]
```

* get stopword as tuple
``` python
>>> from arabicstopwords.stopwords_lexicon import stopwords_lexicon 
>>> lexicon = stopwords_lexicon()
>>> tuples = lexicon.get_stopwordtuples(u'منكم')
>>> tuples
[<stopwordtuple.stopwordTuple object at 0x7fd93b3d12b0>]
>>> for tup in tuples:
...     print(tup)
... 
{'vocalized': 'منكم', 'procletic': '', 'tags': 'حرف;حرف جر;ضمير', 'stem': 'من', 'type': 'حرف', 'original': 'من', 'encletic': '-كم'}
>>> >>> for tup in tuples:
...     dir(tup)
... 
['accept_conjuction', 'accept_conjugation', 'accept_definition', 'accept_inflection', 'accept_interrog', 'accept_preposition', 'accept_pronoun', 'accept_qasam', 'accept_tanwin', 'get_action', 'get_enclitic', 'get_feature', 'get_features_dict', 'get_lemma', 'get_need', 'get_object_type', 'get_procletic', 'get_stem', 'get_tags', 'get_vocalized', 'get_wordclass', 'get_wordtype', 'is_defined', 'stop_dict']
>>> 
```

* get stopword by categories
``` python
>>> from arabicstopwords.stopwords_lexicon import stopwords_lexicon 
>>> lexicon = stopwords_lexicon()
>>> lexicon.get_categories()
['حرف', 'ضمير', 'فعل', 'اسم', 'اسم فعل', 'حرف ابجدي']
>>> lexicon.get_by_category("اسم فعل", lemma=True, vocalized=True)
['آهاً', 'بَسّْ', 'بَسْ', 'حَايْ', 'صَهْ', 'صَهٍ', 'طَاقْ', 'طَقْ', 'عَدَسْ', 'كِخْ', 'نَخْ', 'هَجْ', 'وَا', 'وَا', 'وَاهاً', 'وَيْ', 'آمِينَ', 'آهٍ', 'أُفٍّ', 'أُفٍّ', 'أَمَامَكَ', 'أَوَّهْ', 'إِلَيْكَ', 'إِلَيْكُمْ', 'إِلَيْكُمَا', 'إِلَيْكُنَّ', 'إيهِ', 'بخٍ', 'بُطْآنَ', 'بَلْهَ', 'حَذَارِ', 'حَيَّ', 'دُونَكَ', 'رُوَيْدَكَ', 'سُرْعَانَ', 'شَتَّانَ', 'عَلَيْكَ', 'مَكَانَكَ', 'مَكَانَكِ', 'مَكَانَكُمْ', 'مَكَانَكُمَا', 'مَكَانَكُنَّ', 'مَهْ', 'هَا', 'هَاؤُمُ', 'هَاكَ', 'هَلُمَّ', 'هَيَّا', 'هِيتَ', 'هَيْهَاتَ', 'وَرَاءَكَ', 'وَرَاءَكِ', 'وُشْكَانَ', 'وَيْكَأَنَّ', 'وَرَاءَكُما', 'وَرَاءَكُمْ', 'وَرَاءَكُنَّ', 'بِئْسَمَا']
```

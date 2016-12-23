#Arabic Stop words

##Description


- This  list can be reused, 
It't not easy to detemine the stop words, and in other hand, stop words differs according to the case,
for this purpos, we propose a  classified list
which can be parametered by  developper 
The Word list contains only wonds in its commun forms,
and we have generated all forms by a script.


##Files
-------
* data/ : contains  data of stopwords

* data/classified/stopwords.cvs: the data file as csv

* data/classified/stopwords.xls: data in Excel fomat with more valuble informations, and classified stopwords

* data/allforms/stopwordsallforms.sql: all forms database in sql format 

* data/allforms/stopwords_allforms.txt: data generated from minimal data file
* data/allforms/stopwordsallforms.py: all forms data as python dictionary 
* tools/: scripts used to generate all forms from minimal data 

        usage : 
        generate_stopwords_forms.py -f data/stopwords.cvs  > output_file.txt
        Note: to avoid program to treat some data, comment lines by #, in the data file
        Note: script can be custumed

Data Structure
--------------
All forms data .CSV file 
- 1st field : unvocalised word ( ›Ì)
- 2nd field : unvocalised stemmed word with -'-' between affixes: e.g. ›-»-Œ„”Ì‰-Ì

    
- Minimal classified  data .CSV file 
- 1st field : unvocalised word ( ›Ì)
- 2nd field : type of the word: e.g. Õ—›
- 3rd field : class of word : e.g. preposition 
- Affixation infomration in other fields:
-    4th field : AIN in arabic , if word accept Conjuction '«·⁄ÿ›', '*' else
-    5th field : TEH in arabic , if word accept definate article '«· «· ⁄—Ì›', '*' else
-    6th field : JEEM in arabic , if word accept preposition  article 'Õ—Ê› «·Ã— «·„ ’·…', '*' else      
-    7th field : DAD in arabic , if word accept IDAFA  articles '«·÷„«∆— «·„ ’·…', '*' else              
-    7th field : SAD in arabic , if word accept verb conjugation  articles '«· ’—Ì›', '*' else       
-    8th field : LAM in arabic , if word accept LAM QASAM   articles '·«„ «·ﬁ”„', '*' else       
-    8th field : MEEM in arabic , if word has ALEF LAM as definition article '„⁄—›', '*' else        

How to custum stop word list
---------------
* check the minimal form data file ( stopwords.csv)
* comment by "#" all words which you don't need
* run generate_stopwords_forms.py script
* catch the output of script.

Generation script usage:
------------------------
```
Usage: generate_stopwords_forms -f filename [OPTIONS]
    [-h | --help]       outputs this usage message
    [-V | --version]    program version
    [-f | --file= filename] input file to generate_stopwords_forms
    [-o | --out= output format] output format(csv,python,sql)
```

How to add a word into  word list
---------------
* check if the word doesn't exist in the minimal form data file ( stopwords.csv)
* add affixation information
* run generate_stopwords_forms.py script
* catch the output of script.

Thanks
 

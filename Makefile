#/usr/bin/sh
# Build Arabic stop word list files
DATA_DIR :=data/classified
RELEASES :=releases
BUILD :=$(RELEASES)/build
OUTPUT :=tests/output
SCRIPT :=scripts
VERSION=0.9
DOC="."
DATE=$(shell date +'%y.%m.%d-%H:%M')
FORMAT:=csv
default: all
# Clean build files
clean:
	rm -f -r $(RELEASES)/*
backup: 
	mkdir -p $(RELEASES)/backup$(VERSION)
	#~ mv $(RELEASES)/*.bz2 $(RELEASES)/backup$(VERSION)
#create all files 
all: ods release


# Publish to github
publish:
	git push origin master 

ods: 
	#Generate csv files from ODS
	libreoffice --headless --convert-to "csv:Text - txt - csv (StarCalc):9,34,UTF8" --outdir $(OUTPUT)/ $(DATA_DIR)/stopwords.ods

#Package files
release: backup format pack


format:py sql csv

py: FORMAT:=py
sql: FORMAT:=sql
csv: FORMAT:=csv

py sql csv:
	#Generate Specific format CSV SQL and python
	echo " Generate ${FORMAT} version"
	# all forms
	python3 $(SCRIPT)/generate_stopwords_format.py -v $(VERSION) -a -f $(OUTPUT)/stopwords.csv -o ${FORMAT}    >$(OUTPUT)/stopwordsallforms.${FORMAT}
	# classified
	python3 $(SCRIPT)/generate_stopwords_format.py -v $(VERSION) -f $(OUTPUT)/stopwords.csv -o ${FORMAT}    > $(OUTPUT)/stopwords_classified.${FORMAT}


#packaging 

pack:
	#doc
	mkdir -p $(BUILD)	
	cp -f $(DOC)/README.md $(BUILD)
	cp -f $(DOC)/LICENSE $(BUILD)
	cp -f $(DOC)/AUTHORS $(BUILD)
	echo $(VERSION) >$(BUILD)/VERSION
	#~ #classified
	#~ mkdir -p $(BUILD)/classified
	#~ cp -f $(OUTPUT)/stopwords.csv $(BUILD)/classified/
	#python
	mkdir -p $(BUILD)/python/stopwords
	cp $(OUTPUT)/stopwordsallforms.py $(BUILD)/python/stopwords
	cp $(OUTPUT)/stopwords_classified.py $(BUILD)/python/stopwords
	cp $(OUTPUT)/stopwordsallforms.py python_lib/arabicstopwords
	cp $(OUTPUT)/stopwords_classified.py python_lib/arabicstopwords
	# sql
	mkdir -p $(BUILD)/sql
	cp -f $(OUTPUT)/stopwordsallforms.sql $(BUILD)/sql/
	cp -f $(OUTPUT)/stopwords_classified.sql $(BUILD)/sql/
	# csv
	mkdir -p $(BUILD)/csv
	cp -f $(OUTPUT)/stopwordsallforms.csv $(BUILD)/csv/
	cp -f $(OUTPUT)/stopwords_classified.csv $(BUILD)/csv/
	# corpus
	mkdir -p $(BUILD)/corpus
	cp -f $(OUTPUT)/tashkeela_stopwords_frequency.csv $(BUILD)/corpus/
	cp -f $(OUTPUT)/wiki_stopwords_frequency.csv $(BUILD)/corpus/
	#zip
	cd $(BUILD) && tar cfj arabicstopwords.$(VERSION).tar.bz2 * 
	mv $(BUILD)/arabicstopwords.$(VERSION).tar.bz2 $(RELEASES)/
	# latest
	cp $(BUILD)/* -r  $(RELEASES)/latest/
	# add files to leatest release

sqlite:
	mkdir -p $(BUILD)/sqlite
	sqlite3 $(BUILD)/sqlite/database.sqlite < $(OUTPUT)/stopwordsallforms.sql
	sqlite3 $(BUILD)/sqlite/database.sqlite < $(OUTPUT)/stopwords_classified.sql
	# create indexes
	sqlite3 $(BUILD)/sqlite/database.sqlite "CREATE INDEX idx_voc ON stopwords (unvocalized);"
	sqlite3 $(BUILD)/sqlite/database.sqlite  "CREATE INDEX idx_voc_class ON classedstopwords (word);"

wheel:
	cd python_lib;sudo python3 setup.py bdist_wheel
install:
	cd python_lib;sudo python3 setup.py install
sdist:
	cd python_lib;sudo python3 setup.py sdist
upload:
	echo "use twine upload dist/arabicstopwords-0.6-py2-none-any.whl"

test:
	cd python_lib;python3 -m unittest discover tests
md2html:
	pandoc -s -r markdown -w html README.md -o README.html
md2rst:
	pandoc -s -r markdown -w rst README.md -o python_lib/README.rst
build: wheel wheel3 install install3 sdist


wiki:CORPUS_INPUT= samples/wiki_wordsfreq.txt
wiki:CORPUS_OUTPUT= tests/output/wiki_stopwords_frequency.csv
wiki:CORPUS_VERSION= 01-Feb-2023
wiki:CORPUS_NAME=Arabic Wikippedia
wiki:CORPUS_COMMENT=useful for Standard Modern Arabic
tashkeela:CORPUS_INPUT= samples/tashkeela_unvocalized_freq.txt
tashkeela:CORPUS_OUTPUT= tests/output/tashkeela_stopwords_frequency.csv
tashkeela:CORPUS_VERSION= 1.0
tashkeela:CORPUS_NAME=Tashkeela
tashkeela:CORPUS_COMMENT=useful for Classical Arabic
tashkeela wiki:
	# extract  frequent stopwords from Tahskeela Corpus
	echo "##*************************************"> $(CORPUS_OUTPUT)
	echo "#Arabic Stop word list for morphology analysis and information retrival">> $(CORPUS_OUTPUT)
	echo "#  Most frequent stopwords in $(CORPUS_NAME) Corpus, $(CORPUS_COMMENT)">> $(CORPUS_OUTPUT)
	echo "#Corpus Version $(CORPUS_VERSION): ">> $(CORPUS_OUTPUT)
	echo "#Version        : $(VERSION)">> $(CORPUS_OUTPUT)
	echo "#Generated at   : $(DATE) ">> $(CORPUS_OUTPUT)
	echo "#Author         : Taha Zerrouki "   >> $(CORPUS_OUTPUT)
	echo "#Web            : http://arabicstopwords.sf.net">> $(CORPUS_OUTPUT)
	echo "#Source         : http://github.com/linuxscout/arabicstopwords">> $(CORPUS_OUTPUT)
	echo "#*************************************">> $(CORPUS_OUTPUT)
	cd tests;python3 corpus_stopword_frequency.py -f $(CORPUS_INPUT) >> ../$(CORPUS_OUTPUT)

swap:
	awk ' { t = $1; $1 = $2; $2 = t; print; } ' tests/samples/wiki_wordsfreq.txt > wiki_wordsfreq.inv.txt
corpus: wiki tashkeela
	cp -f $(OUTPUT)/stopwords_classified.sql $(BUILD)/sql/

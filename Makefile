#/usr/bin/sh
# Build Arabic stop word list files
DATA_DIR :=data/classified
RELEASES :=releases
BUILD :=$(RELEASES)/build
OUTPUT :=tests/output
SCRIPT :=scripts
VERSION=0.9
DOC="."
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
	#zip
	cd $(BUILD) && tar cfj arabicstopwords.$(VERSION).tar.bz2 * 
	mv $(BUILD)/arabicstopwords.$(VERSION).tar.bz2 $(RELEASES)/

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

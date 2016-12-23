#/usr/bin/sh
# Build Arabic stop word list files
DATA_DIR :=data/classified
RELEASES :=releases
BUILD :=$(RELEASES)/build
OUTPUT :=tests/output
SCRIPT :=scripts
VERSION=0.3
DOC="."

default: all
# Clean build files
clean:
	rm -f -r $(RELEASES)/*
backup: 
	mkdir -p $(RELEASES)/backup$(VERSION)
	mv $(RELEASES)/*.bz2 $(RELEASES)/backup$(VERSION)
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


format:
	#Generate Specific format SQL and XML
	python $(SCRIPT)/generate_stopwords_format.py -A -f $(OUTPUT)/stopword.csv           > $(OUTPUT)/stopwordsallforms.csv 
	python $(SCRIPT)/generate_stopwords_format.py -A -f $(OUTPUT)/stopword.csv -o python >$(OUTPUT)/stopwordsallforms.py
	python $(SCRIPT)/generate_stopwords_format.py -A -f $(OUTPUT)/stopword.csv -o sql    >$(OUTPUT)/stopwordsallforms.sql

#packaging 

pack:
	#doc
	mkdir -p $(BUILD)	
	cp $(DOC)/README.md $(BUILD)
	cp $(DOC)/LICENSE $(BUILD)
	cp $(DOC)/AUTHORS $(BUILD)
	#classified
	mkdir -p $(BUILD)/classified
	cp  $(OUTPUT)/stopwords.csv $(BUILD)/classified/
	#python
	mkdir -p $(BUILD)/python/stopwords
	cp $(OUTPUT)/stopwordsallforms.py $(BUILD)/python/stopwords
	# sql
	mkdir -p $(BUILD)/sql
	cp $(OUTPUT)/stopwordsallforms.sql $(BUILD)/sql/
	# csv
	mkdir -p $(BUILD)/csv
	cp $(OUTPUT)/stopwordsallforms.csv $(BUILD)/csv/
	#zip
	cd $(BUILD) && tar cfj arabicstopwords.$(VERSION).tar.bz2 * 
	mv $(BUILD)/arabicstopwords.$(VERSION).tar.bz2 $(RELEASES)/


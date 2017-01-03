# -*- coding: utf-8 -*-

import wikitools
#import poster
import os
import sys

wiki_url =  "http://noolaham.org/wiki/api.php"



pagename = "இங்கிலாந்தின்_வரலாறு_1"
wiki = wikitools.wiki.Wiki(wiki_url)

page = wikitools.Page(wiki,  pagename , followRedir=True)

#print page.getWikiText()

template =  page.getWikiText().split("==")[0]



for i in template.split("\n"):
	if "=" in i:
		key = i.split("=")[0].strip()
		value = i.split("=")[1].strip()
		if value[-1] == "|" :
			value = value[:-1] 

		print key.decode('utf-8') + " = " + value.decode('utf-8')


contents = page.getWikiText().split("Contents}}==")[1].split("[[")[0].strip()

print "\n\nTable of Contents = "
print contents

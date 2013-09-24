import textwrap
from nltk.corpus import wordnet as wn
import nltk
import sys

def compressWord(word):
	leng = sys.maxsize
	sword = ""
	for i, syn in enumerate(wn.synsets(word, None)):
		syns = [n.replace('_', ' ') for n in syn.lemma_names]
		for s in syns:
			if len(s) < leng:
				sword = s
				leng = len(sword)
		return sword

def compressFile(filename):
	out = open(filename).read() 
	output = ""

	words = nltk.tokenize.RegexpTokenizer("(?:[A-Z][.])+|\d[\d,.:\-/\d]*\d|\w+[\w\-\'.&|@:/]*\w+|\s|.|,|'|\"", False).tokenize(out)
	for w in words:
		c = compressWord(w)
		if c == None:
			output += w
		else: 
			output += c

	return (output)


print (compressFile("pg11.txt"))

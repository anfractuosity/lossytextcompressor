#!/usr/bin/python3

import textwrap
from nltk.corpus import wordnet as wn
import nltk
import sys


def compressWord(word):
  leng = len(word)
  sword = word
  synsets = wn.synsets(word)

  for i, syn in enumerate(synsets):
    syns = [n.name().replace('_', ' ') for n in syn.lemmas()]

    if not syns[0] in [word, wn.morphy(word)]:
      continue

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
		if w:
				c = compressWord(w)
				if c == None:
					output += w
				else: 
					output += c

	return (output)


print (compressFile("pg11.txt"))

#!/usr/bin/python3

import argparse
import textwrap
from nltk.corpus import wordnet as wn
import nltk
import sys


def compressWord(word):
  leng = len(word)
  sword = word
  synsets = wn.synsets(word)

  for syn in synsets:
    syns = [n.name().replace('_', ' ') for n in syn.lemmas()]

    if not syns[0] in [word, wn.morphy(word)]:
      continue

    for s in syns:
      if len(s) < leng:
        sword = s
        leng = len(sword)

  return sword

def compressFile(filename):
  text = open(filename).read() 
  output = ""

  words = nltk.tokenize.RegexpTokenizer("(?:[A-Z][.])+|\d[\d,.:\-/\d]*\d|\w+[\w\-\'.&|@:/]*\w+|\s|.|,|'|\"", False).tokenize(text)
  for w in words:
    c = compressWord(w)
    output += c

  return output


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='A lossy compression system for English Text')
  parser.add_argument('file', help='The path to a file to compress')
  args = parser.parse_args()

  print(compressFile(args.file))

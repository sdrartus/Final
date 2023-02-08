import re as r
import nltk, pprint
from nltk import word_tokenize

euph = "C:/Users/Sir/Desktop/Final/Final/euphemism.csv"
profane = "C:/Users/Sir/Desktop/Final/Final/bad-words.txt"
euph_infile = open (euph, 'r')
prof_infile = open(profane, 'r')
elines = euph_infile.read()
plines = prof_infile.read()

tokens = word_tokenize(plines)

print(len(tokens))

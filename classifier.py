from util import *
from parser import languages
import pickle
## This takes in a document string and returns the language
## We take the
def setup():
	global charset
	global stopwords
	with open('charset.pkl', 'rb') as handle:
		charset = pickle.load(handle)
	with open('stopwords.pkl','rb') as h2:
		stopwords = pickle.load(h2)


def classifier(string):
	string = preprocess(string)
	wordlist = string.split()
	maximum = 0
	language = ""
	currlanguages = []
	chars = set(string)
	for lang in languages:
		if chars.issubset(charset[lang]):
			currlanguages.append(lang)
	for lang in currlanguages:
		nostopwords = 0
		for stopword in stopwords[lang]:
			if stopword in wordlist:
				nostopwords = nostopwords + 1
		if (maximum < nostopwords):
			maximum = nostopwords
			language = lang
	if (maximum == 0):
		return "language not supported currently"
	return language


        
from glob import glob
from codecs import open, BOM_UTF8
from util import *
import pickle
import pandas as pd

#maxstopwords per language

languages = ["en","fr","esp","ger"]
stopwords = {}
char_set  = {}

##SPANISH
spanish_sent = []

for f in glob("spanishText_10000_15000"):
        for line in open(f, encoding="latin-1"):
            if line == "\n" or line.startswith(("<doc", "</doc>", "ENDOFARTICLE", "REDIRECT"," Acontecimientos"," Fallecimientos"," Nacimientos")):
            	continue
            spanish_sent.append(line)

counter,a,b = corpora_lang(spanish_sent)
char_set["esp"] = character_set(spanish_sent)
stopwords["esp"] = [pair[0] for pair in counter.most_common(15)]



##ENGLISH AND FRENCH

english_sent = []
french_sent  = []

f = open("eng-fra.txt","r")
for line in f.readlines():
    temp = line.split("\t")
    french_sent.append(temp[1])
    english_sent.append(temp[0])

counter,a,b = corpora_lang(english_sent)
char_set["en"] = character_set(english_sent)
stopwords["en"] = [pair[0] for pair in counter.most_common(15)]

counter,a,b = corpora_lang(french_sent)
char_set["fr"] = character_set(french_sent)
stopwords["fr"] = [pair[0] for pair in counter.most_common(15)]

f1 = open("stopwords.pkl","wb")
f2 = open("charset.pkl","wb")

pickle.dump(char_set,f2)
pickle.dump(stopwords,f1)

f1.close()
f2.close()


##GERMAN

df = pd.read_json("recipes.json")
instruct_text = list(df["Instructions"])

counter,a,b = corpora_lang(instruct_text)
char_set["ger"] = character_set(instruct_text)
stopwords["ger"] = [pair[0] for pair in counter.most_common(15)]




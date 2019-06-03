import numpy as np
import pandas as pd
from collections import Counter
import re

def preprocess(sent):
    sent = re.sub(r'[^\w\s]','',sent.lower())
    sent = re.sub(r'[0-9]','',sent)
    return sent

def corpora_lang(language_dataset):
    listofwrds = []
    for sent in language_dataset:
        sent = preprocess(sent)
        sent = sent.split()
        listofwrds.extend(sent)
    setofwrds = set(listofwrds)
    return Counter(listofwrds),len(setofwrds), len(listofwrds)

def character_set(language_dataset):
    char_set = set()
    for sent in language_dataset:
        sent = preprocess(sent)
        char_set = char_set.union(set(sent))
    return char_set



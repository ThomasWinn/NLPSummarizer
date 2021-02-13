# to check
import gensim
from gensim.summarization import summarize

import nltk
nltk.download('stopwords')
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

import re

#source
# https://www.nytimes.com/2014/06/22/magazine/the-slumdog-millionaire-architect.html?src=me&_r=0

# Get raw text

# Given a story stored in article.txt, split the article into sentences given the punctuation [?, !, .]
# tokenize the sentences then tokenize the words in those sentences.
def form_sentence():

    f = open('article.txt', 'r', encoding='UTF-8')
    article = f.read()
    f.close()

    art_split  = re.split('[!?.]', article) # split amongst only periods
    art_split.pop()
    
    sentences = []
    for i in art_split:
        sentences.append(i.replace('[^a-zA-Z]', ' ').split(' '))
    
    for i in range(len(sentences)):
        if i == 0:
            continue
        sentences[i].pop(0)

    return sentences

def sentence_corr ():
    pass
# lemmatization is better at finding the base word rather than stemming

if __name__ == "__main__":
    s = form_sentence()

# summary = summarize(article)
# print(summary)


# clean the text
# There are words like what's whats what all counting as different words
# https://www.geeksforgeeks.org/removing-stop-words-nltk-python/ clean text using nltk

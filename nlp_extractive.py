# to check
import gensim
from gensim.summarization import summarize

#source
# https://www.nytimes.com/2014/06/22/magazine/the-slumdog-millionaire-architect.html?src=me&_r=0

f = open('article.txt', 'r', encoding='UTF-8')
article = f.read()

summary = summarize(article)
print(summary)


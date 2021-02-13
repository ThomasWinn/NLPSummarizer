# to check
import gensim
from gensim.summarization import summarize
import nltk
nltk.download('punkt')

#source
# https://www.nytimes.com/2014/06/22/magazine/the-slumdog-millionaire-architect.html?src=me&_r=0

# Get raw text
f = open('article.txt', 'r', encoding='UTF-8')
article = f.read()
f.close()

#tokenize sentences
print(nltk.sent_tokenize(article))



# summary = summarize(article)
# print(summary)


# clean the text
# There are words like what's whats what all counting as different words
# https://www.geeksforgeeks.org/removing-stop-words-nltk-python/ clean text using nltk

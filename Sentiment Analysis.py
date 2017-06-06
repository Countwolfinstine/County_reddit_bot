import nltk
from nltk.tokenize import word_tokenize

sentiment_dictonary = {}
for line in open('AFINN-111.txt'):
	word, score = line.split('\t')
	sentiment_dictonary[word]= int (score)

words = word_tokenize('This is a good book'.lower()) 

print(words)
print(sum( sentiment_dictonary.get(word,0) for word in words))
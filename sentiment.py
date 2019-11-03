from textblob import TextBlob
import nltk
from newspaper import Article

url = 'https://everythingcomputerscience.com/'
article = Article(url)

article.download() #Downloads the link’s HTML content
article.parse() #Parse the article
nltk.download('punkt')#1 time download of the sentence tokenizer
article.nlp()#  Keyword extraction wrapper

text = article.summary
print(text)

obj = TextBlob(text)
#returns the sentiment of text
#by returning a value between -1.0 and 1.0
sentiment = obj.sentiment.polarity
print(sentiment)

if sentiment == 0:
  print('The text is neutral')
elif sentiment > 0:
  print('The text is positive')
else:
  print('The text is negative')
  
import bs4 as bs  
import urllib.request  
import re
import nltk
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from summa import summarizer
from summa import keywords

url_topull = input('Enter the Wikipedia URL to pull - ')

scraped_data = urllib.request.urlopen(url_topull)  
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:  
    article_text += p.text

print("Data pull done")

print("==================================SUMMARY===================================")
print (summarizer.summarize(article_text,ratio=0.1))

print("==================================KEYWORDS===================================")

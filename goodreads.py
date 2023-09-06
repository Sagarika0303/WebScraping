import csv
import random
from bs4 import BeautifulSoup
import requests
html = requests.get("https://www.goodreads.com/quotes")
soup = BeautifulSoup(html.text,'html.parser')
quotes = soup.find("div",class_="quotes")
#print(quotes.text)
quote_list = quotes.find_all("div",class_="quote")
for quote in quote_list:
    d = quote.find("div",class_ = "quoteText")
    print(d.text.strip())

csv_try = open('test.csv',"w")
writer = csv.writer(csv_try)
writer.writerow(('Sl Number','Author'))
for i in range(10):
    writer.writerow((i+1,random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)))
csv_try.close()
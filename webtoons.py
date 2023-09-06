from bs4 import BeautifulSoup
import requests
html = requests.get("https://www.webtoons.com/en/")
soup = BeautifulSoup(html.text,'html.parser')
section = soup.find("div",class_="eg-flick-viewport")
#print(quotes.text)
titles = section.find_all("h3")
print(titles.text)
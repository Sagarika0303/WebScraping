#### This program scrapes naukri.com's page and gives our result as a
#### list of all the job_profiles which are currently present there.

import xlwt
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#url of the page we want to scrape
url = "https://www.naukri.com/engineering-jobs?src=discovery_trendingWdgt_homepage_srch"

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(5)

html = driver.page_source

# this renders the JS code and stores all
# of the information in static HTML code.

# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find('div', class_="list")
job_profiles = all_divs.find_all('a', class_="title fw500 ellipsis")
company = all_divs.find_all('a', class_="subTitle ellipsis fleft")
experience = all_divs.find_all('span', class_="ellipsis fleft fs12 lh16 expwdth")

# printing top ten job profiles
count = 0
title=[]
companyname=[]
exp=[]
for i in job_profiles :
	title.append(i.text)
	count = count + 1
	if(count == 20) :
		break

for i in company :
	companyname.append(i.text)
	count = count + 1
	if(count == 10) :
		break

for i in experience :
	exp.append(i.text)
	count = count + 1
	if(count == 10) :
		break

#print(len(title))	
#print(len(companyname))
#print(len(exp))

data={'title':title,'companyname':companyname,'exp':exp}
df=pd.DataFrame(data)
df.to_excel("naukri.xls")

#data=[title,companyname,exp]
#print(data)
#df=pd.DataFrame(data, columns=['tit','compan','exp'])
print(df)
#df=pandas.DataFrame(data,columns=[])
#print(data)
#print(title)    
#print(companyname)
#print(exp)



driver.close() # closing the webdriver

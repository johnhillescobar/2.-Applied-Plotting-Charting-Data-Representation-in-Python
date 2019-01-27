from bs4 import BeautifulSoup
import requests
import pandas as pd



URL = 'https://en.wikipedia.org/wiki/List_of_Chicago_Bulls_seasons'
#URL = 'https://en.wikipedia.org/wiki/List_of_largest_manufacturing_companies_by_revenue'

"""
content = requests.get(URL).content
soup = BeautifulSoup(content, 'lxml')

tags = soup.findAll('div', {'class': 'toc'})
tag = soup.find('div', {'class': 'toc'})

links = tag.findAll('a')

#print(links)

for link in links:
    print(link.text)
"""

content = requests.get(URL).content
soup = BeautifulSoup(content, 'lxml')
table = soup.findAll('table', {'class': "wikitable plainrowheaders"})

#"wikitable plainrowheaders"

print(table)

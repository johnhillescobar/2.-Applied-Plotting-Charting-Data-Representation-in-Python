import sys

import bs4 as bs
import urllib.request
import pandas as pd


##URL = 'https://en.wikipedia.org/wiki/List_of_Chicago_Bulls_seasons'
##
##sauce = urllib.request.urlopen(URL).read()
##soup = bs.BeautifulSoup(sauce, 'lxml')
##
###table = soup.table
##table = soup.find('table')
##
##table_rows = table.find_all('tr')
##
##for tr in table_rows:
##    td = tr.find_all('td')
##    row = [i.text for i in td]
##    print(row)


#print(table)


##dfs = pd.read_html('https://en.wikipedia.org/wiki/List_of_Chicago_Bulls_seasons'#, header = 0
##                   )
##for df in dfs:
##    print(df)

##URL = 'https://en.wikipedia.org/wiki/sitemap.xml'
##
##sauce = urllib.request.urlopen(URL).read()
##soup = bs.BeautifulSoup(sauce, 'xml')
##print(soup)


""" DYNAMIC DATA"""
#URL = 'https://en.wikipedia.org/wiki/List_of_Chicago_Bulls_seasons'
URL ='https://pythonprogramming.net/parsememcparseface/'

sauce = urllib.request.urlopen(URL).read()
soup = bs.BeautifulSoup(sauce, 'lxml')
js_test = soup.find('p', class_ = 'jstest')
print(js_test.text)
























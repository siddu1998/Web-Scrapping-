import bs4 as bs
import urllib.request
import pandas as pd


sauce=urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup=bs.BeautifulSoup(sauce,'lxml')
table=soup.find('table')

table_rows=table.find_all('tr')
#here u will get it in the form row1-->[cloumn1, column2, column3......]
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text for i in td]
    print(row)

#dfs data frames this is panda way of reading it...read_html since we are reading html
dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/')
for df in dfs:
     print(df)


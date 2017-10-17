import bs4 as bs
import urllib.request

sauce=urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup=bs.BeautifulSoup(sauce,'lxml')

#this gives all the urls
for url in soup.find_all('a'):
    print(url.get('href'))

#suppose u want only url only in nav!
#then use below
nav=soup.nav
for url in nav.find_all('a'):
    print(url.get('href'))

#paras in body
body=soup.body
for para in body.find_all('p'):
    print(para.text)

# to get all text in all divs which is under the body tag
for div in soup.find_all('div',class_='body'):
       print(div.text)

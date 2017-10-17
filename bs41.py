import bs4 as bs
import urllib.request

sauce=urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup=bs.BeautifulSoup(sauce,'lxml')

#to get title in the form of string
#print(soup.title.string)
#to get all paragaphs on page
#print(soup.find_all('p'))
#parse all paras and print the text...diff btw text and string..
#in para string will show none if u have child text
#in text u get the whole shit

#for para in soup.find_all('p'):
#    print(para.text)


#syntax soup.find_all('tags u need t find')
#incase u need to get link use

for url in soup.find_all('a'):
    print(url.get('href'))


# u use .get_text to get the whole text just incase site does not use
#paras but use span then u  can get text by using get_text
#print(soup.get_text())
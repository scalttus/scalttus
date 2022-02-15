import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

print('Erster Webscraper)')

# https://www.youtube.com/watch?v=-u4GyvpQZBU

baseURL = 'https://shop.ermuri.com/'
URL = baseURL + '/html/de/search.html?grp=all&searchStr=Scheibel+Jubil%E4umsedition&gid=shop90'

print('Scrapen von: ' + URL )

session1 = HTMLSession()
page1 = session1.get(URL)
page1.html.render()
sout1 = BeautyfulSoup(page1.html.html, 'html.parser')
print(soup1.find_all(id='produktoverlay0'))
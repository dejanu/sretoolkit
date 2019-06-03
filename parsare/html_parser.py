import re
from bs4 import BeautifulSoup, SoupStrainer
import html 

with open("page1.html", 'r') as htmlb:
    soup2 = BeautifulSoup(htmlb, 'lxml')


# find all urls from page1.html and write them in page2.html
with open("page2.html", 'w') as h:
    for link in soup2.find_all('a'):
        h.write("<a href=\"{}\">{}</a><br>".format(link.get('href'),link.get('href')))    





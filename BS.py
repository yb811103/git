__author__ = 'yubin'
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("index.html"))
for i in soup.find_all('a'):
    print i.get_text()
    print i.get("href")



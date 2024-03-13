import requests
from bs4 import BeautifulSoup

r = requests.get('http://books.toscrape.com/index.html')
soup = BeautifulSoup(r.text, features="html.parser")
print(soup.text)
print(BeautifulSoup)
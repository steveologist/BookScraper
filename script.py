import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# content_inner > article > div.row > div.col-sm-6.product_main > p.price_color
# content_inner > article > p
price_elements = soup.select("p.price_color")

for price_element in price_elements:
    price = price_element.get_text()


print(price)

import requests
from bs4 import BeautifulSoup


url = "http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html" # noqa


response = requests.get(url)


soup = BeautifulSoup(response.text, "html.parser")


book_title = soup.select_one("div.col-sm-6.product_main > h1").text.strip()
product_page_url = url
upc = soup.select_one("tr:nth-child(1) > td").text.strip() # noqa
p_inc_tax = soup.select_one("tr:nth-of-type(4) > td").text.strip()
p_exc_tax = soup.select_one("tr:nth-of-type(3) > td").text.strip()
quantity_available = soup.select_one("tr:nth-of-type(6) > td").text.strip()
product_description = soup.select_one("article.product_page > p").text.strip()
category = soup.select("ul.breadcrumb > li")[2].text.strip()
review_rating = soup.select_one("p.star-rating")['class'][1]
image_url = soup.select_one("div.item.active > img")['src']


print("Book Title:", book_title)
print("Product Page URL:", product_page_url)
print("Universal Product Code (UPC):", upc)
print("Price Including Tax:", p_inc_tax)
print("Price Excluding Tax:", p_exc_tax)
print("Quantity Available:", quantity_available)
print("Product Description:", product_description)
print("Category:", category)
print("Review Rating:", review_rating)
print("Image URL:", image_url)

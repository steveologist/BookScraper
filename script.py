import requests
from bs4 import BeautifulSoup
import csv


def scrape_book_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    product_page_url = url
    book_title = soup.select_one("div.col-sm-6.product_main > h1").text.strip()
    upc = soup.select_one("tr:nth-child(1) > td").text.strip() # noqa
    p_inc_tax = soup.select_one("tr:nth-of-type(4) > td").text.strip()
    p_exc_tax = soup.select_one("tr:nth-of-type(3) > td").text.strip()
    quantity_available = soup.select_one("tr:nth-of-type(6) > td").text.strip()
    product_description = soup.select_one("article.product_page > p").text.strip() # noqa
    category = soup.select("ul.breadcrumb > li")[2].text.strip()
    review_rating = soup.select_one("p.star-rating")['class'][1]
    image_url = soup.select_one("div.item.active > img")['src']


# CREATING ROWS FOR CSV FILES
    row = [product_page_url, book_title, upc, p_inc_tax, p_exc_tax, quantity_available, product_description, category, review_rating, image_url]  # noqa 
    return row
# header = ['Product Page URL', 'Book Title', 'UPC', 'Price Including Tax', 'Price Excluding Tax', 'Quantity Available', 'Product Description', 'Category', 'Review Rating', 'Image URL'] # noqa


def extract_product_urls(url):
    roduct_urls = []
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('h3')

if __name__ == "__main__":
    url = "http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html" # noqa
    row = scrape_book_data(url)

# using Write to External Files method
# use the  .writer()  and  .writerow()  functions to determine columns into a CSV file. # noqa
with open('.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Product Page URL', 'Book Title', 'UPC', 'Price Including Tax', 'Price Excluding Tax', 'Quantity Available', 'Product Description', 'Category', 'Review Rating', 'Image URL']) # noqa
    writer.writerow(row)

print("hope this works")

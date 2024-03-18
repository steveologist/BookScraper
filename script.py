import requests
from bs4 import BeautifulSoup
import csv


def scrape_book_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    product_page_url = url
    book_title = soup.select_one("div.col-sm-6.product_main > h1").text.strip()
    upc = soup.select_one("tr:nth-child(1) > td").text.strip()
    p_inc_tax = soup.select_one("tr:nth-of-type(4) > td").text.strip()
    p_exc_tax = soup.select_one("tr:nth-of-type(3) > td").text.strip()
    quantity_available = soup.select_one("tr:nth-of-type(6) > td").text.strip() # noqa
    product_description = soup.select_one("article.product_page > p").text.strip() # noqa
    category = soup.select("ul.breadcrumb > li")[2].text.strip()
    review_rating = soup.select_one("p.star-rating")['class'][1]
    image_url = soup.select_one("div.item.active > img")['src']

    row = [product_page_url, book_title, upc, p_inc_tax, p_exc_tax, quantity_available, product_description, category, review_rating, image_url] # noqa
    return row


def write_to_csv(filename, rows):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Product Page URL', 'Book Title', 'UPC', 'Price Including Tax', 'Price Excluding Tax', 'Quantity Available', 'Product Description', 'Category', 'Review Rating', 'Image URL']) # noqa
        writer.writerow(rows)


# thru stackoverflow this conditional block allows You to Execute Code When the File Runs as a Script # noqa
if __name__ == "__main__":
    url = "http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html" # noqa
    row = scrape_book_data(url)
    write_to_csv('.csv', row)
    print("Data extracted into .csv")

    print("did this work????")

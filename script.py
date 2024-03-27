# phase 1 complete

import requests
from bs4 import BeautifulSoup
import csv


def get_book_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting information
    product_page_url = url
    upc = soup.find('th', string='UPC').find_next('td').text # noqa
    book_title = soup.find('div', class_='col-sm-6 product_main').find('h1').text # noqa
    price_including_tax = soup.find('th', string='Price (incl. tax)').find_next('td').text # noqa
    price_excluding_tax = soup.find('th', string='Price (excl. tax)').find_next('td').text # noqa
    quantity_available = soup.find('th', string='Availability').find_next('td').text # noqa
    product_description = soup.find('div', id='product_description').find_next('p').text # noqa
    category = soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip() # noqa
    review_rating = soup.find('p', class_='star-rating')['class'][1]
    image_url = soup.find('div', class_='item active').find('img')['src']

    return [product_page_url, upc, book_title, price_including_tax, price_excluding_tax, quantity_available, product_description, category, review_rating, image_url] # noqa


def write_to_csv(data):
    headers = ["product_page_url", "universal_product_code (upc)", "book_title", "price_including_tax", "price_excluding_tax", "quantity_available", "product_description", "category", "review_rating", "image_url"] # noqa
    with open('phase1.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


if __name__ == "__main__":
    url = "http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html" # noqa
    book_info = get_book_info(url)
    write_to_csv([book_info])

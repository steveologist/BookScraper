import requests
from bs4 import BeautifulSoup
import csv


def scrape_book_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_page_url = url
    upc = soup.find('td', text='UPC').find_next_sibling('td').text
    book_title = soup.find('h1').text
    price_including_tax = soup.find('td', text='Price (incl. tax)').find_next_sibling('td').text # noqa
    price_excluding_tax = soup.find('td', text='Price (excl. tax)').find_next_sibling('td').text # noqa
    quantity_available = soup.find('td', text='Availability').find_next_sibling('td').text # noqa
    product_description = soup.find('meta', attrs={'name': 'description'})['content'] # noqa
    category = soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip() # noqa
    review_rating = soup.find('p', class_='star-rating')['class'][1]
    image_url = soup.find('img')['src']

    return {
        'product_page_url': product_page_url,
        'universal_product_code (upc)': upc,
        'book_title': book_title,
        'price_including_tax': price_including_tax,
        'price_excluding_tax': price_excluding_tax,
        'quantity_available': quantity_available,
        'product_description': product_description,
        'category': category,
        'review_rating': review_rating,
        'image_url': image_url
    }


def write_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def main():
    book_info = scrape_book_info("http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html") # noqa
    write_to_csv([book_info], 'book_info.csv')


if __name__ == "__main__":
    main()

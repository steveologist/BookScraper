# phase 2
import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "http://books.toscrape.com/catalogue/"


# get book function takes the URL as input
# soup.find finds all "h3" tags in the parsed HTML document then makes an empty list function called book info list and stored the info. # noqa
# calls a function get_individual_book_info() with this constructed URL to retrieve information about the book. # noqa
def get_book_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    book_list = soup.find_all('h3')

    book_info_list = []

    for book in book_list:
        book_url = BASE_URL + book.a['href'][9:]
        book_info = get_individual_book_info(book_url)
        book_info_list.append(book_info)

    return book_info_list
# use the requests.get() to provide URL
# html.parser parses the HTML content of the response using BeautifulSoup


def get_individual_book_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting information
    product_page_url = url
    upc = soup.find('th', string='UPC').find_next('td').text.strip()
    book_title = soup.find('div', class_='col-sm-6 product_main').find('h1').text # noqa
    price_including_tax = soup.find('th', string='Price (incl. tax)').find_next('td').text # noqa
    price_excluding_tax = soup.find('th', string='Price (excl. tax)').find_next('td').text # noqa
    quantity_available = soup.find('th', string='Availability').find_next('td').text # noqa
    product_description = soup.find('div', id='product_description').find_next('p').text # noqa
    category = soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip() # noqa
    review_rating = soup.find('p', class_='star-rating')['class'][1]
    image_url = soup.find('div', class_='item active').find('img')['src']

    return [product_page_url, upc, book_title, price_including_tax, price_excluding_tax, quantity_available, product_description, category, review_rating, image_url] # noqa


# headers defines a list as columns for a csv files that has the information it is scraping for # noqa
# opens a new csv file in binary mode, also uses csv.writer which writes rows # noqa 
# uses get_book_info function and writes it to a CSV file with the specified headers # noqa
def write_to_csv(data):
    headers = ["product_page_url", "universal_product_code (upc)", "book_title", "price_including_tax", "price_excluding_tax", "quantity_available", "product_description", "category", "review_rating", "image_url"] # noqa
    with open('science_fiction_books.csv', 'w', newline='', encoding='utf-8') as file: # noqa
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


if __name__ == "__main__":
    category_url = "http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html" # noqa
    book_info_all_pages = []
    # Extracting from first page
    book_info_all_pages.extend(get_book_info(category_url))

    # Checking for other pages
    current_page = 2

    while True:
        next_page_url = category_url.replace('index.html', f'page-{current_page}.html') # noqa
        response = requests.get(next_page_url)

        if response.status_code == 200:
            book_info_all_pages.extend(get_book_info(next_page_url))
            current_page += 1
    write_to_csv(book_info_all_pages)

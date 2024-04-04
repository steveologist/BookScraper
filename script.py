# opersating system import helps functions with working files and directories
import os
import requests
from bs4 import BeautifulSoup
import csv

# base url is a string variable that holds the base URL of a website. # noqa
# index url holds the URL of the index page of the website # noqa
BASE_URL = "http://books.toscrape.com/"
INDEX_URL = BASE_URL + "index.html"


# get categories retrieves categories from books to scrape
# uses the requests.get() to provide URL
# html.parser parses the HTML content of the response using BeautifulSoup
def get_categories():
    response = requests.get(INDEX_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    categories = soup.select('.side_categories > ul > li > ul > li > a')
    return [(category.text.strip(), BASE_URL + category['href']) for category in categories] # noqa


# makes an empty list called book_info_list to store information about each book. # noqa
def get_books_category(category_name, category_url):
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    book_list = soup.find_all('h3')

    book_info_list = []
    for book in book_list:
        book_url = BASE_URL + 'catalogue' + book.a['href'][8:]
        book_info = get_ind_info(book_url)
        book_info_list.append(book_info)

    write_to_csv(book_info_list, category_name)


# use the requests.get() to provide URL
# html.parser parses the HTML content of the response using BeautifulSoup
def get_ind_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
# searches for the table header (th) containing the text 'UPC', finds the next table data (td) element # noqa
# Retrieves the all information from the HTML. It looks for the table header containing 'Price (incl. tax)' # noqa
# image url constructs the URL for the image of the product.
    product_page_url = url
    upc = soup.find('th', string='UPC').find_next('td').text.strip()
    book_title = soup.find('div', class_='col-sm-6 product_main').find('h1').text # noqa
    price_including_tax = soup.find('th', string='Price (incl. tax)').find_next('td').text # noqa
    price_excluding_tax = soup.find('th', string='Price (excl. tax)').find_next('td').text # noqa
    quantity_available = soup.find('th', string='Availability').find_next('td').text # noqa

    product_description_element = soup.find('div', id='product_description')
    product_description = product_description_element.find_next('p').text if product_description_element else None # noqa

    category = soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip() # noqa
    review_rating = soup.find('p', class_='star-rating')['class'][1]
    image_url = BASE_URL + soup.find('div', class_='item active').find('img')['src']# noqa

    # Download and save image
    image_filename = save_image(book_title, image_url)

    return [product_page_url, upc, book_title, price_including_tax, price_excluding_tax, quantity_available, product_description, category, review_rating, image_filename] # noqa


def save_image(book_title, image_url):
    # Create a directory if it doesn't exist
    if not os.path.exists("images"):
    # os.makedirs checks if the directory "images" exists. If it doesn't, it creates one # noqa
        os.makedirs("images")

    # Get the image filename
    # book_title is modified to replace any slashes ('/') with underscores ('_') to ensure it can be used as part of a filename # noqa
    image_filename = f"images/{book_title.replace('/', '_')}.jpg"

    # returns the filename of a saved image
    response = requests.get(image_url)
    with open(image_filename, 'wb') as f:
        f.write(response.content)

    return image_filename


# headers defines a list as columns for a csv files that has the information it is scraping for # noqa
# opens a new csv file in binary mode, also uses csv.writer which writes rows
# uses get_book_info function and writes it to a CSV file with the specified headers # noqa
def write_to_csv(data, category_name):
    headers = ["product_page_url", "universal_product_code (upc)", "book_title", "price_including_tax", "price_excluding_tax", "quantity_available", "product_description", "category", "review_rating", "image_url"] # noqa
    file_name = f"{category_name.replace('/', '_')}.csv"
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


# if __name__ == "__main__": This line checks whether the script is being run directly or if it's being imported as a module by another script. # noqa
# calls the function get_book_info with the provided URL and assigns the returned book information to the variable  # noqa
#  book_info This function writes the book information to a CSV file.
if __name__ == "__main__":
    categories = get_categories()
    for category_name, category_url in categories:
        print("Scraping:", category_name)
        get_books_category(category_name, category_url)

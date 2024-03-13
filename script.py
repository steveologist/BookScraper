import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape data from a product page


def scrape_product_page(url):

    # Send a GET request to the product page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting required data
    product_page_url = url
    upc = soup.find('th', text='UPC').find_next('td').text
    title = soup.find('h1').text.strip()
    p_in_tax = soup.find('th', text='P (inc)').find_next('td').text.strip()[1:]
    p_ex_tax = soup.find('th', text='P (exc)').find_next('td').text.strip()[1:]
    q_available = soup.find('th', text='Avail').find_next('td').text.strip()
    description = soup.find('meta', attrs={'name': 'description'})['content']
    cat = soup.find('a', href=lambda href: href and 'cat' in href).text.strip()
    review_rating = soup.find('p', class_='star-rating')['class'][1]
    image_url = soup.find('div', class_='item active').find('img')['src']

    return {
        'product_page_url': product_page_url,
        'universal_product_code (upc)': upc,
        'book_title': title,
        'p_in_tax': p_in_tax,
        'p_ex_tax': p_ex_tax,
        'q_available': q_available,
        'product_description': description,
        'cat': cat,
        'review_rating': review_rating,
        'image_url': image_url
    }


# Function to write data to a CSV file


def write_to_csv(data, filename):

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


# Main function


def main():

    # URL of the product page
    url = 'http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html'

    # Scrape data from the product page

    product_data = scrape_product_page(url)

    # Write data to a CSV file
    write_to_csv([product_data], 'product_data.csv')


if __name__ == '__main__':
    main()

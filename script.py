import requests
from bs4 import BeautifulSoup
import csv

def scrape_product_page(url): 
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # div.col-sm-6.product_main > p.price_color
    # content_inner > article > p
    price_elements = soup.select("p.price_color")
    for price_element in price_elements:
        # Do something with price_element
        pass  # Placeholder, replace with actual processing code

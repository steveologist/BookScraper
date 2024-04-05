# Project 2
##  Python script scrapes book information from a website and writes it to CSV files.
## imports
- Requests for making HTTP requests
- BeautifulSoup for parsing HTML
- csv for handling CSV files
## Base URL
- It sets the base URL and index URL of the website.

## Function get_categories()
- Sends an HTTP GET request to the index URL
- Parses the HTML response using BeautifulSoup

## Function get_books_category()
- Takes a category name and URL as input
- Sends an HTTP GET request to the category URL
- Parses the HTML response using BeautifulSoup
- Finds all book titles in the category

## Function get_ind_info()
- Takes a book URL as input
- Sends an HTTP GET request to the book URL
- Parses the HTML response using BeautifulSoup
- Extracts various book details such as UPC, title, price, quantity, description, category, review rating, and image URL
- Saves the book's image to a local directory


## Function save_image()
- Saves the book's image to the 'images' directory
- Returns the filename of the saved image

## Function write_to_csv()
- Defines CSV headers
- Writes the book information to a CSV file named after the category
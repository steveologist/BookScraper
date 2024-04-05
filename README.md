 # __Project 2__
##  _Python script scrapes book information from a website and writes it to CSV files._

### Set Up Virtual Environment:
- Open your terminal or command prompt.
- Navigate to the directory where your code is located.
- Other options could be to make a folder anywhere and make that the directory to add the deliverables to
- ( I use mac so to get there I use `cd` `ls` etc )
- Run the following command to create a virtual environment named 'venv':
    ` python -m venv venv `

### Activate Virtual Environment:
- On Windows:
   ` venv\Scripts\activate `
- On macOS and Linux:
   ` source venv/bin/activate `

### Install Dependencies:
- Notice that your command prompt changes, indicating that the virtual environment is active.
- Install the required dependencies by running:
   ` pip install requests beautifulsoup4 `

### Run the Application:
- With the virtual environment activated and dependencies installed, run the application code.
- Run the Python script by executing:
    ` python script.py ` or ` python3 script.py `
- The script will start scraping book information from the provided website and save it into CSV files.
- In my case the deliverables will be on my desktop in a folder named "Bookscraper"

### Deactivate Virtual Environment:
- Once you're done running the application
- deactivate the virtual environment by running:

    ` deactivate `
- This will return you to your normal command prompt environment.





# __Info about script.py__



### Imports
- Requests for making HTTP requests
- BeautifulSoup for parsing HTML
- csv for handling CSV files
- opersating system import helps functions with working files and directories

### Base URL
- It sets the base URL and index URL of the website.

### Function get_categories()
- Sends an HTTP GET request to the index URL
- Parses the HTML response using BeautifulSoup

### Function get_books_category()
- Takes a category name and URL as input
- Sends an HTTP GET request to the category URL
- Parses the HTML response using BeautifulSoup
- Finds all book titles in the category

### Function get_ind_info()
- Takes a book URL as input
- Sends an HTTP GET request to the book URL
- Parses the HTML response using BeautifulSoup
- Extracts various book details such as UPC, title, price, quantity, description, category, review rating, and image URL
- Saves the book's image to a local directory


### Function save_image()
- Saves the book's image to the 'images' directory
- Returns the filename of the saved image

### Function write_to_csv()
- Defines CSV headers
- Writes the book information to a CSV file named after the category

## After executing the script it will print the progress as it scrapes each category and writes the data to CSV files.
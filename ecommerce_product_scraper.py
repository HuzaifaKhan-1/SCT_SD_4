import requests
from bs4 import BeautifulSoup
import csv

# URL of the e-commerce page to scrape
url = 'http://books.toscrape.com/catalogue/category/books/science_22/index.html'

# Sending a request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Finding the containers for the product information
books = soup.find_all('article', class_='product_pod')

# Opening a CSV file to write the data
with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Book Title', 'Price', 'Rating', 'Availability'])

    # Looping through the books and extract information
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text.strip()
        rating = book.p['class'][1]  # The rating is in the class of the <p> tag
        availability = book.find('p', class_='instock availability').text.strip()

        # Writing the data to the CSV file
        writer.writerow([title, price, rating, availability])

print("Data has been written to books.csv")

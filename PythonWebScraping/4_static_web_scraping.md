---
marp: true
author: Rian Adi
theme: gaia
backgroundColor: white
footer: Data Scraping | rianaditro
---
<!-- _backgroundColor: grey -->
<!-- _color: white -->
<!-- _paginate: skip -->
<br>
<br>
<br>
<br>

# Static Web Scraping
KELAS DATA SCRAPING
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

---
<!-- paginate: true -->
## BeautifulSoup
BeautifulSoup is a Python library that simplifies the process of web scraping by allowing developers to extract data from HTML documents easily. It transforms complicated HTML documents into a tree of Python objects, such as tags, navigable strings, and comments. This makes it straightforward to locate and manipulate the desired data.

```python
from bs4 import BeautifulSoup
```

---
## Common Bs4 Operations
**Using find() to Get the First Match**
```python
soup = BeautifulSoup(html, 'html.parser')

# Find the first product div
first_product = soup.find('div', class_='product')
print(first_product)  # Prints the first div with class "product"

# Get the text inside the first product name (h2)
product_name = first_product.find('h2').get_text()
print(product_name)  # Output: Product 1
```
---
**Using find_all() to Get All Matches**
```python
# Find all product divs
products = soup.find_all('div', class_='product')

for product in products:
    # Get product name (h2 tag)
    name = product.find('h2').get_text()
    
    # Get product price (p tag with class "price")
    price = product.find('p', class_='price').get_text()
    
    # Get the "href" attribute from the "a" tag
    buy_link = product.find('a', class_='buy-link')['href']
    
    print(f"Name: {name}, Price: {price}, Buy link: {buy_link}")
```
---
**Using get_text() to Extract Text**
```python
# Extract text of the first product description
description = first_product.get_text()
print(description)
```
**Using get() to Extract Attributes**
```python
# Extract the href attribute safely using get()
buy_link = first_product.find('a', class_='buy-link').get('href')
print(buy_link)  # Output: https://example.com/product-1
```
---
## Class Activity
Open a webpage and save it manually into a HTML file, parse it using BeautifulSoup and print the result in the terminal!

---
## Requests
The Requests library is a popular Python tool that allows you to easily make HTTP requests. It is commonly used for web scraping, where you need to gather data from websites. Think of HTTP requests as asking a website to give you information, like a page of text or an image. With Requests, you can send these requests with just a few lines of code and receive responses that contain the information you need.

```python
import requests
```

---
**Requests Code Example**
```python
import requests  # Import the requests library

# Send a GET request to a website
response = requests.get('https://www.example.com')

# Check the status code of the response
print(f'Status Code: {response.status_code}')  # Outputs the HTTP status code

# Get the content of the response as text
html_content = response.text
print(html_content)  # Outputs the HTML content of the page
```
---
**Difference Between .text and .content**
```python
# Using .content to get raw bytes
binary_content = response.content
print(type(binary_content))  # Outputs: <class 'bytes'>

# If you want to convert it to a string (e.g., HTML), you would decode it:
html_string = binary_content.decode('utf-8')
print(html_string)  # Outputs the HTML as a string
```
---
## Class Activity
Send a GET request to https://api.github.com/users/octocat using the Requests library and print the status code. Use loop and enumerate to find how many requests send before reaching status code 429.

---
## Learn More
Join us on this self-study journey! Click the link below to get started.
- [Requests Documentation](https://docs.python-requests.org/en/master/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)

---
## Discover Advanced Topic
Master this advanced topic and supercharge your skills.
- [How to Scrape Multiple Web Pages Using Python](https://www.freecodecamp.org/news/how-to-scrape-multiple-web-pages-using-python/)

---
## Homework Assignment
Create a script to send a request to https://quotes.toscrape.com/ and extract the data for 3 or more pages

---
<!-- _backgroundColor: grey -->
<!-- _color: white -->
<!-- _paginate: false -->
<br>
<br>
<br>
<br>

# Thank you
Any Question?
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024


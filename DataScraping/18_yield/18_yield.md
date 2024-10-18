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

# Yield
KELAS DATA SCRAPING
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

---
<!-- paginate: true -->
## Introduction
Start
v
[`URL/page/1`, `URL/page/2`, `URL3/page/3`,...]
v
[`product_URL1`, `product_URL2`, `product_URL3`, ...]
v
[`HTML product1`, `HTML product2`, `HTML product3`, ...]
v
[`data product1`, `data product2`, `data product3`, ...]
v
Finished

---
During the scraping process, all the data is stored in a list. Each item in a list is stored in a **block of memory**. As the list gets bigger, it continues to take up memory space, even if we **no longer need** the earlier data.

Once the list reaches the system's **memory limit**, the program may fail, causing your scraping process to **terminate unexpectedly.**

---
## Generator
```python
def countdown(n):
        while n > 0:
            yield n  # use yield instead of return
            n -= 1

yield_obj = countdown(5) # declaring generator object

print(type(countdown)) #<class 'function'>
print(type(yield_obj)) #<class 'generator'>

for num in countdown(5): # example of how to use generator
    print(num)
```

---
## How Generator Works?
[`URL/page/1`, `URL/page/2`, `URL3/page/3`,...]
First loop:
==> `URL/page/1`
=====> `product_URL1` |memory block 1|
=========> `HTML product1` |memory block 2|
[`data product1`] |memory block 3|
Second loop:
==> `URL/page/2`
=====> `product_URL2` |memory block 1|
=========> `HTML product2` |memory block 2|
[`data product1`, `data product2`] |memory block 3|

---
## Memory Consumtion
```python
def scrape_all_data(pages):
    data = []
    for page in range(1, pages + 1):
        page_data = [f"Item {i} from page {page}" for i in range(100)] # Simulating data for each page (each page has 100 items)
        data.extend(page_data)
    return data

# Simulating data scraping using a generator
def scrape_data_generator(pages):
    for page in range(1, pages + 1):
        page_data = [f"Item {i} from page {page}" for i in range(100)] # Simulating data for each page (each page has 100 items)
        yield page_data  # Yielding data one page at a time

data_list = scrape_all_data(10) # Scraping 10 pages and storing everything in memory
data_generator = scrape_data_generator(10) # Creating the generator

print(f"Memory usage with list: {sys.getsizeof(data_list)} bytes")
print(f"Memory usage with generator: {sys.getsizeof(data_generator)} bytes")
```
Memory usage with list: 9080 bytes
Memory usage with generator: 104 bytes

---
## Yield in Scraping Function
```python
import requests

# Function to scrape a multipage site, yielding the response object for each page
def scrape_multipage_site(base_url, total_pages):
    for page in range(1, total_pages + 1):
        url = f"{base_url}?page={page}"  # Construct the URL for each page
        response = requests.get(url)  # Make the request to the current page
        yield response  # Yield the response object without storing it in memory

# Example usage
base_url = "https://example.com/products"
total_pages = 5  # Number of pages you want to scrape

for response in scrape_multipage_site(base_url, total_pages):
    # Process each response one at a time
```

---
## Task
Create a script to scraping https://www.scrapingcourse.com/pagination/ by using generator for every loop instead of returning all the result at once. Notice when you can use yield or return.

---
## Learn More
THIS is a better way to return scraped data.
https://www.youtube.com/watch?v=WlZx9f7AxUI

Python Generators (yield) - Python Web Scraping for Beginners
https://www.youtube.com/watch?v=I3JMS5fQ5Ug

Generators
https://docs.python.org/3/tutorial/classes.html#generators

---
## Discover Advanced Topic
Garbage Collection in Python
https://www.geeksforgeeks.org/garbage-collection-python/

Reading a huge .csv file
https://stackoverflow.com/a/43286094/23418303

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


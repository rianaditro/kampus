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

# Main Topic
Memory Efficient Scraping
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

---
<!-- paginate: true -->
## Introduction
During the scraping process, all data is stored in a list. Each item in a list is stored in a **block of memory**. As the list grows, it continues to take up memory even when we **no longer need** the earlier data.

Once the list reaches the system's **memory limit**, the program may fail, causing your scraping process to **terminate** unexpectedly.

```python
yield data
```

---
## Yield
```python
def scrape_all_data(pages):
    data = []
    for page in range(1, pages + 1):
        page_data = [f"Item {i} from page {page}" for i in range(100)]
        data.extend(page_data)
    return data

# Simulating data scraping using a generator
def scrape_data_generator(pages):
    for page in range(1, pages + 1):
        page_data = [f"Item {i} from page {page}" for i in range(100)]
        yield page_data  # Yielding data one page at a time

data_list = scrape_all_data(10)
data_generator = scrape_data_generator(10)

print(f"Memory usage with list: {sys.getsizeof(data_list)} bytes")
print(f"Memory usage with generator: {sys.getsizeof(data_generator)} bytes")
```
---
**Scraping with Yield**
```python
def scrape_multipage_site(base_url, total_pages):
    for page in range(1, total_pages + 1):
        url = f"{base_url}?page={page}"
        response = requests.get(url) 
        yield response

# Example usage
base_url = "https://example.com/products"
total_pages = 5  # Number of pages you want to scrape

for response in scrape_multipage_site(base_url, total_pages):
    # Process each response one at a time
```

---
## Class Activity
Create a script to scraping https://www.scrapingcourse.com/pagination/ by using generator for every loop instead of returning all the result at once. Notice when you can use yield or return.

---
## Learn More
Join us on this self-study journey! Click the link below to get started.
- [THIS is a better way to return scraped data](https://www.youtube.com/watch?v=WlZx9f7AxUI)
- [Python Generators (yield) - Python Web Scraping for Beginners](https://www.youtube.com/watch?v=I3JMS5fQ5Ug)

---
## Discover Advanced Topic
Master this advanced topic and supercharge your skills.
- [Reading a huge .csv file](https://stackoverflow.com/a/43286094/23418303)

---
## Homework Assignment
Create a list of URLs in a CSV file. Use yield to read the rows one by one and extract the page!

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


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

# Faster Scraping
KELAS DATA SCRAPING
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

---
<!-- paginate: true -->
## Introduction
Request made → Response received → Process response

When web scraping, the scraper sends a request to a website, waits for the response, processes the data, and only then sends the next request.

Meanwhile, the moment after the request made and before the response received our computer are idle.
<!-- handball game to help better understanding -->

---
## How to not wait?
- Use **Multi-Threading**
With threading, each thread handles a separate HTTP request, reducing the time spent waiting.

- Use **Asynchronous**
Asynchronous programming allows you to make requests concurrently using a single thread, without blocking the program execution.

---
## Multi-Threading
ThreadPoolExecutor works like assigning a group of people to finish tasks together. Instead of doing tasks one by one, the team (or pool of threads) can handle multiple tasks at once, making the process faster and more efficient.

---
## ThreadPoolExecutor
```python
import requests
from concurrent.futures import ThreadPoolExecutor


# Initiate a group of 4 worker
executor = ThreadPoolExecutor(max_worker=4)
# This will create a generator for requests.get
response_list = executor.map(requests.get, urls)

for response in response_list:
    # Processing each response

```

---
## Pros and Cons Multi-Threading
**Pros**
- Easy to implement
- Works with synchronous code

**Cons**
- Higher memory consumption
- Limited scaling

---
## Task
Implement multi-threading using ThreadPoolExecutor to your multipage scraping. Compare the time used, before and after.

**Challenge**
Try to reuse the same session across all threads. By sharing a session, you reduce connection setup overhead and improve efficiency.

---
## Asynchronous
Asynchronous programming is a paradigm that enables a program to execute multiple tasks concurrently without waiting for each task to complete before starting the next one. 

It allows you to make requests concurrently using a single thread, without blocking the program execution

---
## CPU-bound vs. I/O-bound Tasks
Not all programs can effectively implement asynchronous programming because **async is designed to improve performance primarily for I/O-bound tasks**, not for CPU-bound tasks.

I/O-bound tasks are network requests (e.g., web scraping or API calls), file I/O (e.g., reading or writing large files), database queries.

CPU-bound tasks are mathematical computations, data processing, image or video processing, etc

---
## Why Async is NOT for all tasks
Example of simple program using synchronous
```python
def print_message(message):
    print(message)

messages = ["Hello", "World", "This", "is", "Async", "Demo"]

for message in messages:
    print_message(message)
```

---
## Why Async is NOT for all tasks
Example of simple program using asynchronous
```python
import asyncio

async def print_message(message):
    print(message)

async def main():
    messages = ["Hello", "World", "This", "is", "Async", "Demo"]
    tasks = [print_message(message) for message in messages]
    await asyncio.gather(*tasks)

# Run the async program
asyncio.run(main())
```

---
## Converting Sync into Async
It is not just simply put async-await keyword. Its literally changing library you used.
```python
time.sleep(10)  ---> asyncio.sleep(10)
file.read()     ---> aiofile
requests        ---> aiohttp
```

---
## Sending Request with Aiohttp
```python
# Asynchronous function to fetch a single URL
async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()

# Asynchronous function to scrape a list of URLs concurrently
async def scrape_urls(urls):
    async with aiohttp.ClientSession() as session:
        # Create tasks to fetch each URL asynchronously
        tasks = [fetch_page(session, url) for url in urls]
        
        # Run all tasks concurrently and gather results
        results = await asyncio.gather(*tasks)
        
        return results
```

---
## Sending Request with Aiohttp
```python
if __name__ == "__main__":
    urls = [f"https://www.bbc.com/search?page={i}" for i in range(10)]

    # Run the async event loop to scrape all URLs
    scraped_data = asyncio.run(scrape_urls(urls))
    
    # Print the scraped content (for demonstration purposes)
    for i, content in enumerate(scraped_data, 1):
        print(f"Content from URL {i}: {content[:100]}...")  # Print first 100 characters
```

---
## Task
Implement asyncio to your code, re-write how you send data between the functions. Compare the time used, before and after.

**Challenge**
Sending multiple URLs concurrently has many benefits, but it can also cause issues like server overload or getting your IP blocked. To avoid these problems, apply rate limiting to manage how many requests are sent simultaneously.

---
## Learn More
Learn more on how to achieve best practice data scraping 
https://asynciolimiter.readthedocs.io/en/latest/
https://proxiesapi.com/articles/effective-strategies-for-rate-limiting-asynchronous-requests-in-python

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


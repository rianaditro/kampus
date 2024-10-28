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

# Time Efficient Scraping
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

In web scraping, the scraper sends a request to a website, waits for the response, processes the data, and then sends the next request.

Meanwhile, our computer is idle from the time the request is made until the response is received.

```python
print(f"Waiting response for {URL}...")
```

---
## Multi-Threading with ThreadPoolExecutor
ThreadPoolExecutor works like assigning a group of people to finish tasks together. Instead of doing tasks one by one, the team (or pool of threads) can handle multiple tasks at once, making the process faster and more efficient.
```python
from concurrent.future import ThreadPoolExecutor
```
---
**Using ThreadPoolExecutor in Web Scraping**
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
## Class Activity
Implement multi-threading using ThreadPoolExecutor to your multipage scraping. Compare the time used, before and after.

**Challenge**: Try to reuse the same session across all threads. By sharing a session, you reduce connection setup overhead and improve efficiency.

---
## Asynchronous Scraping
Asynchronous programming is a paradigm that enables a program to execute multiple tasks concurrently without waiting for each task to complete before starting the next one.

It allows you to make requests concurrently using a single thread, without blocking the program execution.
```python
import asyncio
```
---
**A Simple Asynchronous**
```python
import asyncio

async def count(name):
    await asyncio.sleep(1)
    print(f'{name}_1')
    await asyncio.sleep(1)
    print(f'{name}_2')
    await asyncio.sleep(1)
    print(f'{name}_3')

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    asyncio.run(main())
```
---
**Asynchronous Scraping with Aiohttp**
```python
async def fetch_single_page(url):
        async with aiohttp.ClientSession() as session:
            response = await session.get(url)
            return await response.text()
    
asyncio.run(fetch_single_page(url))
```
---
## Class Activity
Analyze our scraping example!
**Quiz**: Does it implement asynchronous? Is it faster than using requests?

---
**Sending Multiple Request with Aiohttp**
```python
async def fetch_multiple_pages(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task( 
                # This will add a 'task' with pending status
                session.get(url) 
            )
            tasks.append(task)
        return await asyncio.gather(*tasks)
        #  This runs all tasks concurrently, 
        # waits for them to finish, and collects their results

asyncio.run(fetch_multiple_pages(urls))
```
---
## Class Activity
Instead of getting the ClientResponse object, try to get the HTML content directly.

---
## Learn More
Join us on this self-study journey! Click the link below to get started.
- [ThreadPoolExecutor in Python: The Complete Guide](https://superfastpython.com/threadpoolexecutor-in-python/)
- [Asynchronous Web Scraping in Python](asynchronous-web-scraping-python#making-python-requests-async-friendly)
- [Python Asyncio: The Complete Guide](https://superfastpython.com/python-asyncio/)

---
## Discover Advanced Topic
Master this advanced topic and supercharge your skills.
- [Rate Limiting Asynchronous Requests in Python](https://proxiesapi.com/articles/effective-strategies-for-rate-limiting-asynchronous-requests-in-python)

---
## Homework Assignment
Implement asyncio to your code, re-write how you send data between the functions. Compare the time used, before and after.

**Challenge**: Sending multiple URLs concurrently has many benefits, but it can also cause issues like server overload or getting your IP blocked. To avoid these problems, apply rate limiting to manage how many requests are sent simultaneously.

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


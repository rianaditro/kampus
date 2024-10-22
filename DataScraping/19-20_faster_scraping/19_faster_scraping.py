import requests
from bs4 import BeautifulSoup
import time

import asyncio
import aiohttp

from concurrent.futures import ThreadPoolExecutor

def main_thread(urls):
    # Run the async event loop to scrape all URLs
    with ThreadPoolExecutor() as executor:
        response_list = executor.map(requests.get, urls)

    response_data = [response.text for response in response_list]
    return response_data

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
    
async def single_async(url):
    async with aiohttp.ClientSession() as session:
        response = await fetch_page(session, url)
        return response


if __name__ == "__main__":
    start_time = time.time()
    urls = [f"https://www.bbc.com/search?page={i}" for i in range(10)]

    # # using threading
    response_data = main_thread(urls)

    # # using async
    # response_data = asyncio.run(scrape_urls(urls))

    end_time = time.time()

    print(len(response_data))
    print(f"Total execution time: {end_time - start_time:.4f} seconds")


    
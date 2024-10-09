import requests
import sys

from bs4 import BeautifulSoup as bs


""" Yield in Action """

"""
A function + yield keyword = generator
A generator is a special kind of iterator that allows you to iterate over a sequence of values.

Why its matter?
+ Memory Efficient
+ Streaming case
+ Improve performance

When to use?
+ Real-time data processing. Sensor IoT, stock market, etc
+ ETL data pipeline. Instead of loading terrabytes of data at once, load it in small chunks/batches
+ Data scraping multi pages

"""

""" Introduction to Yield start here """
def intro_yield():
    # simple function using yield
    def countdown(n):
        while n > 0:
            yield n
            n -= 1

    # declaring generator object
    yield_obj = countdown(5)

    print(type(countdown)) #<class 'function'>
    print(type(yield_obj)) #<class 'generator'>

    # example of how to use generator
    for num in countdown(5):
        print(num)
""" Introduction to Yield end here """

""" Comparing size of function and generator start here """
def compare_size():
    # Simulating data scraping by storing all data in a list
    def scrape_all_data(pages):
        data = []
        for page in range(1, pages + 1):
            # Simulating data for each page (each page has 100 items)
            page_data = [f"Item {i} from page {page}" for i in range(100)]
            data.extend(page_data)
        return data

    # Simulating data scraping using a generator
    def scrape_data_generator(pages):
        for page in range(1, pages + 1):
            # Simulating data for each page (each page has 100 items)
            page_data = [f"Item {i} from page {page}" for i in range(100)]
            yield page_data  # Yielding data one page at a time

    # Scraping 10 pages and storing everything in memory
    data_list = scrape_all_data(10)

    # Creating the generator
    data_generator = scrape_data_generator(10)

    # Checking memory usage
    print(f"Memory usage with list: {sys.getsizeof(data_list)} bytes")

    # Checking memory usage (only generator object is in memory)
    print(f"Memory usage with generator: {sys.getsizeof(data_generator)} bytes")
""" Comparing size of function and generator end here """

""" Yield in scraping start here """
def scrape_yield():
    # Generator for scraping multiple pages
    def scrape_pages(num_pages):
        for page in range(1, num_pages + 1):
            url = f"https://bbc.com/search?page={page}"
            print(url)

            response = requests.get(url)
            soup = bs(response.text, "html.parser")
            
            # Extract some data from the page (for example, titles)
            titles = soup.find_all("h2", {"data-testid":"card-headline"})
            
            # Yield the titles from the current page
            yield [title.text for title in titles]

    # Scrape and process 5 pages one by one
    for page_titles in scrape_pages(100):
        print(f"Scraped {len(page_titles)} titles from a page:")
        print(page_titles)

""" Yield in scraping end here """


if __name__ == "__main__":
    # # run 1st
    intro_yield()

    # # run 2nd
    # compare_size()

    # # run 3rd
    # scrape_yield()

import requests
import asyncio
import aiohttp
import httpx
import concurrent.futures
import time

from multiprocessing import Pool
from curl_cffi import requests as curlRequests
from curl_cffi.requests import AsyncSession as curlAsyncSession



""""
To speed up the scraping process, you can use the following methods:

1. Use Request Session (Connection Pooling)
2. Use Threading/Multiprocessing
3. Use Asynchronous Requests

"""



# define decorator to record execution time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} executed in {execution_time:.4f} seconds")
        return {"function name": func.__name__, "execution time": execution_time}
    return wrapper


""" Use basic functions """
@timer
def basic_request(urls):
    for url in urls:
        requests.get(url)

@timer
def basic_httpx(urls):
    for url in urls:
        httpx.get(url)

@timer
def basic_curl(urls):
    for url in urls:
        curlRequests.get(url)

"""  Use Session (Connection Pooling) """
@timer
def request_with_session(urls):
    session = requests.Session()
    for url in urls:
        session.get(url)
    session.close()

@timer
def httpx_with_session(urls):
    session = httpx.Client()
    for url in urls:
        session.get(url)
    session.close()

@timer
def curl_with_session(urls):
    session = curlRequests.Session()
    for url in urls:
        session.get(url)
    session.close()


""" Use Threading/Multiprocessing """
def threaded_request(urls):
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(requests.get, urls)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Function threaded_request executed in {execution_time:.4f} seconds")
    return {"function name": "threaded_request", "execution time": execution_time}

def multiprocessing_requests(urls):
    start_time = time.time()
    with Pool(4) as pool:
        pool.map(basic_request, urls)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Function multiprocessing_requests executed in {execution_time:.4f} seconds")
    return {"function name": "multiprocessing_requests", "execution time": execution_time}

""" Use Asynchronous Requests """
async def async_aiohttp(urls):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(session.get(url)))
        await asyncio.gather(*tasks)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Function async_aiohttp executed in {execution_time:.4f} seconds")
    return {"function name": "async_aiohttp", "execution time": execution_time}

async def async_curl(urls):
    start_time = time.time()
    async with curlAsyncSession() as s:
        tasks = []
        for url in urls:
            task = s.get(url)
            tasks.append(task)
        await asyncio.gather(*tasks)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Function async_curl executed in {execution_time:.4f} seconds")
    return {"function name": "async_curl", "execution time": execution_time}


if __name__ == "__main__":

    # list of urls
    urls = [f"https://www.bbc.com/search?page={i}" for i in range(9)]

    # list of functions
    list_func = [
        basic_request,
        basic_httpx,
        basic_curl,
        request_with_session,
        httpx_with_session,
        curl_with_session,
        threaded_request,
        # multiprocessing_requests,
        # async_aiohttp,
        # async_curl
    ]

    aiohttp_timer = asyncio.run(async_aiohttp(urls))
    curl_async_timer = asyncio.run(async_curl(urls))

    time_recorder = [
        aiohttp_timer,
        curl_async_timer
    ]


    for func in list_func:
        time_recorder.append(func(urls))
    

    sorted_time_recorder = sorted(time_recorder, key=lambda x: x["execution time"])
    
    for item in sorted_time_recorder:
        print(item)
    
"""
for 10 page:
{'function name': 'threaded_request', 'execution time': 0.32482290267944336}
{'function name': 'async_curl', 'execution time': 0.35677051544189453}
{'function name': 'async_aiohttp', 'execution time': 0.4574410915374756}
{'function name': 'request_with_session', 'execution time': 0.5395686626434326}
{'function name': 'curl_with_session', 'execution time': 0.5804407596588135}
{'function name': 'httpx_with_session', 'execution time': 0.6912610530853271}
{'function name': 'basic_curl', 'execution time': 1.1148927211761475}
{'function name': 'basic_request', 'execution time': 1.2195713520050049}
{'function name': 'basic_httpx', 'execution time': 2.2062225341796875}

for 100 page:
{'function name': 'threaded_request', 'execution time': 2.3825461864471436}
{'function name': 'async_curl', 'execution time': 3.5307583808898926}
{'function name': 'async_aiohttp', 'execution time': 4.384057283401489}
{'function name': 'httpx_with_session', 'execution time': 5.308608531951904}
{'function name': 'request_with_session', 'execution time': 5.326570510864258}
{'function name': 'curl_with_session', 'execution time': 6.334142446517944}
{'function name': 'basic_request', 'execution time': 14.052895545959473}
{'function name': 'basic_curl', 'execution time': 15.319042205810547}
{'function name': 'basic_httpx', 'execution time': 28.373396396636963}
"""

"""
Advanced tips:
- Use batch processing
- use faster parser
- use proxy
"""

"""
import requests
from bs4 import BeautifulSoup
import time
from lxml import html

url = 'https://example.com'

# Test with BeautifulSoup default parser
start = time.time()
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.title.text)
end = time.time()
print(f"BeautifulSoup (html.parser) took {end - start:.4f} seconds")

# Test with BeautifulSoup using lxml
start = time.time()
soup = BeautifulSoup(response.content, 'lxml')
print(soup.title.text)
end = time.time()
print(f"BeautifulSoup (lxml) took {end - start:.4f} seconds")

# Test with lxml directly
start = time.time()
tree = html.fromstring(response.content)
title = tree.xpath('//title/text()')[0]
print(title)
end = time.time()
print(f"lxml took {end - start:.4f} seconds")


BeautifulSoup (html.parser) took 0.1564 seconds
BeautifulSoup (lxml) took 0.0253 seconds
lxml took 0.0109 seconds

"""
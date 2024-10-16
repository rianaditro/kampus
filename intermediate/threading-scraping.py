"""
concurrent.futures — Launching parallel tasks¶

https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor-example

The concurrent.futures module provides a high-level interface for asynchronously executing callables.

The asynchronous execution can be performed with 
threads, using ThreadPoolExecutor, or
separate processes, using ProcessPoolExecutor. 

ThreadPoolExecutor is a tool that allows multiple tasks to run at the same time by
using a group of workers, or threads. 
Instead of waiting for one task to finish before starting the next, 
it lets several tasks happen at once, making the process faster and more efficient.

The ProcessPoolExecutor is a tool that helps run multiple tasks at the same time by 
using separate workers, called processes. 
Unlike threads, these processes run independently, 
which allows them to perform tasks more efficiently, 
especially when doing heavy work that needs a lot of computing power. 
However, it only works with certain types of data that can be easily shared between these workers.


Both implement the same interface, which is defined by the abstract Executor class.

Which one to use and when?
- use ThreadPoolExecutor for IO-bound tasks, example: web scraping, file reading
- use ProcessPoolExecutor for CPU-bound tasks, example: image processing, data calculation

"""


import requests
from concurrent.futures import ThreadPoolExecutor

from multiprocessing import Pool


def request_responses(urls):
    session = requests.Session()
    responses = [session.get(url) for url in urls]
    print(len(responses))
    print(type(responses[0]))
    print(type(responses))
    return responses


def request_executor_map(urls):
    # use session 
    session = requests.Session()

    with ThreadPoolExecutor() as executor: # create a ThreadPoolExecutor object
        responses = executor.map(session.get, urls) # return an iterator
        responses = list(responses) # convert iterator to list
        print(len(responses))
        print(type(responses[0]))
        print(type(responses))

    return responses


if __name__ == "__main__":
    urls = [
        f"https://www.bbc.com/search?page={i}" for i in range(60)
    ]

    request_responses(urls)
    # request_executor_map(urls)
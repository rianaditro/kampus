import asyncio
import aiohttp
import time

""""
python >= 3.7
"""

"""simplest sample of async code vs normal code"""
# normal tasks
def counting(numbers:int=5):
    print("program started")
    for i in range(numbers):
        print(f"counting: {i}")
        time.sleep(1)
    print("program ended")

# async tasks
async def counting_async_1(numbers:int=5):
    for i in range(numbers):
        await asyncio.sleep(1)
        # time.sleep(1) # this will block the main thread
        print(f"Async Task 1 - Iteration {i + 1}")

async def counting_async_2(numbers:int=5):
    for i in range(numbers):
        await asyncio.sleep(1.5)
        # await time.sleep(1.5) """await only for courtine, future, async function or async task"""
        print(f"Async Task 2 - Iteration {i + 1}")

async def counting_async():
    print("program started")
    await asyncio.gather(counting_async_1(5), counting_async_2(5))
    """ scheduling multiple coroutines to run concurrently. """

    print("program ended")

def basic_example():
    counting()
    print("======Next Program======")
    asyncio.run(counting_async()) #running coroutine

"""this blocks end here"""

"""TO DO: creating tasks"""

if __name__ == "__main__":
    # #simplest sample of async code vs normal code
    # basic_example()

    # # Which one is coroutine?
    # print(type(counting_async())) # <class 'coroutine'>
    # print(counting_async()) # <coroutine object counting_async at 0x7f9e0c9b7f40>
    """ 
    Coroutine objects are created using the async keyword.
    Coroutines is a special type of function that can be paused and resumed.
    Note that simply calling a coroutine will not schedule it to be executed.
    """
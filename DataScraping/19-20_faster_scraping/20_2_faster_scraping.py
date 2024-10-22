import aiohttp
import asyncio


# Asynchronous function to fetch a single URL
async def fetch_single_page(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        return await response.text()
    
async def fetch_multiple_pages(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(
                session.get(url)
            )
            tasks.append(task)
        return await asyncio.gather(*tasks)

# Asynchronous function to fetch a single URL
async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()

async def run_single_async(url):
    async with aiohttp.ClientSession() as session:
        response = await fetch_page(session, url)
        return response


if __name__ == "__main__":
    url = "https://www.scrapingcourse.com/ecommerce/"

    # response_data = asyncio.run(fetch_single_page(url))

    # print(len(response_data))

    urls = [f"https://www.scrapingcourse.com/ecommerce/?page={i}" for i in range(1, 6)]

    response_data = asyncio.run(fetch_multiple_pages(urls))

    print(len(response_data))
    print(response_data[0])
    print(type(response_data[0]))
    print(response_data[0].status)

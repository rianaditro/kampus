import asyncio
import aiohttp
from bs4 import BeautifulSoup



async def extract_product_links(response_text):
    """ Extract product links from a page """

    soup = BeautifulSoup(response_text, 'html.parser')

    class_name = "woocommerce-LoopProduct-link woocommerce-loop-product__link"
    product_links = soup.find_all('a', class_=class_name)

    return [link['href'] for link in product_links]

async def extract_product_data(response_text):
    """ Extract product name and price from a page """
    soup = BeautifulSoup(response_text, 'html.parser')

    class_name = "summary entry-summary"
    product_data = soup.find('div', class_=class_name)

    name = product_data.find('h1').text
    price = product_data.find('p', class_='price').text

    data = {
        'name': name,
        'price': price,
    }
    
    print(data)
    return data

async def fetch_page(session, url):
    """ Fetch a single page """
    async with session.get(url) as response:
        print(f"Fetching {url}")
        return await response.text()

async def extract_product(session, product_url):
    """ Get all product data from multiple pages """
    page_content = await fetch_page(session, product_url)
    product_data = await extract_product_data(page_content)

    return product_data

async def fetch_all_pages(session, page_url):
    """ Get product links from multiple pages """
    page_content = await fetch_page(session, page_url)

    product_links = await extract_product_links(page_content)

    tasks = [extract_product(session, link) for link in product_links]
    all_data = await asyncio.gather(*tasks)

    return all_data


async def main():
    """ Main function """

    base_url = "https://www.scrapingcourse.com/"
    urls = [
        f"{base_url}ecommerce/page/{i}" for i in range(1, 6)
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_all_pages(session, url) for url in urls
        ]

        all_product_data = await asyncio.gather(*tasks)
        all_product_data = [item for sublist in all_product_data for item in sublist]

    return all_product_data


if __name__ == "__main__":
    result = asyncio.run(main())

    print(len(result))
    print(result[0])
    print(type(result[0]))
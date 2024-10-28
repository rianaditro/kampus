import requests

from bs4 import BeautifulSoup


def multipage_urls(base_url, total_pages, session):
    for page in range(1, total_pages + 1):
        url = f"{base_url}{page}"  # Construct the URL for each page
        response = session.get(url)  # Make the request to the current page
        print(f"Scraping page {url}...")
        yield response  # Yield the response object

def get_product_urls(response):
    soup = BeautifulSoup(response.text, "html.parser")
    product_links = soup.find_all("div", {"class": "product-item flex flex-col items-center rounded-lg"})
    print(f"Found {len(product_links)} products")
    for link in product_links:
        yield link.find("a").get("href")

def extract_product(url, session):
    response = session.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("h1", {"class": "product_title entry-title"}).text
    price = soup.find("p", {"class": "price"}).text
    return {"title": title, "price": price}


if __name__ == "__main__":
    main_url = "https://www.scrapingcourse.com/pagination/"

    with requests.Session() as session:
        for response in multipage_urls(main_url, 5, session):
            for url in get_product_urls(response):
                result = extract_product(url, session)
                print(result)


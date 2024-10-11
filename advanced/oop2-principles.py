from oop1 import Postman, Article
from bs4 import BeautifulSoup
import requests

""" OOP principles """
"""1. Encapsulation
Encapsulation is the concept of bundling data (attributes) and
methods (functions) that operate on that data within a single class.
Encapsulating the web request process so the user interacts only with
the scraper’s public methods.
"""
class Postman:
    def __init__(self, url):
        self._url = url  # Encapsulated (private) attribute
        self._response = None  # Private attribute

    def send_request(self):
        self._response = requests.get(self._url)
        return self._response.text

    def get_status_code(self):
        if self._response:
            return self._response.status_code
        return None

    def _log_response(self):  # Private method (not intended for external use)
        if self._response:
            print(f"Status Code: {self._response.status_code}")



""" 2. Inheritance
Inheritance allows a class to inherit attributes and methods from another class. 
This helps with code reuse and creating specialized behaviors for new classes.

"""
class Scraper:
    def __init__(self, url):
        self.url = url
        self.postman = Postman(url)

    def parse_page(self):
        html_content = self.postman.send_request()
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup

# The NewsScraper class inherits from the Scraper class
class NewsScraper(Scraper):
    def parse_page(self):
        # Reuse the parent class's parse_page method
        soup = super().parse_page()
        # Specific logic for scraping news articles
        title = soup.find('h1').text
        content = soup.find('div', class_='article-body').text
        return Article(title, content)


""" 3. Polymorphism
Polymorphism allows objects of different classes to be treated as 
objects of a common superclass. 
This enables a method to work with objects of different types and
still behave as expected.
"""
class BlogScraper(Scraper):
    def parse_page(self):
        page_content = self.fetch_page()
        soup = BeautifulSoup(page_content, 'html.parser')
        title = soup.find('h2').text
        body = soup.find('div', class_='blog-body').text
        return {'title': title, 'body': body}

# Function that uses polymorphism
def scrape_data(scraper: Scraper):
    return scraper.parse_page()

# Example usage:
news_scraper = NewsScraper("https://news.example.com")
product_scraper = ProductScraper("https://product.example.com")
blog_scraper = BlogScraper("https://blog.example.com")

# All scrapers work with the same function
print(scrape_data(news_scraper))  # {'title': 'News Title', 'content': 'News content'}
print(scrape_data(product_scraper))  # {'name': 'Product Name', 'price': '99.99'}
print(scrape_data(blog_scraper))  # {'title': 'Blog Title', 'body': 'Blog content'}


""" 4. Abstraction
Abstraction hides the complex implementation details from the user and
exposes only the necessary functionalities. 
This simplifies the interface for the user of the class.
Defining an abstract class for different types of scrapers so that all subclasses follow the same interface
"""
from abc import ABC, abstractmethod

# Abstract class
class BaseScraper(ABC):
    def __init__(self, url):
        self.url = url
        self.postman = Postman(url)

    @abstractmethod
    def parse_page(self):
        pass  # This must be implemented by any subclass

# Concrete subclass for news scraping
class NewsScraper(BaseScraper):
    def parse_page(self):
        page_content = self.postman.send_request()
        soup = BeautifulSoup(page_content, 'html.parser')
        title = soup.find('h1').text
        content = soup.find('div', class_='article-body').text
        return {'title': title, 'content': content}

# Concrete subclass for product scraping
class ProductScraper(BaseScraper):
    def parse_page(self):
        page_content = self.postman.send_request()
        soup = BeautifulSoup(page_content, 'html.parser')
        name = soup.find('h1').text
        price = soup.find('span', class_='price').text
        return {'name': name, 'price': price}


if __name__ == "__main__":
    pass
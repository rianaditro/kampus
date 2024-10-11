"""
Understanding Entity

Start by asking yourself:
- Who am I?
- What am I?
- What can I do?

My name is Rian, I am a human. I can talk, eat, and sleep.

How about the others?

His name is Hanif, he is a human. He can talk, eat, and sleep.

What we know now?

- There are two human: Rian and Hanif
- Human shared the same capabilities: talk, eat, and sleep
- Each human has its different name.

We can say:
- I am a human named Rian. or ===> myself = Human("Rian")
- Then we explain human ===> Human(name) can do: eat, sleep, talk

myself=Human
|name:Rian  |
|can:       |
| - eat     |
| - sleep   |
| - talk    |

In programming we can translate this into:
- Rian is an object
- Hanif is another object
- Human is a class
- Name is an attribute
- Talk is a method


class Human:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def talk(self):
        print(f"{self.name} is talking")


What are entities in the data scraping?
What we do when we do data scraping?

1. We request the url
2. We get the response
3. We parse the response
4. We extract the data

In real-life scenario it looks like when we sending mails:

1. We give a mail to be send by a postman
2. The postman send the mail and send back the response mail
3. We read the mail
4. We get the information from the mail

Who or what object involved here?
1. Postman:
    - sending & receiving our mail based on our address
2. Mail:
    - contains all the message and data
3. Mail sender:
    - put our mail in mail box
    - receive our mail response
    - read our mail

In data scraping, the involved object are:
1. Requester: 
    - send our request
2. Response:
    - contains all data
3. Scraper:
    - trigger the request
    - parse our response
"""

import requests
from bs4 import BeautifulSoup


class Postman:
    def __init__(self, url):
        self.url = url

    def send_request(self):
        response = requests.get(self.url)
        return response.text  # Return HTML content


class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Content: {self.content[:100]}...")  # Display first 100 characters


class Scraper:
    def __init__(self, url):
        self.url = url
        self.postman = Postman(url)

    def parse_page(self):
        html_content = self.postman.send_request()
        soup = BeautifulSoup(html_content, 'html.parser')
        # Extract title and content
        title = soup.find('h1').text.strip()
        content = soup.find('small').text.strip()
        return Article(title, content)


# Usage example:
scraper = Scraper("https://books.toscrape.com/")
article = scraper.parse_page()
article.display_info()
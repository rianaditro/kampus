---
marp: true
author: Rian Adi
theme: gaia
backgroundColor: white
footer: Data Scraping | rianaditro
---
<!-- _backgroundColor: grey -->
<!-- _color: white -->
<!-- _paginate: skip -->
<br>
<br>
<br>
<br>

# Object Oriented Programming
KELAS DATA SCRAPING
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

---
<!-- paginate: true -->
## Introduction
Object-Oriented Programming (OOP) is a programming paradigm that helps structure your code into reusable pieces by organizing it around objects, which represent **entities in the real world.** In Python data scraping, using OOP can make your code more **modular, reusable, and easier to maintain.**

Instead of writing separate functions or large procedural blocks, you organize the scraping process into classes that model real-world entities.

---
## Key Concepts
1. Class: A blueprint for creating objects. It **defines the properties and methods** of the object.
2. Object: An instance of a class. It represents one specific "thing" **created from the class.**
3. Attributes: Variables that **store data about the object**. They are defined inside the class.
4. Methods: Functions that define the **behavior of an object**. They are defined inside the class and usually use the object’s attributes.

---
## Class and Object
```python
class Dog:
    def __init__(self, name, breed): # Magic method
        self.name = name    # Class attribute
        self.breed = breed  # Class attribute
    
    def bark(self):         # # Class methode
        return f"{self.name} says woof!"

my_dog = Dog("Buddy", "Golden Retriever") # Create an object (instance of Dog)

# Access attributes
print(my_dog.name)  # Outputs: Buddy
print(my_dog.breed)  # Outputs: Golden Retriever

# Call the method
print(my_dog.bark())  # Outputs: Buddy says woof!
```
---
## Scraping with Object
```python
driver = webdriver.Chrome() # Creating chrome browser instance/object

driver.get("https://example.com") # Navigate to a website using webdriver method

html = driver.page_source # Get the full HTML of the page from webdriver atribute
```

```python
class WebDriver:
  def __init__(self):
    self.page_source = None
  
  def get(self, url):
    self.page_source = "<html><body><h1>Hello World!</h1></body></html>"
```

---
## Task
From class WebDriver that we just created try improve the class capability like real Selenium WebDriver instance. For example, add a method to get the current URL. You can add customize features as you like.

**Challenge**
Create a class that replicate the Requests library. Remember when you run **requests.get()** it return a **response object**.

---
## OOP Principles
1. Encapsulation
Keeps the details hidden inside the object, and only allows interaction with what is necessary (like using a car without knowing how the engine works).
`def _log_response(self): something`
2. Inheritance
Allows new objects to inherit features from existing ones (like children inheriting traits from their parents).
`class Scraper: something`
`class NewsScraper(Scraper): something`

---
3. Polymorphism
Polymorphism allows objects of different classes to be treated as objects of a common superclass. 
This enables a method to work with objects of different types and still behave as expected. 
```python
class BlogScraper(Scraper):
    def parse_page(self):

# Function that uses polymorphism
def scrape_data(scraper: Scraper):
    return scraper.parse_page()
  
blog_scraper = BlogScraper("https://blog.example.com")
print(scrape_data(blog_scraper))
```

---
4. Abstraction
Abstraction simplifies the interface for the user of the class. Defining an abstract class for different types of scrapers so that all subclasses follow the same interface.
```python
from abc import ABC, abstractmethod

class BaseScraper(ABC):
    @abstractmethod
    def parse_page(self):
        pass  # This must be implemented by any subclass

class NewsScraper(BaseScraper):
    def parse_page(self): 

class ProductScraper(BaseScraper):
    def parse_page(self):
```

---
## Understanding Entities
Entities represent the **real-world concepts** or things that you want to model in your code.
In the context of OOP, an entity is simply a real-world object or concept that you want to model in your program. For example:
- In a store: An entity could be a Product, Customer, or Order.
- In a game: An entity could be a Player, Enemy, or Weapon.
<!--In web scraping: An entity could be a Scraper, Page, or Data.-->
Once you identify what entities you are dealing with, you can create classes to represent them in your program.

---
## Simple Program Example: Library System
Imagine you’re creating a program that allows users to check out books from a library. 
1. Understand the Problem Domain
The library have many books and user can borrow or return the books.
2. Identify Key Entities (Objects)
The main entity are books and user.

---
3. Define the Object’s Responsibilities (Attributes and Methods)

Book Object:
- Attributes:
  - title (name of the book)
  - author (author of the book)
  - available (whether the book is available for checkout/borrowed)
- Methods:
  - checkout(): Marks the book as checked out.
  - return_book(): Marks the book as returned.

---
User Object:
- Attributes:
  - name (name of the user)
  - borrowed_books (list of books the user has borrowed)

- Methods:
  - borrow_book(book): Allows the user to borrow a book.
  - return_book(book): Allows the user to return a book.

---
4. Create the Classes and Implement the Methods
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # By default, the book is available

    def checkout(self):
        if self.available:
            self.available = False
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_book(self):
        self.available = True
        print(f"{self.title} has been returned.")
```

---
```python
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.checkout()
            self.borrowed_books.append(book)
        else:
            print(f"{book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"{self.name} hasn't borrowed {book.title}.")

```

---
## Task
After defining book and user class, its time to create the objects and run the program to simulate a real library.

**Challenges**
Try to create a scraper program implement OOP.

---
## Learn More
RWID regular class
https://www.youtube.com/watch?v=TnBohKSKxuo

Object Oriented Programming (OOP) In Python - Beginner Crash Course
https://www.youtube.com/watch?v=-pEs-Bss8Wc

OOP in visualization
https://pythontutor.com/visualize.html#mode=edit

---
## Discover Advanced Topic
Python Design Patterns Tutorial
https://www.geeksforgeeks.org/python-design-patterns/

How to call a async function contained in a class?
https://stackoverflow.com/questions/42009202/how-to-call-a-async-function-contained-in-a-class

---
<!-- _backgroundColor: grey -->
<!-- _color: white -->
<!-- _paginate: false -->
<br>
<br>
<br>
<br>

# Thank you
Any Question?
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024


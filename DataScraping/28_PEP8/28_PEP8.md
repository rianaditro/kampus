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

# PEP 8 - Style Guide for Python Code
KELAS DATA SCRAPING
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

---
<!-- paginate: true -->
## Introduction
PEP 8 is the Python Enhancement Proposal that provides guidelines and best practices for writing clean, readable, and consistent Python code. It is essentially the official style guide for Python code, helping developers write code that is easy to understand and maintain across different projects and teams.

---
## Key Aspects of PEP 8
1. Indentation: Use **4 spaces** per indentation level.
2. Line Length: Limit all lines to a maximum of **79 characters.**
3. Blank Lines: Use **2 blank lines** before top-level functions and class definitions, and 1 blank line inside functions to separate logic.
4. Imports: **Group imports into three categories**: standard library imports, third-party imports, and local imports. Import each module in separate lines.

---
5. Whitespace: **Avoid extra spaces** inside parentheses, brackets, or around operators.
6. Naming Conventions:
    - Variables, functions: Use snake_case.
    - Classes: Use CamelCase.
    - Constants: Use ALL_CAPS.
7. Comments and Docstrings: Use comments to **explain why certain decisions were made**, and use docstrings for functions, methods, and classes to **describe their purpose.**

---
## Why We Should?
Although following the style guide isn't mandatory as long as your program works, it's beneficial to implement it because it can impact your career. It improves 
1. Readability : Make code to easier to read and understand.
2. Collaboration : It reduces confusion and miscommunication when working as a team.
3. Professionalism : This can enhance your reputation as a professional, leading to more opportunities, repeat business, and recommendations from satisfied clients.

---
## Evaluate Code Quality with Flake8
Flake8 is a tool for enforcing Python style guidelines (PEP 8), detecting errors, and identifying code complexity issues. For data scraping, writing clean, readable, and efficient code is essential, and Flake8 helps maintain this standard.

---
## Running Flake8
Example code your_script.py
```python
import requests
from bs4 import BeautifulSoup

def scrape():
  url="https://example.com"
  response=requests.get(url)
  if response.status_code==200:
    soup=BeautifulSoup(response.text,"html.parser")
    title=soup.find("h1").text
    print (title)
scrape()
```

---
Install flake8: If you haven't installed flake8 yet, you can do so by running:
```bash
pip install flake8
```
Run flake8: To check the Python script for style violations, run:
```bash
flake8 your_script.py
```
---
Output
```bash
your_script.py:5:3: E111 indentation is not a multiple of four
your_script.py:6:6: E225 missing whitespace around operator
your_script.py:7:6: E225 missing whitespace around operator
your_script.py:8:5: E231 missing whitespace after ','
your_script.py:9:5: E701 multiple statements on one line (colon)
your_script.py:10:5: E201 whitespace after '('
```
This give you instruction on how to improve your code.

---
## Task
Check your code using flake8, how many improvement suggestion you have?

---
## Learn More
PEP 8 – Style Guide for Python Code
https://peps.python.org/pep-0008/

Automate Code Testing
https://medium.com/python-in-plain-english/efficient-django-testing-implementing-github-actions-for-automation-on-youngfounder-id-530833756336

---
## Discover Advanced Topic
Publishing Python Program to PyPI using Poetry
https://medium.com/@rianaditro/publishing-python-program-to-pypi-using-poetry-eb4685a73044

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


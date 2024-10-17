---
marp: true
author: Rian Adi
theme: gaia
backgroundColor: white
paginate: true
---
<!-- _backgroundColor: grey -->
<!-- _color: white -->
<!-- _paginate: false -->

# KAMPUS R

---
# Python Data Scraping Materials

Welcome to the **Python Data Scraping Materials** repository! This repository is dedicated to providing structured Python examples and materials that will guide you through learning data scraping techniques. Whether you're a beginner or an experienced developer looking to expand your scraping skills, you'll find valuable content here.

---

# Table of Contents
1. [Overview](#overview)
2. [Requirements](#requirements)
3. [How to Use](#how-to-use)
4. [Content Overview](#content-overview)
    - [Basic](#basic)
    - [Intermediate](#intermediate)
    - [Advanced](#advanced)
5. [Contribution Guidelines](#contribution-guidelines)
6. [License](#license)

---
# Overview
This repository contains various Python scripts aimed at teaching you different techniques for **web scraping**. The goal is to cover everything from basic HTML scraping to advanced methods, such as handling dynamic content, managing cookies, and bypassing scraping restrictions.

Web scraping is a technique for extracting data from websites by using scripts to automate the process. It is widely used for data collection in research, business analysis, and many other fields.

---
# Requirements
To run the Python scripts provided in this repository, you will need the following:
- Python 3.10 or later
- The list of python package in the requirements.txt
You can install these dependencies by running the following command:
```bash
pip install -r requirements.txt
```
---
# Content Overview
The repository is structured to cover various aspects of data scraping. Below is an overview of the content:

## Basic
- **Requests**: Send requests till get blocked.
  - Relevant File: [`beginner-intro-requests.py`](./basics/beginner-intro-requests.py)

- **Continue vs Pass**: Understanding how pass and continue keyword worked.
  - Relevant File: [`continue-vs-pass.py`](./basics/continue-vs-pass.py)

## Intermediate
- **Regex**: Regex daily tasks
  - Relevant File: [`intermediate-regex.py`](./intermediate/intermediate-regex.py)

- **Yield**: use generator to save memory
  - Relevant File: [`yield-in-action.py`](./intermediate/yield-in-action.py)

- **Selenium**: scraping list of urls and image click automation, waiting strategy
  - Relevant File: [`selenium-req.py`](./intermediate/selenium-req.py)
  - Relevant File: [`selenium-auto.py`](./intermediate/selenium-auto-click.py)
  - Relevant File: [`selenium-waitelement.py`](./intermediate/selenium-waitelement.py) 

- **Selenium: login form**: using request post payload and selenium input form to automate login.
  - Relevant File: [`login-auth.py`](./intermediate/login-auth.py)

- **Speed Up Scraping**: Comparing Threading, Connection pooling, and asynchronous in time consumed.
  - Relevant File: [`speed-up-scraping-method.py`](./intermediate/speed-up-scraping-method.py)

## Advanced
- **OOP**: Understanding entity, object and OOP principles in data scraping
  - Relevant File: [`oop1.py`](./advanced/oop1.py)
  - Relevant File: [`oop2-principles.py`](./advanced/oop2-principles.py)

- **Asynchronous**: Deep understand on asyncio.
  - Relevant File: [`learn-asyncio.py`](./advanced/learn-asyncio.py)

- **FastAPI**: Simple fastapi for scraping.
  - Relevant File: [`advanced-fastapi.py`](./advanced/advanced-fastapi.py)
---
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

# Scraping with Authentication
KELAS DATA SCRAPING
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

---
<!-- paginate: true -->
## Introduction
When scraping data from websites, you will often encounter authentication mechanisms that protect content behind login forms or API credentials.

```python
if user.logged_in: print("Success!")
```

---
## Automate Login vs Payload
**Automate Login using Selenium**
```python
driver = webdriver.Chrome(options=options)
driver.get(url)

username = driver.find_element(By.ID, "email")
username.send_keys("admin@example.com")

password = driver.find_element(By.ID, "password")
password.send_keys("password")

submit_button = driver.find_element(By.ID,"submit-button")
submit_button.click()
```
---
**Login using Requests Payload**
```python
payload = {
            "email": "admin@example.com",
            "password": "password",
        }

response = requests.post(url, data=payload)
```
---
## Class Activity
Create an account on https://webapi.bps.go.id/developer/ then automate your login process using both of selenium and requests payload.

---
## Learn More
Join us on this self-study journey! Click the link below to get started.
- [Scraping Websites With **CSRF Token Authentication** or **WAF-Protected Websites**](https://www.zenrows.com/blog/web-scraping-login-python)

---
## Discover Advanced Topic
Master this advanced topic and supercharge your skills.
- [Can you scraping a website that use **OAuth 2.0** like Google?](https://testdriven.io/blog/oauth-python/)

---
## Homework Assignment
Find any website that using login and try login using the best approach!

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


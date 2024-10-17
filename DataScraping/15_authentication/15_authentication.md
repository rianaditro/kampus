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

# Authentication
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

---
## What happens when we login to a website?
- When you **submitting your credentials**, the website's server verifies your identity.
- If the login is successful, the server sends back a **cookie** to your browser and **saved to memory**. This cookie may contain session information, like a session ID or authentication token.
- On subsequent requests, the browser automatically **sends the stored cookies back to the server** with each request.
- As long as the cookie is valid, you can navigate the website **without needing to log in again.**

---
## How we submit the login credentials?
Normally, we do this by clicking on the form, typing our username and password, and then clicking the login button, right? Now, let's try this using Selenium.

For this learning purpose we will try to login to https://www.scrapingcourse.com/login

---
## Login using Selenium
```python
options = Options()
options.add_argument("--start-maximized")

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
## Login using Requests
Can we login using Requests? How to input the email and password if we dont see the screen?

Identify where to put all the credentials:

- Find where form is sending the data
- Find how the data wrapped

---
## Login using Requests
```python
payload = {
        "email": "admin@example.com",
        "password": "password",
    }

response = requests.post(url, data=payload)
```
---
## Task
Create an account on https://webapi.bps.go.id/developer/ or use this account:
- email: razapoetra@gmail.com
- password: e@muPTFPxhTazh2

Login and then go to https://webapi.bps.go.id/developer/user/profile and extract user information.

Remember: the https://webapi.bps.go.id/developer/user/profile only accessible by logged-in user only. Find out how to **stay logged-in between request.**

---
## Learn More
Learn more on how to Scraping Websites With **CSRF Token Authentication** for Login and Scraping Behind the Login on **WAF-Protected Websites** here:
https://www.zenrows.com/blog/web-scraping-login-python

## Challenges
Can you scraping a website that use **OAuth 2.0** like Google?
https://testdriven.io/blog/oauth-python/
https://github.com/oauthlib/oauthlib
https://github.com/requests/requests-oauthlib

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


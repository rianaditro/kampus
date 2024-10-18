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

# Selenium
KELAS DATA SCRAPING
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

---
<!-- paginate: true -->
## Introduction
Selenium stands out from other scraping tools  because it **interacts with a real browser**. This makes it particularly useful for websites that rely heavily on JavaScript, AJAX, or dynamic content loading. Selenium can handle:
- Pages that load content dynamically with JavaScript.
- Interaction with forms, buttons, and scroll events.
- Handling cookies, authentication, and pop-ups.

---
## Creating a Browser Instance
```python
from selenium import webdriver

# Creating chrome browser instance/object
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://example.com")

# Get the full HTML of the page
html = driver.page_source

# Closing browser after use
driver.quit()
```

---
## Set options for Chrome
```python
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--start-maximize") # fullsize window

options.add_argument("--blink-settings=imagesEnabled=false") # disable images

options.add_argument("--ignore-certificate-errors") # ignore certificate errors

options.add_argument("--disable-notifications") # disable notifications

options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"]) # disable pop-up

options.add_argument("--headless")  # This runs Chrome in headless mode (no UI)
options.add_argument("--disable-gpu")  # Disables GPU hardware acceleration (useful in headless mode)

driver = webdriver.Chrome(options=options)
```

---
## Task
Try to navigate through a list of URLs. How you approach this? Is a new browser instance created for every URL visited? Can you make it **use same instance** to make it more efficient?

**Quiz**
What happens if we dont add `driver.quit()` ? Why we need it?

---
## Element in Selenium
In Selenium, an element refers to any individual part of the web page's HTML document that you can interact with. These elements are objects such as buttons, text fields, links, images, or any other **HTML tag on the page**. Selenium allows you to **locate, interact with, and extract data** from these elements using various methods.

---
## Selectors and Element Interaction
**Locating Elements Using `By`**
```python
element = driver.find_element(By.ID, "element-id")  # Finds element by ID

element = driver.find_element(By.CLASS_NAME, "element-class")  # Finds element by class name

element = driver.find_element(By.NAME, "element-name")  # Finds element by name attribute

element = driver.find_element(By.XPATH, "//tagname[@attribute='value']")  # Find by XPath

element = driver.find_element(By.CSS_SELECTOR, ".class-name > tagname")  # Find by CSS selector
```

---
**Working with Multiple Elements**
```python
elements = driver.find_elements_by_class_name("common-class")
for elem in elements:
    print(elem.text)
```
**Interact with Web Elements**
```python
element = driver.find_element(By.NAME, "search")  # Locate element by name attribute

print("Text of the element:", element.text)  # This prints the visible text inside the element

placeholder_text = element.get_attribute("placeholder")
print("Placeholder of the input field:", placeholder_text) # Get an attribute from the element (e.g., 'placeholder' or 'value')

element.clear()  # Clears any existing text
element.send_keys("Selenium WebDriver")  # Types 'Selenium WebDriver' into the input field

element.submit()  # Submits the form containing the input field
# If this was a button, you could use element.click()
```

---
## Task
Visit an ecommerce website, find your desired product and get the image URL of the product. There should be more than one image. Click on the image to get the full image resolution.

**Challenge**
Download the image into a folder named product name. Add a validation to make sure if the image already downloaded it's not re-downloading the image again.

---
## Waiting Strategy
When automating web tasks or scraping data with Selenium, elements on a webpage may not be immediately available due to delays in loading, JavaScript execution, or dynamic content rendering. To ensure that your code interacts with elements only when they are ready, Selenium provides waiting strategies.

---
**1. Implicit Wait**
Implicit Wait sets a default wait time for the WebDriver to poll the DOM for elements before throwing a NoSuchElementException.

```python
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to be present
```
**2. Explicit Wait** (clickable, visible, presence)
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID"submit-button")))

element.click()
```

---
## Task
Visit https://sturents.com/s/newcastle/newcastle?ne=54.9972%2C-1.5544&sw=54.9546%2C-1.6508 notice how the page still rendering the data. Use waiting strategy to find the data and make sure the amount of data in selenium is equal to our real browser.

---
## Learn More
Fluent wait in selenium
https://www.youtube.com/watch?v=L9wThGzzbMA

How to handle iFrame in Selenium
https://www.browserstack.com/guide/handling-frames-in-selenium

Selenium is fairly easily detected, especially by all major anti-bot providers (Cloudflare, Akamai, etc).
https://stackoverflow.com/a/68895614/23418303

---
## Discover Advanced Topic
Playwright
https://playwright.dev/python/docs/intro

Hrequests
https://github.com/daijro/hrequests

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


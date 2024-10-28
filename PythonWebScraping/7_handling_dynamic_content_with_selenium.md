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

# Handling Dynamic Content with Selenium
KELAS DATA SCRAPING
<!-- <br> -->
<br>
<br>
<br>

Kampus Remote Worker Indonesia | 2024

---
<!-- paginate: true -->
## Selenium
Selenium stands out from other scraping tools  because it **interacts with a real browser**. This makes it particularly useful for websites that rely heavily on JavaScript, AJAX, or dynamic content loading. Selenium can handle:
- Pages that load content dynamically with JavaScript.
- Interaction with forms, buttons, and scroll events.

```python
from selenium import webdriver
```

---
## Browser Instance
**Creating a Browser Instance**
```python
from selenium import webdriver

driver = webdriver.Chrome() # Creating chrome browser instance/object

driver.get("https://example.com") # Navigate to a website

html = driver.page_source # Get the full HTML of the page

driver.quit() # Closing browser after use
```
---
**Set Options for Chrome**
```python
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--start-maximize")

options.add_argument("--blink-settings=imagesEnabled=false")

options.add_argument("--ignore-certificate-errors")

options.add_argument("--disable-notifications")
options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])

options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
```
---
## Class Activity
Try to navigate through a list of URLs. How you approach this? Is a new browser instance created for every URL visited? Can you make it **use same instance** to make it more efficient?

---
## Element in Selenium
In Selenium, an element refers to any individual part of the web page's HTML document that you can interact with. These elements are objects such as buttons, text fields, links, images, or any other **HTML tag on the page**. Selenium allows you to **locate, interact with, and extract data** from these elements using various methods.

```python
<class WebElement>
```
---
**Locating Elements Using `By`**
```python
from selenium.webdriver.common.by import By

element = driver.find_element(By.ID, "element-id")  

element = driver.find_element(By.CLASS_NAME, "element-class")  

element = driver.find_element(By.NAME, "element-name")  

element = driver.find_element(By.XPATH, "//tagname[@attribute='value']")  

element = driver.find_element(By.CSS_SELECTOR, ".class-name > tagname")  
```
---
**Interact with Web Elements**
```python
element = driver.find_element(By.NAME, "search")  
# Locate element by name attribute

print("Text of the element:", element.text)  
# This prints the visible text inside the element

placeholder_text = element.get_attribute("placeholder")
print("Placeholder of the input field:", placeholder_text) 
# Get an attribute from the element (e.g., 'placeholder' or 'value')

element.clear()  
# Clears any existing text
element.send_keys("Selenium WebDriver")  
# Types 'Selenium WebDriver' into the input field

element.submit()  # Submits the form containing the input field
# If this was a button, you could use element.click()
```
---
## Class Activity
Scrape image of product from a shop in Tokopedia. Trigger image click to get the image in full size and download all the images.

**Challenge**: Add a functionality to avoid the re-download of the entire image files when the script is executed a second time.

---
## Waiting Strategy
When automating web tasks or scraping data with Selenium, elements on a webpage may not be immediately available due to delays in loading, JavaScript execution, or dynamic content rendering. To ensure that your code interacts with elements only when they are ready, Selenium provides waiting strategies.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```
---
**Implicit Wait**
```python
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to be present
```
**Explicit Wait (clickable, visible, presence)**
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.ID"submit-button")))

element.click()
```
---
## Class Activity
Visit https://sturents.com/s/newcastle/newcastle?ne=54.9972%2C-1.5544&sw=54.9546%2C-1.6508 and notice how the page is still rendering the data. Use wait strategy to find the data and make sure the amount of data in selenium is equal to our real browser.

---
## Learn More
Join us on this self-study journey! Click the link below to get started.
- [Fluent wait in selenium](https://www.youtube.com/watch?v=L9wThGzzbMA)
- [How to handle iFrame in Selenium](https://www.browserstack.com/guide/handling-frames-in-selenium)

---
## Discover Advanced Topic
Master this advanced topic and supercharge your skills.
- [Selenium is fairly easily detected](https://stackoverflow.com/a/68895614/23418303)

---
## Homework Assignment
Create a script automate form submission using selenium to https://demoqa.com/automation-practice-form and take a screenshot!

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


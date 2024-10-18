from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# List of URLs to scrape
urls = [
    "https://quotes.toscrape.com/page/1/",
    "https://quotes.toscrape.com/page/2/",
    "https://quotes.toscrape.com/page/3/"
]

# Step 1: Initialize the Selenium WebDriver (for example, Chrome)
driver = webdriver.Chrome()  # Ensure the chromedriver executable is in your PATH

html_list = []
# Example of WebDriverWait
for url in urls:
    driver.get(url)
    
    # Wait until a specific element (e.g., body) is present before getting page source
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    html_content = driver.page_source

    page_data = {
        "url": url,
        "content-length": len(html_content)
    }

    html_list.append(page_data)
driver.quit()

print(html_list)

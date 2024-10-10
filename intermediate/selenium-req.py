from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# List of URLs to scrape
urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

# Step 1: Initialize the Selenium WebDriver (for example, Chrome)
driver = webdriver.Chrome()  # Ensure the chromedriver executable is in your PATH


# Example of WebDriverWait
for url in urls:
    driver.get(url)
    
    # Wait until a specific element (e.g., body) is present before getting page source
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    html_content = driver.page_source
    print(f"Scraped HTML content from {url}:{len(html_content)} characters")

driver.quit()

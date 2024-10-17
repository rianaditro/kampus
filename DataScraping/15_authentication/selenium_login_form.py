import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def login_selenium(url: str):
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    username = driver.find_element(By.ID, "email")
    username.send_keys("admin@example.com")

    time.sleep(2)
    password = driver.find_element(By.ID, "password")
    password.send_keys("password")

    time.sleep(2)
    submit_button = driver.find_element(By.ID,"submit-button")
    submit_button.click()

    return driver 


if __name__ == "__main__":
    url = "https://www.scrapingcourse.com/login"

    driver = login_selenium(url)
    print(driver.title)
    print(f"Content length: {len(driver.page_source)}")
    
    time.sleep(2)
    driver.close()


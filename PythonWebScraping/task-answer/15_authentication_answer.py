import requests
import time
from bs4 import BeautifulSoup

from selenium import webdriver #web driver instance
from selenium.webdriver.common.keys import Keys # keyboard input
from selenium.webdriver.chrome.options import Options # options for variant of browser styles
from selenium.webdriver.common.by import By # css locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_req():
    url = "https://webapi.bps.go.id/developer/login"

    session = requests.Session()

    payload = {
        "LoginForm[username]": "razapoetra@gmail.com",
        "LoginForm[password]": "e@muPTFPxhTazh2",
        "yt0": "Login",
    }

    response = session.post(url, data=payload)
    if response.status_code == 200:
        print("Login request successful")

        response = session.get("https://webapi.bps.go.id/developer/user/profile")
        html = response.text

        soup = BeautifulSoup(html, "html.parser")
        my_name = soup.find("table", {"id": "yw0"}).find("td").text
        print(my_name)
    else:
        print("Login failed")

def login_sel():
    url = "https://webapi.bps.go.id/developer/login"

    driver = webdriver.Chrome()
    driver.get(url)

    username = driver.find_element(By.ID, "LoginForm_username")
    username.send_keys("razapoetra@gmail.com")

    time.sleep(2)

    password = driver.find_element(By.ID, "LoginForm_password")
    password.send_keys("e@muPTFPxhTazh2")

    time.sleep(2)

    login = driver.find_element(By.NAME,"yt0")
    login.click()

    driver.get("https://webapi.bps.go.id/developer/user/profile")
    print("Login selenium successful")

    wait =  WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table#yw0")))

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    my_name = soup.find("table", {"id": "yw0"}).find("td").text
    print(my_name)

if __name__ == "__main__":
    login_req()
    # login_sel()
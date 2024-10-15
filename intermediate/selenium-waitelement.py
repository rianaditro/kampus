from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def get_driver():
    # initiate web options
    options = Options()

    # fullsize window
    options.add_argument("start-maximized")

    driver = webdriver.Chrome(options=options)
    return driver

def get_html(driver, url, save: bool = False):
    # implicit wait
    # driver.implicitly_wait(10)

    driver.get(url)
    
    # explicit wait
    # maxWait = 10
    # wait =  WebDriverWait(driver, maxWait)
    # # wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'new--search-result-item')))
    # # wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'new--search-result-item')))
    # wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'new--search-result-item')))

    try:
        elements = driver.find_elements(By.CLASS_NAME, "new--search-result-item")
        print("Element found")

        print(len(elements))
        # driver.execute_script("arguments[0].scrollIntoView(true);", elements[-1])

    except:
        elements = []
        print("Element not found")

        return
    
    html = driver.page_source

    if save:
        with open("result.html", "w") as f:
            f.write(html)
    return html


if __name__ == "__main__":
    url = "https://sturents.com/s/newcastle/newcastle?ne=54.9972%2C-1.5544&sw=54.9546%2C-1.6508"

    driver = get_driver()
    html = get_html(driver, url)
    
import requests

from bs4 import BeautifulSoup


def login_req(url:str, payload:dict):
    response = requests.post(url, data=payload)

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.text

    print(title)
    print(f"Content length: {len(html)}")


if __name__ == "__main__":
    url = "https://www.scrapingcourse.com/login"

    payload = {
        "email": "admin@example.com",
        "password": "password",
    }

    login_req(url, payload)
    
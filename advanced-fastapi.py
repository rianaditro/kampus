from typing import Union
from fastapi import FastAPI
from bs4 import BeautifulSoup as bs
import requests


app = FastAPI()

@app.get("/")
def read_root():
    return {"status code": 200,
            "message": "ok"}

@app.get("/newsList/{site}")
def read_item(site:str = "detik"):
    if site == "detik":
        site = "https://news.detik.com/indeks"
        
    # get html
    response = requests.get(site).text

    # parsing html
    soup = bs(response, "html.parser")
    list_content = soup.find("div", {"class": "grid-row list-content"})
    list_content = list_content.find_all("h3", {"class": "media__title"})

    # container for list of news data
    news = []

    for i, content in enumerate(list_content):
        data = {
            "id": i,
            "title": content.text.replace('"', '').strip(),
            "link": content.find("a").get("href")
        }

        news.append(data)

    result = {
        "status code": 200,
        "message": "ok",
        "count" : len(news),
        "data": news
    }
    return result
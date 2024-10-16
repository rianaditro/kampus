from typing import Union
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from bs4 import BeautifulSoup as bs
import requests, pandas, io


app = FastAPI()

@app.get("/")
def read_root():
    return {"status code": 200,
            "message": "ok"}

@app.get("/newsList/")
def read_item(site:str = "detik", download: bool = False):
    if site == "detik":
        site = "https://news.detik.com/indeks"
        
    # get params
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

    # non-download
    response = None

    # download as csv
    if download:
        csv_file = pandas.DataFrame(news)

        # create a file object, waiting for file
        stream = io.StringIO()
        # response = StreamingResponse(stream, media_type="text/csv")

        csv_file.to_csv(stream, index=False)
        file_path = stream.getvalue()
        response = StreamingResponse(file_path, media_type="text/csv", status_code=200)

        stream.close()

        return response

    result = {
        "status code": 200,
        "methode": "GET",
        "message": "OK",
        "count" : len(news),
        "download": download,
        "data": news
    }
    return result
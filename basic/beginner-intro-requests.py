import requests
from fake_useragent import UserAgent

counter = 0

url = "https://api.github.com/users/octocat" #limit at 60 requests

# url = 'https://gamefaqs.gamespot.com/' #error 400

url = "https://httpbin.org/ip"

ua = UserAgent()
headers = {"User-Agent": ua.random}

proxy = {
    "http":"http://101.128.78.202:32650",
}

while True:
    response = requests.get(url,proxies=proxy)
    if response.status_code != 200:
        print(f"{url} limit requests is {counter}: Error code {response.status_code}")
        break
    counter += 1
    print(f"{counter} - {response.status_code}")
    print(response.text)

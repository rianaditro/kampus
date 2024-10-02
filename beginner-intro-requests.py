import requests

counter = 0

url = "https://api.github.com/users/octocat"

while True:
    response = requests.get(url)
    if response.status_code != 200:
        print(f"{url} limit requests is {counter}: Error code {response.status_code}")
        break
    counter += 1
    print(f"{counter} - {response.status_code}")
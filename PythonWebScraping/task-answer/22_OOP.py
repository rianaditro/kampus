from typing import Any
import requests


url = "https://httpbin.org/ip"

response = requests.get(url)

# print(requests)
# print(type(response))
# print(response) # representation of object
# print(response.status_code)

# print("========end of code========")


class ResponseCopy:
    def __init__(self, status_code: int = None, text: str = None):
        self.status_code = status_code
        self.text = text

    def __repr__(self) -> str:
        return f"<ResponseCopy [{self.status_code}]>"

class RequestCopy:
    def get(self, url: str) -> ResponseCopy:
        status_code = 200
        text = "<html><body><h1>Hello, World!</h1></body></html>"
        return ResponseCopy(status_code, text)
    
request_copy = RequestCopy()
response_copy = request_copy.get("https://example.com")

# print(request_copy)
# print(type(response_copy))
# print(response_copy) # representation of object
# print(response_copy.status_code)


class ResponseInherit(ResponseCopy):
    def __init__(self, status_code: int = 200, text: str = None):
        super().__init__(status_code, text)
        self.headers = {"Content-Type": "text/html"}

response_inherit = ResponseInherit()
print(response_inherit)
import requests

class APIClient:
    def __init__(self):
        self.base_url = "https://httpbin.org"

    def send_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, **kwargs)
        return response
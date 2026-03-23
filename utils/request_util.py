import requests

class RequestUtil:
    def __init__(self, base_url=""):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()

    def request(self, method, url, **kwargs):
        # 如果传入了 base_url 就拼接，否则默认请求 httpbin
        full_url = f"{self.base_url}{url}" if self.base_url else f"https://httpbin.org{url}"
        
        # 统一处理请求异常，保证测试不因为网络波动直接崩溃
        try:
            resp = self.session.request(method.upper(), full_url, **kwargs)
            return resp.json()
        except Exception as e:
            return {"status": "Error", "msg": str(e), "text": "请求失败"}
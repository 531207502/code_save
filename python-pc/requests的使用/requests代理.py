import requests
url = "https://httpbin.org/ip"
proxy = {"http":"115.221.211.246:9999"}
resp=requests.post(url,proxies=proxy)
print(resp.content.decode("utf-8"))
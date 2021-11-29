import requests
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
# r = requests.get('http://httpbin.org/headers',headers=headers)
# print(r.json())
# print(r.raise_for_status())

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/username/password')
# r = s.get("http://httpbin.org/cookies")
# print(r.text)
s = requests.Session()
r = s.get('http://httpbin.org/cookies',cookies={'from-my': 'browser'})
print(r.text)
cookies=s.cookies
r = s.get('http://httpbin.org/cookies',cookies=cookies)
print(r.cooki)
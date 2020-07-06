import requests
import re
url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
    "Referer":"https://movie.douban.com/"
}
response = requests.get(url,headers=headers)
str = response.content.decode("utf-8")
#print(str)
pingfen=re.findall('"rate":"\S+?"',str)
print(pingfen)
pianming=re.findall('"title":"\S+?"',str)
print(pianming)
pianming=re.findall('"title":"\S+?"',str)
url=re.findall('"url":"\S+?"',str)
for i in range(len(url)):
    print(re.sub("\\\\/","/",url[i]))

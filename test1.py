import requests
from lxml import etree
from bs4 import BeautifulSoup
def firstwy(resp):
    soup = BeautifulSoup(resp.content.decode("gb18030",errors="ignore"), "lxml")
    print(type(soup))
    trs = soup.find_all("ul")
    print(type(trs))
    return trs
def shuchu(soup2):
    text=soup2[8].find_all("a")
    text1 = soup2[8].find_all("a", attrs={"class": "ulink"})
    list=[]
    for i in text:
        element={}
        print("影片链接是：",i["href"])
        print("影片名为：",i.string)
        element["影片链接是："]=i["href"]
        element["影片名是："] =i.string
        list.append(element)
    print(list)
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
}
url = "https://www.dytt8.net/html/gndy/dyzz/index.html"
resp=requests.get(url,headers=headers)
with open("dy.html","w",encoding="utf-8") as fp:
    str1=resp.content.decode("gb18030",errors="ignore")
    fp.write(str1)
trs1=firstwy(resp)
with open("dy1.html","w",encoding="utf-8") as fp:
    fp.write(str(trs1[8]))
shuchu(trs1)


import requests
from lxml import etree
import re
page=int(4)
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
}
def wangyehuoqu(url,headers):
    response=requests.get(url,headers=headers)
    text=response.content.decode("gb18030",errors="ignore")
    wangye=etree.HTML(text)
    return wangye
def xiangqing(wy):
    list=wy.xpath("//td/b/a/text()")
    lianjie=wy.xpath("//td/b/a/@href")
    pianming=wy.xpath("//tr/td[@colspan=2]/text()")
    for i in range(len(wy.xpath("//td/b/a/text()"))):
        print("标题是:",list[i])
        print("片名是:",pianming[i])
        print("其余内容:",re.split("◎",pianming[i]))
        print("链接是:","dytt8.net"+lianjie[i])
for i in range(1,page):
    if i==1:
         url = "https://www.dytt8.net/html/gndy/dyzz/index.html"
         #print(url)
         wy=wangyehuoqu(url,headers)
         xiangqing(wy)
    else:
         url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html".format(i)
         print(url)
         wy=wangyehuoqu(url,headers)
         xiangqing(wy)
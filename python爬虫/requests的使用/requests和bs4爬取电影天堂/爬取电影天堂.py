from bs4 import BeautifulSoup
import lxml
import requests
import re
#这里只是爬取的头两页
page=int(2)
#这里是获取整个网页的内容
def huoquwy(page):
    for i in range(1,page+1):
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        }
        if i ==1:
            url = "https://www.dytt8.net/html/gndy/dyzz/index.html"
        else:
            url="https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html".format(i)
        resp = requests.get(url, headers=headers)
        with open("num{}.html".format(i), "w", encoding="gb18030") as fp:
            fp.write(resp.content.decode("gb18030", errors="ignore"))
#这里是对保存的整体网页数据进行处理
def chuli(page):
    for i in range(1,page+1):
        soup=BeautifulSoup(open("num{}.html".format(i)),"lxml")
#记住这里是每一个find_all返回的结果都可以再进一步的find，bs4就是这样一层一层剥开的
        trs=soup.find_all("ul")
        trs2=trs[8].find_all("a",attrs={"class":"ulink"})
        for j in trs2:
            print("电影链接是：","www.dytt8.net"+j["href"])
        trs3=trs[8].find_all("a",attrs={"class":"ulink"})
        for k in trs3:
            #print(k.get_text())
            list1=re.findall("《.*》",str(k.get_text()))
            print("电影名是:",list1)
huoquwy(page)
chuli(page)
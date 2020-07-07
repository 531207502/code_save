from bs4 import BeautifulSoup
import requests
import lxml
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
}
url="http://www.weather.com.cn/textFC/xn.shtml"
resp=requests.get(url,headers=headers)
pageall=resp.content.decode("utf-8")
def chuli(page):
    soup=BeautifulSoup(page,"lxml")
    #下面的是整页
    trs=soup.find("div",attrs={"class":"conMidtab"})
    #下面的把整页按照城市拆分
    trs1=trs.find_all("div",attrs={"class":"conMidtab2"})
    list_2=[]
    for i in trs1:
        trs2=i.find_all("tr")[2:]
        #print(trs2)
        #break
        k=0
        for j in trs2:
            if k==0:
                trs3 = j.stripped_strings
                list1=(list(trs3))
                list_2.append({"city":list1[1],"temp":list1[9]})
            else:
                trs3 = j.stripped_strings
                list1 = (list(trs3))
                #print(list(trs3))
                list_2.append({"city":list1[0],"temp":list1[8]})
            k+=1
        #print("接着下一个目录了")
    for l in list_2:
        print(l)
        list_2.sort(key=)
chuli(pageall)
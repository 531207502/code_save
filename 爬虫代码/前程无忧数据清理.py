from lxml import etree
from bs4 import BeautifulSoup
import requests
import re

#这里使用的是51jb的来进行实验的，因为51的还比较简单，同时他代码是html写的，不像腾讯或者拉钩，反爬虫比较多，所以这里用这个来进行xpath的实验
url = "https://search.51job.com/list/090200,000000,0000,00,9,99,%2B,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
}
resp = requests.get(url,headers=headers)
with open("qiancheng.html","w",encoding="gb18030") as fp:
    fp.write(resp.content.decode("gb18030"))#这里用utf-8不行，会报错，所以用gb18030
#这里和网页上有点不同，这里注意虽然是通过文件打开的，但是还是要选择解析器
bstext=BeautifulSoup(open("qiancheng.html",encoding="gb18030"),"lxml")
#第一次数据清理，提取所有标签是div，过滤条件是class=el的
list1=bstext.find_all("div",attrs={"class":"el"})
print(len(list1))
#这里是根据提取出来的，发现我们需要的数据是从第18个开始的，一直到结束
#print(len(list1))
# for i in range(17,66):
#     list1[i].find_all("")
for i in range (17,66):
    print("下面是提取出来的数据明细")
    print("岗位要求：{}".format(*list(list1[i].find_all("a")[0].stripped_strings)))
    print("公司名称：{}".format(*list(list1[i].find_all("span",attrs={"class":"t2"})[0].stripped_strings)))
    print("详细信息网址：{}".format(list1[i].find_all("a")[0]["href"]))
    try:
        print("薪资：{}".format(*list(list1[i].find_all("span",attrs={"class":"t4"})[0].strings)))
    except:
        print("薪资：没有在表中体现薪资")
    print("--"*60)

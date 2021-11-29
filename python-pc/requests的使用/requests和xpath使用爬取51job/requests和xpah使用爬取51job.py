from lxml import etree
import requests
import re

#这里使用的是51jb的来进行实验的，因为51的还比较简单，同时他代码是html写的，不像腾讯或者拉钩，反爬虫比较多，所以这里用这个来进行xpath的实验
url = "https://search.51job.com/list/090200,000000,0000,00,9,99,%2B,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
}
resp = requests.get(url,headers=headers)
with open("qiancheng.html","w",encoding="utf-8") as fp:
    fp.write(resp.content.decode("gb18030"))#这里用utf-8不行，会报错，所以用gb18030
parser = etree.HTMLParser(encoding="utf-8")
html = etree.parse("qiancheng.html",parser=parser)
#1：获取所有div标签，这里获取所有的div标签，虽然没啥意义，因为很多东西是我们不要的，但是主要是为了做实验，同时这个语法和在网页中使用xpath是一样的，这里显示的就是div下所有的内容
#同时注意xpath返回的是一个列表
# divs = html.xpath("//div")
# for div in divs:
#     print(div)
#     print(etree.tostring(div,encoding="utf-8").decode("utf-8"))
#获取第二个div标签，注意这里的第二个标签和第一个标签是父子关系，而不是平级的关系的，自己体会下,因为//div代表任意位置的div，加上[2]代表这个位置下的第二个div，属于任意位置的div子元素的第二个子元素
# divs = html.xpath("//div[2]")
# for div in divs:
#     print(div)
#     print(etree.tostring(div,encoding="utf-8").decode("utf-8"))
#这里拿的是很多第二个，如果只取第一个的话，也可以这样写
#div = html.xpath("//div[2]")[0]
#获取所有class等于el的div标签,同时获取职位详情的url,他职位的详情url是在span class="t2"里面,所以这里的路径写的是./span/a/@href,这里的.代表当前路径,@href是取的对应属性的值
# divs = html.xpath("//div[@class='el']")
# for div in divs:
    # print(div)
    # print(etree.tostring(div,encoding="utf-8").decode("utf-8"))
    # href=div.xpath("./span/a/@href")
    # print(href)
#获取所有标签的值
divs = html.xpath("//div[@class='el']")
for div in divs:
    #print(div)
    #print(etree.tostring(div,encoding="utf-8").decode("utf-8"))
    zhiwei=div.xpath("./p/span/a/text()")
    if zhiwei!=[]:
        print(re.sub("/r|/n","",zhiwei[0]).strip())
        gongsi = div.xpath("./span[1]/a/text()")
        print(*gongsi)
        addr = div.xpath("./span[2]/text()")
        print(addr)
        sr = div.xpath("./span[3]/text()")
        print(sr)
        date = div.xpath("./span[4]/text()")
        print(date)
    else:
        pass
from urllib import request
from urllib import parse
#通过网站访问的页面的地址是：https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%88%98%E5%BE%B7%E5%8D%8E
#实际我们输入的地址是：https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=刘德华
#因为有中文，所以需要进行编码，把中文转为16进制的字符串，两种方式，字典或者quote
param = parse.quote("刘德华")
zd={"wd":"刘德华"}
param2 = parse.urlencode(zd)
print(param)
print(param2)
url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&"
url1= url + "wd=" +param
print(url1)
url2= url + param2
print(url2)
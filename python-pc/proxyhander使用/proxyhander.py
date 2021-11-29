from urllib import request
url = 'http://httpbin.org/ip'
handler = request.ProxyHandler({'http': '49.7.96.227:16818'})#c传入代理地址构建代理
opener = request.build_opener(handler)#通过构建的代理创建一个opener
resp = opener.open(url)#通过创建的opener去发送请求
print(resp.read().decode('utf-8'))
from urllib import request
resp = request.urlopen("http://www.baidu.com")
print(resp.readline())
print(resp.read())
#print(resp.readlines())
print(resp.geturl())
print(resp.getcode())
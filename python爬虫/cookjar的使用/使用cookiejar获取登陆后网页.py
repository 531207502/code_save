from urllib import request
from urllib import parse
from http.cookiejar import CookieJar
cookiejar = CookieJar()
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
login_url = 'http://www.renren.com/PLogin.do'
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}
data = {
    'email': '531207502@qq.com',
    'password': '890718feng'
}
req = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
opener.open(req)
dapeng_url = 'http://www.renren.com/880151247/profile'
req = request.Request(dapeng_url, headers=headers)
resp = opener.open(req)
with open('renren.html','w',encoding='utf-8') as fp:
    fp.write(resp.read().decode('utf-8'))
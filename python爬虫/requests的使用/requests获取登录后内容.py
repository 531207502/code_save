import requests
data={
    "email":"531207502@qq.com",
    "password":"890718feng"
}
session=requests.session()
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}
login_url="http://www.renren.com/PLogin.do"
session.post(login_url,data=data,headers=headers)
cookies=session.cookies
dapeng_url = 'http://www.renren.com/880151247/profile'
resp=session.get(dapeng_url,headers=headers,cookies=cookies)
with open("renren.html","w",encoding="utf-8") as fp:
    fp.write(resp.content.decode("utf-8"))
import requests
from urllib import request
data={
    "email":"531207502@qq.com",
    "password":"890718feng"
}
#通过创建session来保存cookie实现对需要cookie页面的访问
session=requests.session()
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}
login_url="http://www.renren.com/PLogin.do"
#以下是第一次登录网页，此时登录后会在session中保存登陆后的cookie
session.post(login_url,data=data,headers=headers)
cookies=session.cookies
dapeng_url = 'http://www.renren.com/880151247/profile'
#进行登陆后的操作，访问指定的页面，此时因为有了对应的cookies，所以可以调用进行访问,这里session中就有了cookie了，所以不需要在参数中再次添加cookie
#另外补充说明下，这里的headers和cookies，proxies这些都应该是request里面有的，他应该是继承了request的一些功能，统一包含在了**kwargs参数里
resp=session.get(dapeng_url,headers=headers)
with open("登陆后人人网页.html","w",encoding="utf-8") as fp:
    fp.write(resp.content.decode("utf-8"))
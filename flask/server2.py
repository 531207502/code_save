from flask import Flask
from flask import render_template,request
#创建web服务对象
app=Flask('hi_flask')
#指定路由和访问方式，访问方式是放在列表中的，必须大写
@app.route('/hi',methods=['GET','POST'])
#在上面指定路由后，会自动运行下面的 hi1
def hi1():
    #假设只支持安卓的手机访问
    #print(app.url_map)
    platform=request.args.get('platform','pc')
    if platform.lower()!='android':
        return"""
        <h2>目前支支持安装的设备</h2>
        """
    if request.method=='GET':
        return """
        <h1>用户登录页面</h1>
        <form action="/hi?platform=android"method='post'>
        <input name="username" placeholder="用户名"><br>
        <input name="pwd" placeholder="密码"><br>
        <button>提交</button>
        </form>
        """
    else:
        name=request.form.get('username')
        pwd=request.form.get('pwd')
        if all((name=="cisco",pwd=="cisco")):
            return """
            <h2 style="color:blue">登陆成功</h2>
            """
        else:
            return """
                        <h2 style="color:orange;width:200px;height:200px;background:red;text-align:center;">登陆失败<a href="/hi?platform=android">重试</a></h2>
                        """
# @app.route('/bank',methods=['GET','POST'])
# def addbank():
#     data={
#         'title':'绑定银行卡',
#         'error_message':'没有对应的信息'
#     }
#     html=render_template('temp.html',**data)
#     return html
app.run("localhost",5000)
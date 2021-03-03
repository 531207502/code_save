import os
from wsgiref.simple_server import make_server
#处理业务最核心的函数,env用来接收http请求的对象，make_response是发送响应http请求的函数
def app(env,make_response):
    #生成响应头的信息
    '''
    请求路径：PATH_INFO
    请求方法：REQUEST_METHOD
    请求查询参数：QUERY_STRING
    客户端地址：REMOTE_ADDR
    请求上传的数据类型：CONTENT_TYPE
    客户端的代理（浏览器）：HTTP_USER_AGENT
    读取请求上传的字节数据对象：wsgi.input
    '''
    # for k,v in env.items():
    #     print(k,':',v)
    #获取请求资源的路径
    path=env.get('PATH_INFO')
    #响应头，根据响应的数据增加不同的响应头，结构为k:v
    headers=[]
    #响应的数据
    body=[]
    # 静态资源的目录
    static_dir='images'
    if path == '/favicon.ico':
        #静态资源的完整路径
        res_path=os.path.join(static_dir,'aim.png')
        headers.append(('content-type','image/*'))
    elif path == '/':
        #主页
        res_path=os.path.join(static_dir,'test.html')
        headers.append(('content-type', 'text/html;charset=utf-8'))
    else:
        res_path=os.path.join(static_dir,path[1:])
        print(res_path)
        if res_path.endswith('.html'):
            headers.append(('content-type', 'text/html;charset=utf-8'))
        elif any((res_path.endswith('.png'),
                 res_path.endswith('.ico'))):
            headers.append(('content-type','image/*'))
    # make_response('200 OK',[('Content-Type','text/html;charset=utf-8')])
    # #响应的数据
    # return ['<h3>HI,WSGI</h3>'.encode('utf-8')]
    #判断资源是否存在
    status_code=200
    if not os.path.exists(res_path):
        status_code=404
        body.append('<h1 style="color;red text-align:center">不存在的访问路径:404</h1>'.encode('gbk'))
    else:
        with open(res_path,'rb') as f:
            body.append(f.read())
    make_response('{} ok'.format(status_code),headers)
    return body
#生成web应用服务进程
httpd=make_server('0.0.0.0',8000,app)
#启动服务，开始监听客户端连接
httpd.serve_forever()
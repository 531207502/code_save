#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
import time
#整个程序的思路为：
#1：首先登录主页http://scxk.nmpa.gov.cn:81/xk/，然后爬取主页，存储文件名为zhuye.html进行查看，发现需要的部分没有显示出来
#2：继续在主页，判定为ajax，通过谷歌开发者工具查看发现XHR中的post请求和网址才是获取需要部分的数据，进行爬取后分析后续需要提取的数据
#3：继续上面的思路，发现需要爬取的每个企业的详细信息也是在XHR中显示的，前缀都一样，post请求里面的数据为第二步里面提取的id值
if __name__ == "__main__":
    url = 'http://scxk.nmpa.gov.cn:81/xk/'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    date_resp=requests.get(url=url,headers=headers).content.decode('utf-8')
    with open('./zhuye.html','w',encoding='utf-8') as fp:
        fp.write(date_resp)
    url1='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    url2='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    page=input('请输入你想要查询的页数：')
    for page1 in range(int(page)):
        data={
            'on': 'true',
            'page': page1+1,
            'pageSize': '15',
            'productName':'',
            'conditionType': '1',
            'applyname':'',
            'applysn':''
        }
        date_resp1=requests.post(url=url1,data=data,headers=headers).json()
        # print(date_resp1)
        for getid in date_resp1['list']:
            #print(getid['ID'])
            data2 = {
                'id': getid['ID']
            }
            date_resp2 = requests.post(url=url2, data=data2, headers=headers).json()
            print(date_resp2)
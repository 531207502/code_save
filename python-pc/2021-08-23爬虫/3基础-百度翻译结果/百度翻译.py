#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
if __name__ == "__main__":
    #1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # post_url1= 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
    #2.进行UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    #3.post请求参数处理（同get请求一致）
    word = input('enter a word:')
    data = {
        'kw':word
    }
    # data1 ={
    # 'from': 'en',
    # 'to': 'zh',
    # 'query': 'cat',
    # 'transtype': 'realtime',
    # 'simple_means_flag': 3,
    # #'sign': 326156.6461,
    # 'token': '659059f428c5cf7711d477475fcb3815',
    # 'domain': 'common'
    # }
    #4.请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    # response1 = requests.post(url=post_url1, data=data1, headers=headers)
    #5.获取响应数据:json()方法返回的是obj（如果确认响应数据是json类型的，才可以使用json（））
    dic_obj = response.json()
    # dic_obj1 = response1.json()
    #持久化存储
    fileName = word+'.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    # fileName1 = word+ '1' + '.json'
    # fp = open(fileName1, 'w', encoding='utf-8')
    # json.dump(dic_obj1, fp=fp, ensure_ascii=False)
    print('over!!!')



#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
if __name__ == "__main__":
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    area = input('选择你的area :')
    data = {
        'cname': area,
        'pageIndex': '1',
        'pageSize': 10
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    response = requests.post(url=url,data=data,headers=headers)

    list_data = response.content.decode('utf-8')
    print(type(list_data))
    print(list_data)
    fp = open('./KFC.text','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    fp.close()
    print('over!!!')
    json.dumps
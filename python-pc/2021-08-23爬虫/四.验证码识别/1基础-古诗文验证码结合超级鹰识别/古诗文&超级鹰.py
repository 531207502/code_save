import requests
from lxml import etree
import os
import cjy
import time
if __name__ == "__main__":
    dlurl = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    headers1 ={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    response = requests.get(url=dlurl, headers=headers).content.decode('utf-8')
    # print(response)
    xresp = etree.HTML(response)
    li_list = xresp.xpath('//*[@id="imgCode"]/@src')[0]
    pjurl = 'https://so.gushiwen.cn/'
    #print(li_list)
    if not os.path.exists('./dlyzm'):
        os.mkdir('./dlyzm')
    session = requests.Session()
    response1 = session.get(url=pjurl+li_list, headers=headers,proxies={}).content
    with open('./dlyzm/'+'yzm.jpg', 'wb') as fp:
        fp.write(response1)
    time.sleep(0.1)
    chaojiying = cjy.Chaojiying_Client('531207502', '890718feng', '921747')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('dlyzm/yzm.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    cjy_result=(chaojiying.PostPic(im, 1004))  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    print(cjy_result['pic_str'])
    gswrul = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    data_gsw ={
    '__VIEWSTATE': 'GoO6y+FWBGy+uDWuohyw5yuK69+GFiPeciHy/gWiIUOe3O65aE4azkuHg/v4AZ4B+LiRGTcNy83QY9hZ7Xbux87PfBbZqbpQHu8Y/Qgp7kXMBp+dfRM5JnjH6Is=',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email':'531207502@qq.com',
    'pwd':'890718feng',
    'code': cjy_result['pic_str'],
    'denglu': '登录'
    }
    # gswurl2='https://so.gushiwen.cn/user/collect.aspx'
    # headers2 ={
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    #     'cookie' : 'login=flase; ASP.NET_SessionId=vzs5p3drwbtbha2gyiy3czls; wsEmail=531207502%40qq.com; Hm_lvt_9007fab6814e892d3020a64454da5a55=1630047597,1630071897; codeyzgswso=3cad990d74cd110e; Hm_lpvt_9007fab6814e892d3020a64454da5a55=1630074188; gsw2017user=2068936%7c02421D334C05D85ACF7BCF3D7A847AEF; login=flase; wxopenid=defoaltid; gswZhanghao=531207502%40qq.com; gswEmail=531207502%40qq.com'
    # }
    gsw_data = session.post(url=gswrul,data=data_gsw,headers=headers1)
    # gsw_data2 = requests.get(url=gswurl2,headers=headers2)
    print(gsw_data.status_code)
    print(session.cookies)
    # print(gsw_data2.status_code)
    with open('./gsw.html','w',encoding='utf-8') as fp:
        fp.write(gsw_data.text)
    # with open('./gsw2.html','w',encoding='utf-8') as fp:
    #     fp.write(gsw_data2.text)
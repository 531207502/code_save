import requests
from lxml import etree
import os
if __name__ == "__main__":
    url = 'http://pic.netbian.com/4kmeinv/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers).content.decode('gbk')
    #print(response)
    xresp = etree.HTML(response)
    li_list = xresp.xpath('//div[@class="slist"]/ul/li')
    print(li_list)
    if not os.path.exists('./mnLibs'):
        os.mkdir('./mnLibs')
    for li in li_list:
        src = 'http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
        #print(src)
        des = li.xpath('./a/img/@alt')[0]
        #print(des)
        # test = li.xpath('./a/b/text()')
        # print(test)
        img_data = requests.get(url=src, headers=headers).content
        img_path = 'mnLibs/' + des
        with open(img_path+'.jpg', 'wb') as fp:
            fp.write(img_data)
            print(des, '下载成功！！！')
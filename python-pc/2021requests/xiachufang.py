from bs4 import BeautifulSoup
import requests
import os
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
content=requests.get('https://www.xiachufang.com/',headers=headers)
#print(content.content.decode('utf-8'))
soup=BeautifulSoup(content.content.decode('utf-8'),'lxml')
#print(soup.prettify())
img=soup.find_all('img')
num1=1
#print(img)
list2=[]
for list1 in img:
    print("这是find的方法取值，这是第{}次".format(num1))
    num1+=1
    if list1.has_attr('data-src'):
        #print(list1['data-src'])
        if list1['data-src'].split('?')[0]:
            list2.append(list1['data-src'].split('?')[0])
    else:
        #print(list1['src'])
        if list1['src'].split('?')[0]:
            list2.append(list1['src'].split('?')[0])
print(list2)
image_dir=os.path.join(os.path.curdir+'images')
print(image_dir)
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)
for lj in list2:
    #print(lj.split('/')[-1])
    nr=requests.get(lj,headers=headers)
    filename=os.path.join(image_dir,lj.split('/')[-1])
    #print(filename)
    with open(filename,'wb') as f:
        f.write(nr.content)
from bs4 import BeautifulSoup
import re
html = """
<html><head><title>The Dormouse's story1</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup=BeautifulSoup(html,'lxml')
#print(soup.prettify())

# 输出第一个 title 标签（整个title标签）
print(soup.title)

# 输出第一个 title 标签的标签名称
print(soup.title.name)

# 输出第一个 title 标签的包含内容
print(soup.title.string)

# 输出第一个 title 标签的父标签的标签名称
print(soup.title.parent.name)

# 输出第一个p标签（整个p标签）
print(soup.p)

# 输出第一个  p 标签的 class 属性内容（属性内容都是通过字典的方式获得的）
print(soup.p['class'])

# 输出第一个  a 标签的  href 属性内容
print(soup.a['href'])
'''
soup的属性可以被添加,删除或修改. 再说一次, soup的属性操作方法与字典一样
'''
# 修改第一个 a 标签的href属性为 http://www.baidu.com/
soup.a['href'] = 'http://www.baidu.com/'

# 给第一个 a 标签添加 name 属性
soup.a['name'] = u'百度'

# 删除第一个 a 标签的 class 属性为
del soup.a['class']

##输出第一个  p 标签的所有子节点
print(soup.p.contents)

# 输出第一个  a 标签
print(soup.a)

# 输出所有的  a 标签，以列表形式显示
print(soup.find_all('a'))
# 输出第一个 id 属性等于link3 的a 标签
print(soup.find(id="link3"))

# 获取所有文字内容
print(soup.get_text())

# 输出第一个  a 标签的所有属性信息
print("输出标签信息")
print(soup.a.attrs)

for link in soup.find_all('a'):
    # 获取 link 的  href 属性内容
    print(link.get('href'))

# 对soup.p的子节点进行循环输出
for child in soup.p.children:
    print(child)

# 正则匹配，名字中带有b的标签
for tag in soup.find_all(re.compile("b")):
    print(tag.name)

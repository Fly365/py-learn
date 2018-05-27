# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

# 创建 BeautifulSoup 对象
soup = BeautifulSoup(html, "lxml")

# 查找的是所有内容中的第一个符合要求的标签
print(soup.head)

# name即为 [document]
print(soup.head.name)

# attrs
print(soup.p.attrs)

print(soup.p['class'])
# 对这些属性和内容等进行修改
#soup.p['class'] = "newClass"
# 可以对这个属性进行删除
#del soup.p['class']

# 得到标签内容后，获取标签内部文字，用.string即可
print(soup.p.string)

# comment对象是一个特殊类型的NavigableString对象，其输出内容不包括注释符号
print(soup.a.string)

# 直接子节点: .contents .children 属性,输出方式为列表
print(soup.head.contents)
# 直接子节点.children 属性,返回的不是list，可以通过遍历获取所有子节点
print(soup.head.children)
for child in soup.body.children:
    print(child)

# 所有子孙节点 : .descendants属性
for child in soup.descendants:
    print(child)

# 节点内容： .string
print(soup.title.string)



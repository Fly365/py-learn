# -*- coding: utf-8 -*-
from lxml import etree

html = etree.parse("lxml-opt.html")

print(type(html))

# 获取所有li标签
result = html.xpath("//li")

print(result)

print(result[0])

# 获取li标签的所有class属性
print("----------li下的所有class属性----------------")
result02 = html.xpath("//li/@class")
print(result02)

# 获取li标签下hre为 link1.html的 a 标签
print("-----------li标签下hre为 link1.html的 a 标签-------------")
result03 = html.xpath("//li/a[@href='link1.html']")
print(result03)

# 获取li标签下的所有span标签
print("-----------获取li标签下的所有span标签-------------")
result04 = html.xpath("//li//span")
print(result04)

# 获取li标签下的a标签里面所有class
result05 = html.xpath("//li/a//@class")
print(result05)

# 获取最后一个li的a的href，使用谓语 [last()] 可以找到最后一个元素
result06 = html.xpath("//li[last()]/a/@href")
print(result06)

#获取倒数第二个元素的内容
result07 = html.xpath("//li[last()-1]/a")
print(result07[0].text)

#获取class值为bold 的标签名
result08 = html.xpath("//*[@class='bold']")
print(result08[0].tag)
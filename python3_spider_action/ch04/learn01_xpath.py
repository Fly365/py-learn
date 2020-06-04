# encoding=utf8

from lxml import etree

# 所有节点
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//*')
print(result)

# 子节点
result2 = html.xpath('//li/a')
print(result2)

# 父节点，通过..来实现,也可以通过parent::来获取
result3 = html.xpath('//a[@href="link4.html"]/../@class')
print(result3)

# 属性匹配
result4 = html.xpath('//li[@class="item-0"]')
print(result4)

# 文本获取
result5 = html.xpath('//li[@class="item-0"]/a/text()')
print(result5)

# 属性获取
result6 = html.xpath('//li/a/@href')
print(result6)

# 属性多值匹配
result7 = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result7)

# 多属性匹配
result8 = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result8)
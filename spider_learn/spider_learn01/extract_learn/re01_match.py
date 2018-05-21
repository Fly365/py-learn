import re

# 用于匹配至少一个数字
patterm_1 = re.compile(r'\d+')
# 查找头部，没有匹配
m = patterm_1.match("one12twothree34four")
print(m)

# 从 'e' 位置开始匹配，没有匹配
m2 = patterm_1.match("one12twothree34four",2,10)
print(m2)

# 从 '1' 的位置开始匹配，正好匹配
m3 = patterm_1.match("one12twothree34four",3,10)
print(m3)

m3.group(0)
m3.start(0)
m3.end(0)
m3.span(0)
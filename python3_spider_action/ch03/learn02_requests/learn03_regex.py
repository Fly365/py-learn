# encoding=utf8

# match 匹配方法,检测字符串是否匹配
import re
content = "hello 123 4567 world_this is l Regex Demo"
result = re.match("^hello\s\d\d\d\s\d{4}\s\w{10}", content)
print(result)
# 匹配到的内容
print(result.group())
# 输出匹配的范围，即 匹配到结果字符串在原字符串中的位置范围
print(result.span())

'''
使用()括号将想要提取字符串括起来。()实际上标记了一个子表达式开始和结束位置，
被标记每个子表达式会依次对应每一个分组
'''
import re
content = "hello 1234567 World_this is l Regex Demo"
result = re.match("^hello\s(\d+)\sWorld", content)
print(result)
print(result.group(1))

# 通用匹配，.(点)可以匹配任意字符(除换行符)
# *(星)可以匹配前面字符无限次
import re
content = "hello 123 4567 world_this is l Regex Demo"
# 中间部分直接忽略，全部使用.*来代替
result = re.match("^hello.*Demo$", content)
print(result)
print(result.group())

import re

pattern = re.compile(r"\d+")

result1 = pattern.findall("hello 123456 789")
result2 = pattern.findall("one1tow2three3four4",0,10)

print(result1)

print(result2)

pattern2 = re.compile(r"\d+\.\d+")
result3 = pattern2.findall("123.1234, 'bigdata',23456, 3.13")
# findall以列表形式，返回全部能匹配的子串给result
for item in result3:
    print(item)

import re


str = "你好，hello, 中文"
pattern = re.compile(r'[\u4e00-\u9fa5]+')
result = pattern.findall(str)

print(result)

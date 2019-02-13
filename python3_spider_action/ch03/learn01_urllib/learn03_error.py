# encoding=utf-8

# 用else来处理正常的逻辑，较好的异常处理方法
from urllib import request,error

try:
    response = request.urlopen("https://cuiqingcai.com/index.htm")
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print("request successfully")
# encoding=utf8

import requests

# 基础使用
r = requests.get("https://www.baidu.com")
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

# GET 请求
r = requests.get("http://httpbin.org/get")
print(r.text)

# 带有参数的 GET
data = {
    "name": "jerry",
    "age": 20
}
r = requests.get("http://httpbin.org/get", params= data)
# 网页的返回类型实际上是 str 类型，当时它很特殊，是 JSON格式的。
# 如果想直接解析返回结果，得到一个字典格式化话，可以直接调用json()方法
print(r.text)
print(r.json())

# 抓取网页
import requests, re
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile("explore-feed.*?question_link.*?>(.*?)</a>", re.S)
titles = re.findall(pattern, r.text)
print(titles)

# 获取二进制数据
import requests
r = requests.get("https://github.com/favicon.ico")
print(r.text)
print(r.content)
# 存储
with open("favicon.ico", "wb") as f:
    f.write(r.content)

# POST请求
import requests
data = {
    "name": "jerry",
    "age": 20
}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)

# requests内置状态码查询 requests.codes
import requests
r = requests.get("http://www.baidu.com")
print(r.status_code)
exit() if not r.status_code == requests.codes.ok else print("request successfully")
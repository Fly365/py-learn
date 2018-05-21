import requests

kw = {'wd':'python3教程'}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# params 接收一个字典或者字符串查询参数，字典类型自动转换为URL编码，不需要urlencode()
response = requests.get("http://www.baidu.com/s?",params=kw, headers=headers)

# 查看响应内容，response.text返回的是Unicode格斯数据
print(response.text)

# 查看响应内容，response.content返回字节流数据
print(response.content)

# 查看完整URL地址
print(response.url)

# 查看响应头部字符编码
print(response.encoding)

# 查看响应码
print(response.status_code)
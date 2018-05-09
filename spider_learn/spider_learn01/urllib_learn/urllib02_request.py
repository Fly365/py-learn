import urllib.request

# URL作为Request()方法的参数，构造并返回一个Request对象
request = urllib.request.Request('http://www.baidu.com')

# 将request对象作为urlopen()方法的参数，发送给服务器并接收响应
response = urllib.request.urlopen(request)

html = response.read().decode('utf-8')

print(html)
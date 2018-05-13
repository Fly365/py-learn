import urllib.request

# 构建一个HTTPHandler处理器对象，支持处理HTTP请求
http_handler = urllib.request.HTTPHandler()
# 加上debuglever参数，还可以启动debug模式,默认值为0
#http_handler = urllib.request.HTTPHandler(debuglevel=1)

# 构建一个HTTPHandler处理器对象，支持处理HTTPS请求
#http_handler = urllib.request.HTTPSHandler()


# 调用urllib.request.build_opener()方法，创建支持处理HTTP请求的opener对象
opener = urllib.request.build_opener(http_handler)

#构建request请求
request = urllib.request.Request("http://www.baidu.com/")

#调用自定义opener对象的open()方法，发送request请求
response = opener.open(request)
html = response.read().decode("utf-8")
print(html)
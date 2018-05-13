import urllib.request

# 构建两个代理Handler，一个有代理IP，一个没有代理IP
http_proxy_handler = urllib.request.ProxyHandler({"http":"124.88.67.81:80"})
null_proxy_handler = urllib.request.ProxyHandler({})

proxy_switch = True

#通过urllib.request.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
if proxy_switch:
    opener = urllib.request.build_opener(http_proxy_handler)
else:
    opener = urllib.request.build_opener(null_proxy_handler)

request = urllib.request.Request("http://www.baidu.com")

# 如果这样写，只有使用opener.open()方法发送请求才使用自定义代理，而urlopen()则不使用自定义代理
response = opener.open(request)

# 如果这样写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen()发送请求，都将使用自定义代理
#urllib.request.install_opener(opener)
#response = urllib.request.urlopen(request)

html = response.read().decode("utf-8")
print(html)
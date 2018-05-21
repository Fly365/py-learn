import urllib.request,http.cookiejar

# 保存cookie的本地磁盘文件名
filename = "cookie.txt"

# 声明一个MozillaCookieJar(有save实现)对象实例来保存cookie，之后写入文件
cookiejar = http.cookiejar.MozillaCookieJar(filename)

handler = urllib.request.HTTPCookieProcessor(cookiejar)

opener = urllib.request.build_opener(handler)

response = opener.open("http://www.baidu.com")

cookiejar.save()
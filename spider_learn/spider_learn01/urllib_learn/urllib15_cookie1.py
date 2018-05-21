import urllib.request,http.cookiejar

# 构建一个CookieJar对象实例来保存cookie
cookie_jar = http.cookiejar.CookieJar()

# 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
handler = urllib.request.HTTPCookieProcessor(cookie_jar)

opener = urllib.request.build_opener(handler)

# 以get方法访问页面，访问后自动保存cookie到cookie_jar中
opener.open("http://www.baidu.com")

# 可以按表尊格式将保存cookie打印出来
cookieStr = ""
for item in cookie_jar:
    cookieStr = cookieStr + item.name + "=" + item.value + ";"

# 摄取最后一位分号
print(cookieStr[:-1])
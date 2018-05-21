import urllib.request,http.cookiejar,urllib

cookie = http.cookiejar.CookieJar()

cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(cookie_handler)

# addheaders接受一个列表，里面每个元素都是一个handers信息的元组，opener将附带henders信息
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]

# 登录需要账户密码
data = {"email":"mr_mao_hacker@163.com", "password":"alaxxxxxime"}

# 通过urlencode转码
postdata = urllib.parse.urlencode(data)

request = urllib.request.Request("http://www.renren.com/PLogin.do",data=postdata.encode("utf-8"))
# 通过opener发送请求，并获取登录后的cookie值
opener.open(request)

# opener包含用户登录后的这个cookie值，可以直接访问登录后才可以访问的页面
response = opener.open("http://www.renren.com/410043129/profile")

print(response.read().decode("utf-8"))
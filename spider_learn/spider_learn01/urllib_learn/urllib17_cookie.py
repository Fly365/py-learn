import urllib.request,http.cookiejar

cookiejar = http.cookiejar.MozillaCookieJar()
cookiejar.load("cookie.txt")

handler = urllib.request.HTTPCookieProcessor(cookiejar)

opener = urllib.request.build_opener(handler)

response = opener.open("http://www.baidu.com")
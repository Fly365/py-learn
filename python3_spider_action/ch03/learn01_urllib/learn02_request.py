# encoding=utf-8

# 验证
from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http://localhost:5000'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)


# 代理
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http' : 'http://127.0.0.1:9000',
    'https' : 'https://127.0.0.1:7000'
})

opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

# cookies
import http.cookiejar,urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)

# cookie 以文本形式保存
filename = 'cookies.txt'
# LWPCookeJar同样可以读取和保存Cookies，但格式和MozillaCookieJar不同,
# 会保存成 libwww.perl(LWP)格式的Cookies文件
cookie  = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)

# LWPCookie 从文件中读取并利用
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
print(response.read().decode('utf-8'))






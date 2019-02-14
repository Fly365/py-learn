# encoding=utf8


# 文件上传，上传文件在同一目录中
import requests
files = {"file": open("time.jpg", "rb")}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)


# cookies
import requests
r = requests.get("https://www.baidu.com")
print(r.cookies)
for key,value in r.cookies.items():
    print(key + "=" + value)

# 从浏览器headers中将cookie内容复制
import requests
headers = {
    "Cookie": "",
    "Host": "www.zhihu.com",
    "User-Agent": ""
}
r = requests.get("https://www.baidu.com", headers=headers)
print(r.text)


'''
第一个请求使用post方法登录某个网站，第二次获取成功登录后的自己个人信息，
再次用GET请求相关页面，实际上，相当于打开两个浏览器，是两个完全不相关会话，
是不能获取相关信息的
-- 解决该问题方法：维持同一个会话(相当于打开一个新的浏览器选型卡而不是新开一个浏览器)
如不想每次设置Cookies，可以使用 session对象
'''
import requests
requests.get("http://httpbin.org/cookies/set/number/123456789")
r=requests.get("http://httpbin.org/cookies")
print(r.text)
# 使用 session
s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/123456789")
r = s.get("http://httpbin.org/cookies")
print(r.text)

# SSL证书验证
# 使用verify参数控制是否检查此证书，默认为 True
import requests
from requests.packages import urllib3

urllib3.disable_warnings()
response = requests.get("https://www.12306.cn", verify=False)
print(response.status_code)

# 或者使用本地证书作为客户端证书，本地私有证书的key必须是解密状态
import requests
response = requests.get("http://12306.cn", cert=("/path/server.crt", "/path/key"))
print(response.status_code)

'''
代理设置
对于某些网站，测试时能正常获取内容，但是大规模爬取，网站可能会弹出验证码，或者调整到登录页面，
甚至会直接封禁客户端IP，导致一定时间段内无法访问
'''
import requests
proxies = {
    "http": "http://127.0.0.1:7000",
    "https": "https://127.0.0.1:8000"
}
requests.get("",proxies=proxies)

# 使用HTTP Basic Auth 代理
import requests
proxies = {
    "http": "http://user:password@host:port"
}
requests.get("", proxies=proxies)

# 使用 socks 协议代理,需要安装 socks库
# pip3 install 'requests[socks]'
import requests
proxies = {
    "http": "socks5://user:password@host:port",
    "https": "socks5://user:password@host:port"
}
requests.get("", proxies=proxies)

# 超时,秒
import requests
requests.get("", timeout=1)

# 身份认证
import requests
from requests.auth import HTTPBasicAuth
r = requests.get("", auth=HTTPBasicAuth("username", "password"))
print(r.status_code)

# 身份验证 简化方式
import requests
r = requests.get("", auth=("username","password"))
print(r.status_code)

# 其他认证，如 OAuth认证，需要安装oauth包
# pip3 install requests_oauthlib
import requests
from requests_oauthlib import OAuth1
url = "https://api.twitter.com/1.1/account/verify_credentials.json"
auth = OAuth1("your_app_key", "app_secret", "user_oauth_token", "user_oauth_token_secret")
requests.get(url,auth=auth)

# 将请求标识为数据结构 prepared request
from requests import Request, Session
url = "http://httpbin.org/post"
data = {
    "name": "jerry"
}
headers = {
    "User-Agent": ""
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)






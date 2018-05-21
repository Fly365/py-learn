import urllib.request,urllib

user = "test"
passwd = "123456"

web_server = "http://192.168,3.100"

# 构建密码管理对象
passwd_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

passwd_mgr.add_password(None,web_server,user,passwd)

http_auth_handler = urllib.request.HTTPBasicAuthHandler(passwd_mgr)

opener = urllib.request.build_opener(http_auth_handler)

# 通过install_opener()方法定义opener为全局opener
urllib.request.install_opener(opener)

request = urllib.request.Request(web_server)

# 定义opener为全局后，可直接使用urlopen()发送请求
response = urllib.request.urlopen(request)

print(response.read().decode("utf-8"))
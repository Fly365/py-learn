import urllib.request,urllib

# 代理授权账户
user = "mr_mao_hacker"
passwd = "sffqry9r"
proxy_server = "61.158.163.130:16816"

# 构建一个密码管理对象，用来保存需要处理的用户名和密码
passwd_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

#添加账户信息，第一个参数realm是与远程服务器相关的信息，一般都是用None
passwd_mgr.add_password(None,proxy_server,user,passwd)

# 构建一个代理基础用户名/密码验证的ProxyBasicAuthHandler处理器对象，参数是创建的密码管理对象
# 注意，这里不再使用普通ProxyHandler
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler(passwd_mgr)

# 通过build_opener()方法使用这些代理Handler对象，创建自定义opener对象，参数包括构建proxy_handler
opener = urllib.request.build_opener(proxy_auth_handler)

request = urllib.request.Request("http://www.baidu.com")

response = opener.open(request)

print(response.read().decode("utf-8"))

















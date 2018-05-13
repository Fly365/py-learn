import urllib.request,random

proxy_list = [
    {"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"},
    {"http" : "124.88.67.81:80"}
]

proxy = random.choice(proxy_list)

http_proxy_handler = urllib.request.ProxyHandler(proxy)
opener = urllib.request.build_opener(http_proxy_handler)
request = urllib.request.Request("http://www.baidu.com")
response = opener.open(request)
# encoding=utf-8

#import urllib.request,urllib.parse,urllib.error
from urllib import request,parse,error
import ssl
import socket

# urllib.error.URLError: <urlopen error unknown url type: https>
context = ssl._create_unverified_context()
#ssl._create_default_https_context = ssl._create_unverified_context
#response = urllib.request.urlopen("https://www.baidu.com",context=context)
#print(response.read().decode("utf-8"))


#data参数使用，如果传递了参数，那么请求方式是 post
#data = bytes(urllib.parse.urlencode({"word":"hello"}),encoding= "utf-8")
#response = urllib.request.urlopen("http://httpbin.org/post",data = data)
#print(response.read())


#timeout参数，设置超时时间控制一个网页抓取
#try:
#    response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.1)
#except urllib.error.URLError as e:
#    if isinstance(e.reason,socket.timeout):
#        print("Time out")


url = "http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Host":"httpbin.org"
}
dict = {
    "name":"Jerry"
}
data = bytes(parse.urlencode(dict), encoding="utf-8")
req = request.Request(url=url, data=data,headers=headers,method="POST")
resp = request.urlopen(req)
print(resp.read().decode("utf-8"))
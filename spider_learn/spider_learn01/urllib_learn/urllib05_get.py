# urllib负责URL编码处理
import urllib.request,urllib

url = "http://www.baidu.com/s"
# Python3中也有urllib和urllib3两个库，其中urllib几乎是Python2中urllib和urllib2两个模块的集合，
# 所以我们最常用的urllib模块，而urllib3则作为一个拓展模块使用
word = urllib.parse.urlencode({"wd":"scrapy示例教程"})

newurl = url + "?" + word
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

request = urllib.request.Request(newurl,headers=headers)
response = urllib.request.urlopen(request)

html = response.read().decode("utf-8")
print(html)


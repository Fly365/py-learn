import urllib.request

url = 'http://www.baidu.com'

ua_header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

request = urllib.request.Request(url,headers=ua_header)

response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
print(html)
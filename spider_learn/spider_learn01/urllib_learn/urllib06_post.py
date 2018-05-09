import urllib.request,urllib

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

formdata = {
    "i":"i love Python",
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"1525708104954",
    "sign":"7549261db061213c181974e1afa7f4a2",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTIME",
    "typoResult":"false"
}

data = urllib.parse.urlencode(formdata)
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request,data=data.encode('utf-8'))
html = response.read().decode("utf-8")
print(html)
# -*- coding: utf-8 -*-
import urllib.request,json,chardet
# pip install jsonpath-rw
from jsonpath_rw import jsonpath,parse

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
html = response.read()

# 把json格式字符串转换成Python对象
jsonobj = json.loads(html)

# 从根节点，匹配name节点

# encoding=utf-8

import urllib.request,urllib
import ssl

# urllib.error.URLError: <urlopen error unknown url type: https>
context = ssl._create_unverified_context()
#ssl._create_default_https_context = ssl._create_unverified_context
response = urllib.request.urlopen("https://www.baidu.com",context=context)
print(response.read().decode("utf-8"))
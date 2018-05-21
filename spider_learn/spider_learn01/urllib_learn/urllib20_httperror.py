import urllib.request

request = urllib.request.Request("https://bbs.csdn.net/777777")

try:
    urllib.request.urlopen(request)
except urllib.request.HTTPError as err:
    print(err.code)
    print(err)

print("--------------")
import urllib.request

request = urllib.request.Request("http://aa.bb.cc.com/")

try:
    response = urllib.request.urlopen(request,timeout=5)
    response.close()
except urllib.request.URLError as err:
    print(err.reason())
except ConnectionResetError as connErr:
    print(connErr)

print("----line------")
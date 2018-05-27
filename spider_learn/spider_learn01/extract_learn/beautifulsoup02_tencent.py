# -*- coding: utf-8 -*-
import urllib,urllib.request,json
from bs4 import BeautifulSoup

def tencent():
    url = "https://hr.tencent.com"
    req = urllib.request.Request(url + "/position.php?&start=10#a")
    resp = urllib.request.urlopen(req)
    resHmtl = resp.read()

    output = open("./tencent/tencent.json","w")
    html = BeautifulSoup(resHmtl,"lxml")

    # css selector
    result = html.select("tr[class='even']")
    result02 = html.select("tr[class='odd']")
    result += result02

    items = []

    for site in result:
        item = {}
        name = site.select("td a")[0].get_text()
        detailLink = site.select("td a")[0].attrs["href"]
        catalog = site.select("td")[1].get_text()
        recruitNumber = site.select("td")[2].get_text()
        workLocation = site.select("td")[3].get_text()
        publishTime = site.select("td")[4].get_text()

        item['name'] = name
        item['detailLink'] = url + detailLink
        item['catalog'] = catalog
        item['recruitNumber'] = recruitNumber
        item['workLocation'] = workLocation
        item['publishTime'] = publishTime
        print(item)
        items.append(item)

    # 禁用ASCII编码，使用utf-8
    line = json.dumps(items,ensure_ascii=False)
    output.write(str(line.encode("utf-8")))
    output.close()

if __name__ == "__main__":
    tencent()
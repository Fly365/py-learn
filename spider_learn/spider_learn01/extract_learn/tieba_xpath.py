# -*- coding: utf-8 -*-

import os,urllib,urllib.request
from lxml import etree

class Spider:
    def __init__(self):
        self.tiebaName = input("请输入访问贴吧名称:")
        self.beginPage = input("输入起始页:")
        self.endPage = input("请输入终止页：")

        self.url = "http://tieba.baidu.com/f"
        self.ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        # 图片编号
        self.userName = 1

    def tiebaSpider(self):
        for page in range(int(self.beginPage),int(self.endPage) + 1):
            pn = (page - 1) * 50
            word = {'pn':pn, 'kw':self.tiebaName}

            word = urllib.parse.urlencode(word)
            myUrl = self.url + "?" + word

            links = self.loadPage(myUrl)

    def loadPage(self, url):
        req = urllib.request.Request(url,headers=self.ua_header)
        html = urllib.request.urlopen(req).read()

        # 解析HTML为 HTML文档
        selector = etree.HTML(html)

        links = selector.xpath("//div[@class='threadlist_lz clearfix']/div/a/@href")

        for link in links:
            link = "http://tieba.baidu.com" + link
            self.loadImages(link)

    def loadImages(self, link):
        req = urllib.request.Request(link,headers=self.ua_header)
        html = urllib.request.urlopen(req).read()

        selector = etree.HTML(html)
        imagesLinks = selector.xpath("//img[@class='BDE_Image']/@src")
        for imagesLink in imagesLinks:
            self.writeImages(imagesLink)

    def writeImages(self, imagesLink):
        print(imagesLink)
        print("正在存储文件 %d ...." %self.userName)
        file = open("./images/" + str(self.userName) + ".png","wb")
        images = urllib.request.urlopen(imagesLink).read()
        file.write(images)

        file.close()
        self.userName += 1

if __name__ == "__main__":
    mySpider = Spider()
    mySpider.tiebaSpider()


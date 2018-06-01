# -*- coding: utf-8 -*-
import scrapy
from ..items import SinaspiderItem
import os

class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        items = []

        parentUrls = response.xpath("//div[@id='tab01']/div/h3/a/@href").extract()
        parentTitle = response.xpath("//div[@id='tab01']/div/h3/a/text()").extract()

        subUrls = response.xpath("//div[@id='tab01']/div/ul/li/a/@href").extract()
        subTitle = response.xpath("//div[@id='tab01']/div/url/li/a/text()").extract()

        # 所有大类
        for i in range(0,len(parentTitle)):
            #指定大类目录路径和目录名
            parentFilename = "./data/" + parentTitle[i]
            # 如果目录不存在，则创建
            if(not os.path.exists(parentFilename)):
                os.makedirs(parentFilename)

            # 抓取小类
            for j in range(0,len(subUrls)):
                item = SinaspiderItem()

                item["parentTitle"] = parentTitle[i]
                item["parentUrls"] = parentUrls[i]

                #检查小类的URL是否以同类别大类URL开头，如果是返回True
                # (sports.sina.com.cn 和 sports.sina.com.cn/nba)
                if_belong = subUrls[j].startwith(item["parentUrls"])

                #如果是大类，存储目录放在本大类目录下
                if(if_belong):
                    subFilename = parentFilename + "/" + subTitle[j]
                    if(not os.path.exists(subFilename)):
                        os.makedirs(subFilename)

                    #存储小类信息
                    item["subUrls"] = subUrls[j]
                    item["subTitle"] = subTitle[j]
                    item["subFilename"] = subFilename

                    items.append(item)

        # 发送每个小类下子链接URL的Request请求，得到Response后连同包含数据meta数据一同交给回调函数 detail_parse方法
        for item in items:
            yield scrapy.Request(url = item["sonUrls"],meta={"meta_2":item}, callback=self.detail_parse)

    def detail_parse(self,response):
        item = response.meta["meta_2"]
        content = ""
        head = response.xpath("//h1[@id='main_title']/text()")
        content_list = response.xpath("//div[@id='artibody']/p/text()").extract()

        # 将p标签文本内容合并一起
        for content_one in content_list:
            content += content_one

        item["head"] = head
        item["content"] = content

        yield item



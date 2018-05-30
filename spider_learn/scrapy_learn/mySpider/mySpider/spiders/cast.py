# -*- coding: utf-8 -*-
import scrapy
from scrapy_learn.mySpider.mySpider.items import CastItem


class CastSpider(scrapy.Spider):
    name = 'cast'
    allowed_domains = ['cast.cn']
    start_urls = ['http://cast.cn/']

    # 1. 负责解析返回的网页数据，提取结构化数据(生成item)
    # 2. 生成下一页的URL请求
    def parse(self, response):
        #filename = "tea.html"
        #open(filename,"w").write(response.body)
        items = []
        for each in response.xpath("//div[@class='li_txt']"):
            # 将获取数据封装到对象
            item = CastItem()
            # extract() 方法返回的都是Unicode字符串
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()

            # xpath返回的是包含一个元素的列表
            item["name"] = name[0]
            item["title"] = title[0]
            item["info"] = info[0]

            items.append(item)
        return items

# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DouyuspiderItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['capi.douyucdn.cn']

    offset = 0
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    start_urls = [url + str(offset)]

    def parse(self, response):
        # 返回从json 里获取 data段数据集合
        data = json.loads(response.text)["data"]

        for each in data:
            item = DouyuspiderItem()
            item["name"] = each["nickname"]
            item["imgsUrls"] = each["vertical_src"]
            yield  item

        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

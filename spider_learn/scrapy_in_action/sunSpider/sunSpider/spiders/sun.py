# -*- coding: utf-8 -*-
import scrapy
from ..items import SunspiderItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
import time


class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    #每一页的匹配规则
    pagelink = LinkExtractor(allow=('type=4'))
    # 每个帖子的匹配规则
    contentLink = LinkExtractor(allow=r"/html/question/\d+/\d+.shtml")

    rules = [
        # 该实例需要调用deal_links方法处理每个页面里的链接
        Rule(pagelink,process_links="detail_links",follow=True),
        Rule(contentLink,callback="parse_item")
    ]

    # 重新处理每个页面里的链接，将链接里的 'Type&type=4?page=xxx'替换为 'Type?type=4&page=xxx'
    # （或者是Type&page=xxx?type=4’替换为‘Type?page=xxx&type=4’），否则无法发送这个链接
    def detail_links(self,links):
        for link in links:
            link.url = link.url.replace("?","&").replace("Type&","Type?")
            print(link.url)
        return links

    def parse_item(self,response):
        print(response.url)
        item = SunspiderItem()
        item["title"] = response.xpath("//div[contains(@class,'pagecenter p3)']//strong/text()").extract[0]
        item["number"] = item["title"].split(" ")[-1].split(":")[-1]

        # 文字内容
        content = response.xpath("//div[@class='contentext']/text()").extract()
        # 如果没有内容，则获取没有图片情况下的文字内容列表
        if len(content) == 0:
            content = response.xpath("//div[@class='c1 text14_2']/text()").extract()
            # content为列表，通过join拼接为字符串，并去除首尾空格
            item["content"] = "".join(content).strip()
        else:
            item["content"] = "".join(content).strip()

        # 链接
        item["url"] = response.url

        yield item

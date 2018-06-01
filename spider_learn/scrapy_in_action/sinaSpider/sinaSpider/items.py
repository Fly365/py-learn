# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SinaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 大类
    parentTitle = scrapy.Field()
    parentUrls = scrapy.Field()

    # 小类标题及URL
    subTitle = scrapy.Field()
    subUrls = scrapy.Field()

    # 小类目录存放路径
    subFilename = scrapy.Field()

    # 小类下的子链接
    sonUrls = scrapy.Field()

    #文章标题合内容
    head = scrapy.Field()
    content = scrapy.Field()

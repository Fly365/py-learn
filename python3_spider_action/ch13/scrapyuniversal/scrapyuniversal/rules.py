# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

rules = {
    'china': (
        Rule(LinkExtractor(allow='articles\/.*\.html',
             restrict_xpaths='//div[@id="rank-defList"]//div[@class="item_con"]'),
             callback='parse_item'),
        #Rule(LinkExtractor(restrict_xpaths='//div[@class="pages"]//ul/a[last()]'))
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pages"]//a[contains(.,"下一页")]'))
    )
}
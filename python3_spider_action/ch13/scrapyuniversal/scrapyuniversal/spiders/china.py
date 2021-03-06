# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversal.items import NewsItem
from scrapyuniversal.loaders import ChinaLoader


class ChinaSpider(CrawlSpider):
    name = 'china'
    allowed_domains = ['tech.china.com']
    start_urls = ['https://tech.china.com/articles/']

    rules = (
        Rule(LinkExtractor(allow='articles\/.*\.html',
             restrict_xpaths='//div[@id="rank-defList"]//div[@class="item_con"]'),
             callback='parse_item'),
        #Rule(LinkExtractor(restrict_xpaths='//div[@class="pages"]//ul/a[last()]'))
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pages"]//a[contains(.,"下一页")]'))
    )

    def parse_item(self, response):
        '''
        item = NewsItem()
        item['title'] = response.xpath('//h1[@id="chan_newsTitle"]/text()').extract_first()
        item['url'] = response.url
        item['text'] = ''.join(response.xpath('//div[@id="chan_newsDetail"]/text()').extract()).strip()
        item['datatime'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first('(\d+-\d+-\d+\s\d+:\d+:\d+)')
        item['source'] = response.xpath('//div[@id="chan_newsInfo"]/text()').re_first(' 来源:(.*)').strip()
        item['website'] = '中华网'
        yield item
        '''
        loader = ChinaLoader(item=NewsItem(), response=response)
        loader.add_xpath('title', '//h1[@id="chan_newsTitle"]/text()')
        loader.add_xpath('url', response.url)
        loader.add_xpath('text', '//div[@id="chan_newsDetail"]/text()')
        loader.add_xpath('datetime', '//div[@id="chan_newsInfo"]/text()', re='(\d+-\d+-\d+\s\d+:\d+:\d+)')
        loader.add_xpath('source', '//div[@id="chan_newsInfo"]/text()', re=' 来源:(.*)')
        loader.add_value('website', '中华网')
        yield loader.load_item()
# -*- coding: utf-8 -*-
from scrapy import Request,FormRequest
from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from ..items import ZhihuspiderItem


class ZhihuSpider(CrawlSpider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    rules = (
        Rule(LinkExtractor(allow=('/question/\d+#.*?',)), callback='parse_page', follow=True),
        Rule(LinkExtractor(allow=('/question/\d+',)), callback='parse_page', follow=True),
    )

    headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
    "Connection": "keep-alive",
    "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    "Referer": "http://www.zhihu.com/"
    }

    # 重写爬虫类方法，实现自定义请求，运行成功后调用callback回调函数
    def start_requests(self):
        return [Request("https://www.zhihu.com/signup", meta= {"cookiejar":1}, callback=self.post_login)]

    def post_login(self, response):
        print("preparing login")
        # 用于抓取请求网页后返回中的_xsrf 字段的文字，用于成功提交表单
        xsrf = Selector(response).xpath("//input[@name='_xsrf']/@value").extract()[0]
        print(xsrf)
        # formRequest.from_response是scrapy提供的一个函数，用于POST表单
        # 登录成功后，会调用 after_login 回调函数
        return [FormRequest.from_response(response,
                                          meta = {"cookiejar":response.meta["cookiejar"]},
                                          headers = self.headers,
                                          formdata= {
                                              "_xsrf":xsrf,
                                              "email": "1095511864@qq.com",
                                              "password":"123456"
                                          },
                                          callback = self.after_login,
                                          dont_filter = True)]

    def after_login(self,response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)























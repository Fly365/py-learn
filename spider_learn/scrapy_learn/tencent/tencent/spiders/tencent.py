from ..items import TencentItem
import scrapy
import re

class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["hr.tencent.com"]
    start_urls = ["http://hr.tencent.com/position.php?&start=0#a"]

    def parse(self, response):
        for each in response.xpath("//*[@class='even']"):
            item = TencentItem()
            name = each.xpath("./td[1]/a/text()").extract()[0]
            detailLink = each.xpath("./td[1]/a/@href").extract()[0]
            positionInfo = each.xpath("./td[2]/text()").extract()[0]
            peopleNumber = each.xpath("./td[3]/text()").extract()[0]
            workLocation = each.xpath("./td[4]/text()").extract()[0]
            publishTime = each.xpath("./td[5]/text()").extract()[0]

            item["name"] = name
            item["detailLink"] = detailLink
            item["positionInfo"] = positionInfo
            item["peopleNumber"] = peopleNumber
            item["workLocation"] = workLocation
            item["publishTime"] = publishTime

            curPage = re.search("(\d+)",response.url).group(1)
            page = int(curPage) + 10
            url = re.sub("\d+", str(page), response.url)

            # 发送新的URL请求加入待爬队列，并调用回调函数 self.parse
            yield scrapy.Request(url, callback= self.parse)

            # 将获取的数据交给pipel
            yield item


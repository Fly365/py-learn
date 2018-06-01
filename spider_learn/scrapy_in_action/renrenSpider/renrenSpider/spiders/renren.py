import scrapy

# 主要为模拟登录

class Renren1Spider(scrapy.Spider):
    name = "renren1"
    allowed_domains = ["renren.com"]

    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        # FormRequest是scrapy发送POST请求方法
        yield scrapy.FormRequest(
            url = url,
            formdata={"email" : "", "password" : ""},
            callback=self.parse_page
        )

    def parse_page(self,response):
        with open("mao2.html","w") as filename:
            filename.write(response.body)

class Renren2Spider(scrapy.Spider):
    name = "renren1"
    allowed_domains = ["renren.com"]
    start_urls = ("http://www.renren.com/PLogin.do")

    #处理start_urls里登录URL响应内容，提取登录需要的参数(如需要的话)
    def parse(self, response):
        #提取登录需要的参数
        #_xsrf = response.xpath("//_xsrf").extract[0]

        #发送请求数据，并调用指定回调函数处理
        yield scrapy.FormRequest.from_response(
            response,
            formdata={"email": "", "password": ""},  # , "_xsrf" = _xsrf},
            callback = self.parse_page
        )

    # 获取登录成功状态，访问需要登录后才能访问的页面
    def parse_page(self, response):
        url = "http://www.renren.com/422167102/profile"
        yield scrapy.Request(url,callback=self.parse_newpage)

    def parse_newpage(self,response):
        with open("xiao.html","w") as filename:
            filename.write(response.body)


class Renren3Spider(scrapy.Spider):
    name = "renren1"
    allowed_domains = ["renren.com"]
    start_urls = (
        'http://www.renren.com/111111',
        'http://www.renren.com/222222',
        'http://www.renren.com/333333',
    )

    cookies = {
    "anonymid" : "ixrna3fysufnwv",
    "_r01_" : "1",
    "ap" : "327550029",
    "JSESSIONID" : "abciwg61A_RvtaRS3GjOv",
    "depovince" : "GW",
    "springskin" : "set",
    "jebe_key" : "f6fb270b-d06d-42e6-8b53-e67c3156aa7e%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1484060607478%7C1%7C1486198628950",
    "t" : "691808127750a83d33704a565d8340ae9",
    "societyguester" : "691808127750a83d33704a565d8340ae9",
    "id" : "327550029",
    "xnsid" : "f42b25cf",
    "loginfrom" : "syshome"
    }

    # 重写Spider类的start_requests方法，附带cookie值，发送POST请求
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url,cookies=self.cookies,callback=self.parse_page)

    def parse_page(self,response):
        with open("deng.html","w") as filename:
            filename.write(response.body)



























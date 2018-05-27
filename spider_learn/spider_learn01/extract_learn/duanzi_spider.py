import urllib.request

class Spider:
    '''
        内涵段子类
    '''
    def loadPage(self,page):
        '''
        :brier 定义一个URL请求页面的方法
        :param page: 需要请求的第几页
        :return: 返回页面的HTML
        '''
        url = "http://www.neihan8.com/article/list_5_" + str(page) + ".html"
        user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
        headers = {"User-Agent":user_agent}
        req = urllib.request.Request(url,headers=headers)
        response = urllib.request.urlopen(req)
        #html = response.read().decode("utf-8")
        # 如果原URL地址为gbk，输出为utf-8
        #html = response.read().decode('gbk').encode("utf-8")
        html = response.read().decode('gbk')
        return html

if __name__ == "__main__":
    mySpider = Spider()
    html = mySpider.loadPage(1)
    print(html)
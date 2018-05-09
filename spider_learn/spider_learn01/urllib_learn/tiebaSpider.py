import urllib.request,urllib


def loadPage(fullurl, filename):
    print("正在下载" + filename)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    request = urllib.request.Request(fullurl,headers=headers)
    response = urllib.request.urlopen(request)
    return response.read().decode("utf-8")


def writeFile(html, filename):
    print("正在存储" + filename)
    with open(filename,'w') as f:
        f.write(html)
    print("-" * 20)


def tiebaSpider(url, beginPage, endPage):
    '''
    作用：负责处理URL，分配每个URL去发送请求
    :param url: 需要处理的第一个url
    :param beginPage:爬虫执行的起始页面
    :param endPage:爬虫执行的截止页面
    :return:
    '''
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)

        html = loadPage(fullurl,filename)
        writeFile(html,filename)


if __name__ == '__main__':
    kw = input("请输入需要爬取的贴吧:")
    beginPage = int(input("起始页面:"))
    endPage = int(input("结束页:"))

    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw":kw})

    # 组合后URL示例http://tieba.baidu.com/f?kw=lol
    url = url + key

    tiebaSpider(url,beginPage,endPage)
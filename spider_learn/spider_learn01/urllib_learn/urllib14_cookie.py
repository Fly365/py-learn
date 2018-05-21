import urllib.request

'''获取一个有登录信息的cookie模拟登录'''

# 构建一个已经登录过用户headers信息
headers = {
    "Host": "www.renren.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",

    # 便于终端阅读，表示不支持压缩文件
    # Accept-Encoding: gzip, deflate, sdch,

    # 重点：这个Cookie是保存了密码无需重复登录的用户的Cookie，这个Cookie里记录了用户名，密码(通常经过RAS加密)
    "Cookie": "anonymid=ixrna3fysufnwv; depovince=GW; _r01_=1; JSESSIONID=abcmaDhEdqIlM7riy5iMv; jebe_key=f6fb270b-d06d-42e6-8b53-e67c3156aa7e%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1484060607478%7C1%7C1484060607173; jebecookies=26fb58d1-cbe7-4fc3-a4ad-592233d1b42e|||||; ick_login=1f2b895d-34c7-4a1d-afb7-d84666fad409; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=99e54330ba9f910b02e6b08058f780479; ap=327550029; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20140529/1055/h_main_9A3Z_e0c300019f6a195a.jpg; t=214ca9a28f70ca6aa0801404dda4f6789; societyguester=214ca9a28f70ca6aa0801404dda4f6789; id=327550029; xnsid=745033c5; ver=7.0; loginfrom=syshome"
}

# 通过headers里头报头信息(主要是cookie信息)，构建request对象
request = urllib.request.Request("http://www.renren.com/",headers=headers)
# 直接访问renren主页，服务器会根据headers报头信息(主要是cookie信息)，判断是一个已经登录用户，病返回页面
response = urllib.request.urlopen(request)

print(response.read().decode("utf-8"))
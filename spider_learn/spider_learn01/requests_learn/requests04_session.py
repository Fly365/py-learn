import requests

session = requests.session()

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}

# 发送附带账户信息请求，并获取登录后的cookie值，保存在session
session.post("http://www.renren.com/PLogin.do",data=data)

response = session.get("http://www.renren.com/410043129/profile")

print(response.text)
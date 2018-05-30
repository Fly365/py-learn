import requests,time,pytesseract
from PIL import Image
from bs4 import BeautifulSoup

def captcha(data):
    with open("captcha.jpg","wb") as fp:
      fp.write(data)

    time.sleep(1)
    img = Image.open("captcha.jpg")
    text = pytesseract.image_to_string(img)
    print("OCR识别后的验证码位:" + text)
    command = input("请输入Y表示同意使用，按其他建自行重新输入:")
    if (command == "Y" or command == "y"):
        return text
    else:
        return input("请输入验证码:")

def zhihuLogin(username,passwd):
    #构建一个保存cookie值的session对象
    session = requests.Session()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    #先获取页面信息，找到需要POST的数据(并且已记录当前页面的cookie)
    html = session.get("https://www.zhihu.com/#signin",headers=headers).content
    #找到name属性值位 _xsrf 的input标签，取出value里的值
    _xsrf = BeautifulSoup(html,'lxml').find("input",attrs={"name":"_xsrf"}).get("value")

    #取出验证码，r后面的值是Unix时间戳，time.time()
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)
    response = session.get(captcha_url,headers=headers)

    data = {
        "_xsrf":_xsrf,
        "email":username,
        "password":passwd,
        "remember_me":True,
        "captcha": captcha(response.content)
    }

    response = session.post("https://www.zhihu.com/login/email",data=data,headers=headers)
    print(response.text)

    response = session.get("https://www.zhihu.com/people/maozhaojun/activities",headers=headers)
    print(response.text)

if __name__ == "__main__":
    zhihuLogin('xxxx@qq.com','ALAxxxxIME')
# encoding:utf8

import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .chaojiying import Chaojiying

EMAIL = ''
PASSWORD = ''

CHAOJIYING_USERNAME = ''
CHAOJIYING_PASSWORD = ''
CHAOJIYING_SOFT_ID = 893590
CHAOJIYING_KIND = 9102

class CrackTouClick():
    def __init__(self):
        self.url = ''
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD
        self.chaojiying = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)

    def __del__(self):
        self.browser.close()

    def oopen(self):
        """打开网页输入用户名密码"""
        self.browser.get(self.url)
        email = self.wait.until(EC.presence_of_element_located((By.ID, 'email')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        email.send_keys(self.email)
        password.send_keys(self.password)

    def get_touclick_button(self):
        """获取初始验证按钮"""
        button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'touclick-hod-wrap')))
        return button

    def get_touclick_element(self):
        """获取验证码对象"""
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'touclick-pub-content')))
        return element

    def get_position(self):
        """获取验证码位置"""
        element = self.get_touclick_element()
        time.sleep(2)
        location = element.location
        size = element.size
        top, bottom, left, right = location['y'], location['y'] + size[
            'height'], location['x'], location['x'] + size['width']
        return (top, bottom, left, right)

    def get_screenshot(self):
        """获取网页截图"""
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_touclick_image(self, name='captcha.png'):
        """获取验证码图片"""
        pass
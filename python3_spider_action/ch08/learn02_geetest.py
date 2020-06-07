# encoding=utf8
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from io import BytesIO
from PIL import Image

EMAIL = '1234567@qq.com'
PASSWORD = '1234567'
BORDER = 6
INIT_LEFT = 60

class CrackGeetest():
    def __init__(self):
        self.url = 'https://auth.geetest.com/login/'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD
        
    def __del__(self):
        self.browser.close()

    def get_geetest_button(self):
        """
        获取初始验证按钮
        :return: 按钮对象
        """
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_radar_tip')))
        return button

    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_canvas_img')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
        return (top, bottom, left, right)

    def get_geetest_img(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        print(' 验证码位置 ', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        return captcha

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_slider(self):
        """
        获取滑块
        :return:  滑块对象
        """
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    def is_pixel_equal(self, img1, img2, x, y):
        """
        判断两个像素是否相同
        :param img1: 图片1
        :param img2: 图片2
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        """
        # 取两个图片的像素点
        pixel1 = img1.load()[x, y]
        pixel2 = img2.load()[x, y]
        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def get_gap(self, img1, img2):
        """
        获取缺口偏移量
        两张图片有两处明显不同的地方：一个就是待拼合的滑块，一个就是缺口。
        滑块的位置会出现在左边位置，缺口会出现在与滑块同一水平线的位置，
        所以缺口一般会在滑块的右侧。如果要寻找缺口，直接从滑块右侧寻找即可。
        我们直接设置遍历的起始横坐标为 60，也就是从滑块的右侧开始识别，
        这样识别出的结果就是缺口的位置。
        :param img1: 不带缺口图片
        :param img2: 带缺口图片
        """
        left = 60
        for i in range(left, img1.size[0]):
            for j in range(img1.size[1]):
                if not self.is_pixel_equal(img1, img2, i, j):
                    left = i
                    return left
        return left

    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        滑块滑动的加速度用 a 来表示，当前速度用 v 表示，初速度用 v0 表示，
        位移用 x 表示，所需时间用 t 表示
        x = v0 * t + 0.5 * a * t * t
        v = v0 + a * t
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正 2
                a = 2
            else:
                # 加速度为负 3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度 v = v0 + at
            v = v0 + a * t
            # 移动距离 x = v0t + 1/2 * a * t^2
            move = v0 * t + 1/2 * a * t * t
            #当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track

    def move_to_gap(self, slider, tracks):
        """
        拖动滑块到缺口
        :param slider: 滑块
        :param tracks: 轨迹
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
            time.sleep(0.5)
            ActionChains(self.browser).release().perform()

    def login(self):
        submit = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-btn')))
        submit.click()
        time.sleep(10)
        print(' 登录成功 ')      

    def open(self):
        """
        打开网页输入用户名密码
        :return： None
        """
        self.browser.get(self.url)
        # //*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[1]/input
        email = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[1]/div/div[1]/input')))
        password = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[2]/div/div[1]/input')))
        email.send_keys(self.email)
        password.send_keys(self.password)
        
    def crack(self):
        self.open()
        # 点击验证按钮
        button = self.get_geetest_button()
        button.click()
        success = self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_success_radar_tip_content'), '验证成功'))
        print(success)
        # 登录一次，只有登录失败时，才继续弹出验证码
        self.login()
        # 获取验证码图片
        img1 = self.get_geetest_img('captcha1.png')
        # 点按呼出缺口
        slider = self.get_slider()
        slider.click()
        # 获取带缺口的验证码图片
        img2 = self.get_geetest_img("captcha2.png")
        # 获取缺口位置
        gap = self.get_gap(img1, img2)
        print('缺口位置', gap)
        # 减去缺口位移
        gap -= BORDER
        # 获取移动轨迹
        track = self.get_track(gap)
        print('滑动轨迹', track)
        # 拖动滑块
        self.move_to_gap(slider, track)

        success = self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME,'geetest_success_radar_tip_content'), '验证成功'))
        print(success)

        if not success:
            self.crack()
        else:
            self.login()

if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()



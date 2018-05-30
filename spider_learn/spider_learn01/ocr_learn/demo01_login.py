from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.douban.com")

# 输入账户密码
driver.find_element_by_id("form_email").send_keys("xxxxx@xxxx.com")
driver.find_element_by_name("form_password").send_keys("xxxxxxxx")

# 模拟点击登录
driver.find_element_by_xpath("//input[@class='bn-submit']").click()

time.sleep(3)

driver.save_screenshot("douban.png")

with open("douban.html","w") as file:
    file.write(driver.page_source)

driver.quit()




















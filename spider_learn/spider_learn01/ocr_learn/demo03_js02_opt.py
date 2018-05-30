from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=")

#向下滚动10000像素
js = "document.body.scrollTop=10000"
time.sleep(3)

driver.execute_script(js)

time.sleep(10)

driver.quit()
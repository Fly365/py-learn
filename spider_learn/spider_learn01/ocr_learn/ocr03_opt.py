import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")

#等待页面加载完成
time.sleep(5)

imgList = []

#当向右箭头可以点击时，开始翻页
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    # 获取已加载新页面(一次可以加载多个页面，但是重复的页面不能加载到集合中)
    pages = driver.find_element_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        img = page.get_attribute("src")
        imgList.append(img)
driver.quit()

#用tesseract处理收集的图片URL链接
for img in sorted(imgList):
    urlretrieve(img,"page.jpg")
    p = subprocess.Popen(["tesseract","page.jpg","page"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    f = open("page.txt","r")
    p.wait()
    print(f.read())
    f.close()


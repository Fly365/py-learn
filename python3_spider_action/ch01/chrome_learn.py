# encoding=utf8

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
print(browser.current_url)
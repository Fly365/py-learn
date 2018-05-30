from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

#给搜索输入框标红的JavaScript脚本
js = "var q=document.getElementById(\"kw\");q.style.border=\"2px solid red\";"

# 调用给搜索输入框标红js脚本
driver.execute_script(js)

driver.save_screenshot("redbaidu.png")

#js隐藏元素，将获取图片元素隐藏
img = driver.find_element_by_xpath("//*[@id='lg']/img")
driver.execute_script("$(arguments[0]).fadeOut()",img)

#向下滚动到页面底部
driver.execute_script("$('.scroll_top').click(function(){$('html,body').animate({scrollTop: '0px'}, 800);});")

driver.quit()
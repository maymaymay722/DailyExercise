# coding = utf-8
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
# print browser.title # 把页面title 打印出来 print
#print browser.current_url()  #打印url
browser.find_element_by_id("kw").send_keys("乃万")
browser.find_element_by_id("su").click()
#time.sleep(10)
browser.implicitly_wait(10)
browser.find_element_by_link_text("乃万_百度百科").click()

# browser.implicitly_wait(20) #智能等待30秒
# browser.find_element_by_id("kw").send_keys("虞书欣")
# browser.find_element_by_id("su").click()

# browser.find_element_by_id("kw").send_keys("虞书欣")
# time.sleep(3)
# browser.find_element_by_id("kw").clear()
# browser.find_element_by_id("kw").send_keys("赵小棠")
# time.sleep(3)
# browser.find_element_by_id("su").submit()

#browser.find_element_by_id("su").click()
time.sleep(6)
browser.quit()
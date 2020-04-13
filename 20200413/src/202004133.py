from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")

#浏览器最大化
#browser.maximize_window()

#browser.find_element_by_link_text("hao123").click()
#time.sleep(6)

browser.find_element_by_id("kw").send_keys("虞书欣")
browser.find_element_by_id("su").click()
time.sleep(8)

js="var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)
time.sleep(6)

js="var q=document.documentElement.scrollTop=0"
browser.execute_script(js)
time.sleep(6)
#browser.back()
#time.sleep(6)
#browser.forward()
#time.sleep(6)

#设置浏览器宽、高
#browser.implicitly_wait(10)

# t=browser.title
# print(t)
# url=browser.current_url
# print(url)
# time.sleep(4)
browser.quit()
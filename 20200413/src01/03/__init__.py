from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time,os

driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('level_locate.html')
driver.get(file_path)
#driver.implicitly_wait(10)
# 把驱动传进去，等待10秒
#WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id("Link1"))

#点击 Link1 链接（弹出下拉列表）
driver.find_element_by_link_text('Link1').click()
driver.implicitly_wait(10)

#找到 id 为dropdown1 的父元素
list=driver.find_element_by_id("dropdown1").find_elements_by_link_text('Action')
webdriver.ActionChains(driver).move_to_element(list[0]).perform()
time.sleep(6)
driver.quit()



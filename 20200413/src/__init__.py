from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("虞书欣")
time.sleep(3)

su=driver.find_element_by_id("su")
#ActionChains(driver).context_click(su).perform()
ActionChains(driver).double_click(su).perform()

#定位元素的原位置
element = driver.find_element_by_id("s_btn_wr")
#定位元素要移动到的目标位置
target = driver.find_element_by_class_name("btn")
#执行元素的移动操作
ActionChains(driver).drag_and_drop(element, target).perform()

time.sleep(4)
driver.quit()
from selenium import webdriver
import time,os

driver=webdriver.Chrome()
file_path='file:///'+os.path.abspath("frame.html")
driver.get(file_path)
driver.implicitly_wait(10)
driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("虞书欣")
driver.find_element_by_id("su").click()

time.sleep(3)
driver.quit()
from selenium import webdriver
import time,os

driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath("send.html")
driver.get(file_path)

driver.find_element_by_xpath("/html/body/input").click()
time.sleep(5)
alert=driver.switch_to.alert
alert.send_keys("虞书欣")
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)
driver.quit()
from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://mail.163.com/")
driver.implicitly_wait(10)
driver.find_element_by_name("email").send_keys("meiyingying0722")
driver.find_element_by_name("password").send_keys("maymay0722may")
driver.find_element_by_id("dologin").click()

time.sleep(10)
driver.quit()
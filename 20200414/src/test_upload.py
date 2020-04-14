from selenium import webdriver
import time
import os

driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('upload.html')
driver.get(file_path)
time.sleep(5)
#定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('D:\\Code\\课件\\测试课件\\测试教程-自动化测试selenium-3.pdf')
time.sleep(5)
driver.quit()

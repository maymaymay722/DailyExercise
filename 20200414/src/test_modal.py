from selenium import webdriver
import time
import os

driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('modal.html')
driver.get(file_path)

#打开对话框
driver.find_element_by_id('show_modal').click()
time.sleep(5)

#点击对话框中的链接
link=driver.find_element_by_id('myModal').find_element_by_id('click').click()
time.sleep(5)

#关闭对话框
buttons=driver.find_element_by_class_name('modal-footer').find_element_by_class_name('btn').click()

time.sleep(5)
driver.quit()
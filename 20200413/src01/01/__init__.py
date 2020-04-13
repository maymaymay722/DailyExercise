from selenium import webdriver
import time,os

driver=webdriver.Chrome()
file_path='file:///'+os.path.abspath("01/checkbox.html")
driver.get(file_path)

inputs=driver.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute('type')=="checkbox":
        input.click()
        time.sleep(3)
time.sleep(6)
driver.quit()
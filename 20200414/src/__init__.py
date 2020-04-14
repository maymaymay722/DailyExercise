from selenium import webdriver
import time,os


driver=webdriver.Chrome()
file_path="file:///"+os.path.abspath("checkbox.html")
driver.get(file_path)
driver.implicitly_wait(10)

inputs=driver.find_elements_by_tag_name("input")
for input in inputs:
    if input.get_attribute('type')=="checkbox":
        input.click()
time.sleep(6)
driver.quit()



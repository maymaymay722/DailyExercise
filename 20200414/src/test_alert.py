from selenium import webdriver
import time
import os

driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath("alert.html")
driver.get(file_path)

# 点击链接弹出alert
driver.find_element_by_id("tooltip").click()
driver.implicitly_wait(10)

#接受警告信息
alert=driver.switch_to.alert
#time.sleep(6)
print(alert.text)
#driver.dismiss()
time.sleep(10)
driver.quit()

# #得到文本信息打印
# print alert.text
# #取消对话框（如果有的话）
# alert.dismiss()
# #输入值
# alert.send_keys("hello word")
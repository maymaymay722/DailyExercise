from selenium import webdriver
import time
import unittest
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

class Baidu2(unittest.TestCase):

    #test fixture，初始化环境
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url="http://baidu.com/"
        self.verficationErrors=[]
        self.accept_next_alert=True

    #测试用例，必须以test开头

    def test_baidusearch(self):
        driver=self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"selenium")
        driver.find_element_by_id("su").click()
        driver.find_element_by_id("su").click()

    #判断element是否存在，可删除
    def is_element_present(self,how,what):
        try:self.driver.find_element(by=how,value=what)
        except NoSuchElementException as e:return False
        return True

    #判断alert是否存在，可删除
    def is_alert_present(self):
        try:self.driver.switch_to.alert
        except NoAlertPresentException as e:return False
        return True

    #关闭alert，可删除
    def close_alert_and_get_its_text(self):
        try:
            alert=self.driver.switch_to.alert
            alert_text=alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:self.accept_next_alert=True

    #text fixture,清除环境
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verficationErrors)

    if __name__=="__main__":
       unittest.main()
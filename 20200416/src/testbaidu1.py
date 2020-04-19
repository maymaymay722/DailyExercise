from selenium import webdriver
import unittest,time,os

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class Baidu1(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url="http://www.baidu.com/"
        self.verficationErrors=[]
        self.accept_next_alert=True

    @unittest.skip("skipping")
    def test_baidusearch(self):
        driver=self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"测试")
        driver.find_element_by_id("su").click()

    def test_hao(self):
        driver=self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_link_text("hao123").click()
        self.assertEqual(u"hao123_上网从这里开始",driver.title)

    def is_element_present(self, how, what):
        try:self.driver.find_element(by=how,value=what)
        except NoSuchElementException as e:return False
        return True

    #判断alert是否存在，可删除
    def is_alert_present(self):
        try:self.driver.switch_to.alert
        except NoAlertPresentException as e:return False
        return True
        
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

    #test fixture 清除环境
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verficationErrors)

    if __name__=="__main__":
        unittest.main()

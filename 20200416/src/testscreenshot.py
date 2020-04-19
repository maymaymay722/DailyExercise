from selenium import webdriver
import time,os
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class Baidu1(unittest.TestCase):

    #test fixture，初始化环境
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url="http://www.baidu.com"
        self.verficationErrors=[]
        self.accept_next_alert=True

    #测试用例，必须test开头
    def test_hao(self):
        driver=self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_link_text("hao123").click()
        time.sleep(3)
        try:
            self.assertEquals(u'hao_上网从这里开始',driver.title)
        except:
            self.savescreenshot(driver,'hao.png')

     #判断 element 是否存在，可删除
    def is_element_present(self,how,what):
        try:self.driver.find_element(by=how,value=what)
        except NoSuchElementException as e:return False
        return True

    #判断 alert是否存在，可删除
    def is_alert_present(self):
        try:self.drievr.switch_to.alert
        except NoAlertPresentException as e:return False
        return True

    #关闭 alert，可删除
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

    #test fixture，清除环境
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verficationErrors)

    #异常捕捉与错误截图
    def savescreenshot(self,driver,file_name):
        if not os.path.exists('./image'):
            os.makedirs('./image')
        now=time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time()))
        driver.get_screenshot_as_file('./image/'+now+'-'+file_name)
        time.sleep(3)

if __name__=="__main__":
    unittest.main()

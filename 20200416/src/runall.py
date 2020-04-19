import sys,os

from selenium import webdriver
import time
import unittest
import HTMLTestRunner

#导入testbaidu1,testbaidu2
from src import testbaidu1
from src import testbaidu2

#手工添加案例到套件
def createsuite():

    # 将测试用例加入到测试容器（套件）中   addTest()
    # suite=unittest.TestSuite()
    # suite.addTest(testbaidu1.Baidu1("test_baidusearch"))
    # suite.addTest(testbaidu1.Baidu1("test_hao"))
    # suite.addTest(testbaidu2.Baidu2("test_baidusearch"))
    # return suite

    # makeSuite()
    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(testbaidu1.Baidu1))
    # suite.addTest(unittest.makeSuite(testbaidu2.Baidu2))
    # return suite

    #TestLoader()
    # suite1=unittest.TestLoader().loadTestsFromTestCase(testbaidu1.Baidu1)
    # suite2=unittest.TestLoader().loadTestsFromTestCase(testbaidu2.Baidu2)
    # suite=unittest.TestSuite([suite1,suite2])
    # return suite

    discover=unittest.defaultTestLoader.discover("../src",pattern='testbaidu*.py',top_level_dir=None)
    print(discover)
    return discover

if __name__=="__main__":
    suite=createsuite()
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    curpath=sys.path[0]
    #取当前时间
    now=time.strftime("%Y-%m-%d-%H %M %S",time.locatiome(time.time()))

    if not os.path.exits(curpath+'/resultreport'):
        os.makedirs(curpath+'/resultreport')

    filename=curpath+'/resultreport'+now+'resultreport.html'
    with open(filename,'wb') as fp:
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况',verbosity=2)
        suite=createsuite()
        runner.run(suite)
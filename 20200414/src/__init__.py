import unittest
from selenium import webdriver
import time,os

class chandao(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url="http://127.0.0.1/"

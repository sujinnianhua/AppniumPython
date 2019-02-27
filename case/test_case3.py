# coding=utf-8
import pytest
import unittest
from appium import webdriver
import time
from business.login_business import LoginBusiness


class TestClass(unittest.TestCase):
     @classmethod
     def setUpClass(cls):
         capabilities = {
            "platformName":"Android",
             "deviceName":"127.0.0.1:21503",
             "appPackage":"com.phsxy.footballbaby.test",
             "appActivity":"com.phsxy.footballbaby.activity.welcome.SplashActivity",
             #屏蔽软键盘
             "unicodeKeyboard":True,
             "resetKeyboard":True,
         }
         cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
         time.sleep(10)
         cls.login_business = LoginBusiness(cls.driver)
     def setUp(self):
         print "this is setup"
     def test_login(self):
         self.login_business.login_pass()
         self.driver.quit()
     def tearDown(self):
        print "this is tearDown1111111"




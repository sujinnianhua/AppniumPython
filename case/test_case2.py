# #coding=utf-8
# import time
# import unittest
# import HTMLTestRunner
# from appium import webdriver
# from business.login_business import LoginBusiness
# class CaseTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         capabilities = {
#             "platformName":"Android",
#             "deviceName":"127.0.0.1:21503",
#             "appPackage":"com.phsxy.footballbaby.test",
#             "appActivity":"com.phsxy.footballbaby.activity.welcome.SplashActivity",
#             #屏蔽软键盘
#             "unicodeKeyboard":True,
#             "resetKeyboard":True,
#         }
#         cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
#         time.sleep(10)
#         cls.login_business = LoginBusiness(cls.driver)
#     def setUp(self):
#         print "this is setup"
#     def test_login(self):
#         self.login_business.login_pass()
#     def tearDown(self):
#         print "this is tearDown"
#
# if __name__ == '__main__':
#     print "111111111111"
#     suit = unittest.TestSuite()
#     suit.addTest(CaseTest("test_login"))
#     # suit.addTest(CaseTest("test_userError"))
#     unittest.TextTestRunner().run(suit)
#     html_file = "D:/workplace/AppniumPython/report/report.html"
#     fp = file(html_file,"wb")
#     HTMLTestRunner.HTMLTestRunner(fp).run(suit)
#     fp.close()




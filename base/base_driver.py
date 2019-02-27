#coding=utf-8
import time
from appium import webdriver
class BaseDriver:
    def android_driver(self,i):
        capabilities = {
            "platformName":"Android",
            "deviceName":"127.0.0.1:21503",
            "app": "d:/football.apk",
            "appWaitActivity":"com.phsxy.footballbaby.activity.welcome.SplashActivity",
            #屏蔽软键盘
            "unicodeKeyboard":True,
            "resetKeyboard":True
        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
        time.sleep(10)
        return driver
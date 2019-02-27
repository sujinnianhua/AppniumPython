#coding=utf-8
from telnetlib import EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_driver import BaseDriver
from util.get_by_local import GetByLocal
import time
class LoginPage:
    #获取登录页面所有的页面元素信息
    def __init__(self,driver):
        # base_driver = BaseDriver()
        # self.driver = base_driver.android_driver(driver)

        self.get_by_local = GetByLocal(driver)
    #滑动
    def get_swipe(self,num):
         return self.get_by_local.swipe_left(num)

    def get_username_elment(self):
        '''
        获取用户名元素信息
        :return:
        '''
        return self.get_by_local.get_element('username')
    def get_password_element(self):
        '''
        获取密码元素信息
        :return:
        '''
        return self.get_by_local.get_element('password')
    def get_login_button_element(self):
        '''
        获取登按钮元素按钮信息
        :return:
        '''
        return self.get_by_local.get_element('login_button')
    def get_home_page_into(self):
        '''
        首页立即进入
        :return:
        '''
        return self.get_by_local.get_element('into')
    def get_closed(self):
        '''
        点击关闭
        :return:
        '''
        return self.get_by_local.get_element("btn_close")
    def get_setting_my(self):
        '''
        点击我的
        :return:
        '''
        return self.get_by_local.get_element("my")
    def get_settings(self):
        '''
        点击我的
        :return:
        '''
        return self.get_by_local.get_element("mycenter_setting")
    def get_click_address_setting(self):
        '''
        点击收货地址设置
        :return:
        '''
        return self.get_by_local.get_element("click_address_setting")
    def get_address(self):
        '''
        点击添加收货地址
        :return:
        '''
        return self.get_by_local.get_element("address")
    def get_add_name(self):
        '''
        点击添加收货人姓名
        :return:
        '''
        return self.get_by_local.get_element("add_name")
    def get_add_mobile(self):
        '''
        点击添加收货人手机号
        :return:
        '''
        return self.get_by_local.get_element("add_mobile")
    def get_region(self):
        '''
        点击添加收货人地区
        :return:
        '''
        return self.get_by_local.get_element("region")
    def get_confirm(self):
        '''
        点击确定
        :return:
        '''
        return self.get_by_local.get_element("confirm")
    def get_add_detail(self):
        '''
        点击添加收货人详细地址
        :return:
        '''
        return self.get_by_local.get_element("add_detail")
    def get_btn_save(self):
        '''
        点击保存添加地址
        :return:
        '''
        return self.get_by_local.get_element("btn_save")


    # def get_tost_elment(self,message):
    #     '''
    #     获取toastElement
    #     :param message:
    #     :return:
    #     '''
    #     time.sleep(2)
    #     tost_element = ("xpath","//*[contains(@text,"+message+")]")
    #     return WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(tost_element))


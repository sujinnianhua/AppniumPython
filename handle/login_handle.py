#coding=utf-8
from page.login_page import LoginPage
class LoginHandle:
    def __init__(self,driver):
        self.login_page = LoginPage(driver)
    #操作登录页面的元素
    def swipe_lefts(self,num):
        return self.login_page.get_swipe(num)

    def click_into(self):
        '''
        点击进入
        :return:
        '''
        self.login_page.get_home_page_into().click()
    def send_username(self,user):
        '''
        输入用户名
        :param user:
        :return:
        '''
        self.login_page.get_username_elment().send_keys(user)
    def send_password(self,password):
        '''
        输入密码
        :param password:
        :return:
        '''
        self.login_page.get_password_element().send_keys(password)
    def click_login(self):
        '''
        点击登录按钮
        :return:
        '''
        self.login_page.get_login_button_element().click()
    def click_closed(self):
        '''
        点击关闭按钮
        :return:
        '''
        self.login_page.get_closed().click()
    def click_setting_my(self):
        '''
        点击我的
        :return:
        '''
        self.login_page.get_setting_my().click()
    def click_settings(self):
        '''
        点击设置
        :return:
        '''
        self.login_page.get_settings().click()
    def click_address_setting(self):
        '''
        点击添加收货地址设置
        :return:
        '''
        self.login_page.get_click_address_setting().click()
    def click_address(self):
        '''
        点击添加收货地址
        :return:
        '''
        self.login_page.get_address().click()
    def send_add_name(self,addName):
        '''
        点击添加收货人姓名
        :return:
        '''
        self.login_page.get_add_name().send_keys(addName)
    def send_add_mobile(self,mobile):
        '''
        点击添加收货人手机号
        :return:
        '''
        self.login_page.get_add_mobile().send_keys(mobile)
    def click_region(self):
        '''
        点击添加收货人地区
        :return:
        '''
        self.login_page.get_region().click()
    def click_confirm(self):
        '''
        点击确定
        :return:
        '''
        self.login_page.get_confirm().click()
    def send_add_detail(self,detail):
        '''
        点击添加收货人详细地址
        :return:
        '''
        self.login_page.get_add_detail().send_keys(detail)
    def click_save(self):
        '''
        点击保存
        :return:
        '''
        self.login_page.get_btn_save().click()

    def get_fail_tost(self,message):
        '''
        获取toast信息
        :param message:
        :return:
        '''
        tost_elment = self.login_page.get_tost_elment(message)
        if tost_elment:
            return True
        else:
            return False


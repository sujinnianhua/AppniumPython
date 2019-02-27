#coding=utf-8
import time
import  sys
reload(sys)
sys.setdefaultencoding('utf8')
from handle.login_handle import LoginHandle
class LoginBusiness:
    def __init__(self,driver):
        self.login_handle = LoginHandle(driver)


    def login_pass(self):
        self.login_handle.swipe_lefts(4)
        self.login_handle.click_into()
        self.login_handle.send_username('18510985743')
        self.login_handle.send_password('a8887187')
        self.login_handle.click_login()
        self.login_handle.click_closed()
        self.login_handle.click_setting_my()
        self.login_handle.click_settings()
        self.login_handle.click_address_setting()
        self.login_handle.click_address()
        self.login_handle.send_add_name(u"王先生")
        self.login_handle.send_add_mobile("18510985743")
        self.login_handle.click_region()
        self.login_handle.click_confirm()
        self.login_handle.send_add_detail(u"测试地址呀不告诉你")
        self.login_handle.click_save()

    def login_user_error(self):
        self.login_handle.swipe_lefts(4)
        self.login_handle.click_into()
        self.login_handle.send_username('185109857411')
        self.login_handle.send_password('a8887187')
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_tost('用户不存在')
        if user_flag:
            return True
        else:
            return False
    def login_password_error(self):
        self.login_handle.send_username('18510985743')
        self.login_handle.send_password('a88871871')
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_tost('登录密码错误,请重新输入')
        if user_flag:
            return True
        else:
            return False



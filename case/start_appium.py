# -*- coding: UTF-8 -*-
import  sys

from appium.webdriver.common.touch_action import TouchAction

sys.path.append('D:/workplace/AppniumPython')
reload(sys)
# sys.setdefaultencoding('utf8')
from util.get_by_local import GetByLocal
from appium import  webdriver
import time




def get_driver():
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

driver = get_driver()
#获取屏幕的宽高
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width,height

#向左边滑动 [100,200]
def swipe_left(num):
    x1 = get_size()[0]/10*9
    y1 = get_size()[1]/2
    x = get_size()[0]/10
    for n in range(1,num):
        driver.swipe(x1,y1,x,y1,1000)
#向右边滑动 [100,200]
def swipe_right():
    x1 = get_size()[0]/10
    y1 = get_size()[1]/2
    x = get_size()[0]/10*9
    driver.swipe(x1,y1,x,y1,2000)
#向上滑动 [100,200]
def swipe_up():
    x1 = get_size()[0]/2
    y1 = get_size()[1]/10*9
    y = get_size()[1]/10
    driver.swipe(x1,y1,x1,y,1000)
#向下滑动 [100,200]
def swipe_down():
    x1 = get_size()[0]/2
    y1 = get_size()[1]/10
    y = get_size()[1]/10*9
    driver.swipe(x1,y1,x1,y,1000)
def swipe_on(direction,num):
    if direction =='up':
        swipe_up()
    elif direction =='down':
        swipe_down()
    elif direction =='left':
        swipe_left(num)
    else:
        swipe_right()

#屏幕左滑3次
swipe_on("left",4)
get_by_local = GetByLocal(driver)
#点击立即进入
get_by_local.get_element('into').click()
#输入登录账号
get_by_local.get_element('username').send_keys("18510985743")
#输入登录密码
get_by_local.get_element('password').send_keys("a8887187")
#点击登录
get_by_local.get_element('login_button').click()


#关闭窗口
driver.find_element_by_id("com.phsxy.footballbaby.test:id/iv_close").click()
# com.phsxy.footballbaby.test:id/tv_information_comments
# #点击我的
driver.find_element_by_id("com.phsxy.footballbaby.test:id/rb04_footballbabymain").click()
# #点击设置
driver.find_element_by_id("com.phsxy.footballbaby.test:id/activity_mycenter_setting_li").click()
# #点击退出
# driver.find_element_by_id("com.phsxy.footballbaby.test:id/activity_editpersonalinfo_exitlogin").click()

# #点击收货地址设置
driver.find_element_by_id("com.phsxy.footballbaby.test:id/activity_setting_address_li").click()
# #点击添加收货地址
driver.find_element_by_id("com.phsxy.footballbaby.test:id/title_iv_right").click()
# #设置收件人姓名
driver.find_element_by_id("com.phsxy.footballbaby.test:id/activity_addressee_edt").send_keys("wsl")
#
# #设置收件人手机号
driver.find_element_by_id("com.phsxy.footballbaby.test:id/activity_addresseemobile_edt").send_keys("18510985743")
# #设置收件人地区
driver.find_element_by_id("com.phsxy.footballbaby.test:id/activity_addressregion_tv").click()
# #选择确定
driver.find_element_by_id("com.phsxy.footballbaby.test:id/btnSubmit").click()
# #设置收件人详细地址
#
driver.find_element_by_id("com.phsxy.footballbaby.test:id/activity_addresseedetail_edt").send_keys(u'北京市昌平区西二旗')
# #点击保存
#
driver.find_element_by_id("com.phsxy.footballbaby.test:id/activity_editaddress_savebtn").click()
#
# #设置默认地址
TouchAction(driver).press(x=689,y=187).wait(2000).move_to(x=103,y=83).release().perform()
driver.find_element_by_id("com.phsxy.footballbaby.test:id/item_leftslip_default").click()
# #返回到设置
driver.find_element_by_id("com.phsxy.footballbaby.test:id/title_iv_left").click()
# #修改登录密码
driver.find_element_by_id("com.phsxy.footballbaby.test:id/activity_setting_modifypassword_li").click()
# #输入登录密码
driver.find_element_by_id("com.phsxy.footballbaby.test:id/activity_setpass_edt").send_keys("a8887187")
# #再次输入登录密码
driver.find_element_by_id("com.phsxy.footballbaby.test:id/activity_setpass_sureedt").send_keys("a8887187")
driver.find_element_by_id("com.phsxy.footballbaby.test:id/btn_finish").click()
# #输入登录账号
driver.find_element_by_id("com.phsxy.footballbaby.test:id/et_login_mobile").send_keys("18510985743")
# #输入登录密码
driver.find_element_by_id("com.phsxy.footballbaby.test:id/et_login_").send_keys("a8887187")
# #点击登录
driver.find_element_by_id("com.phsxy.footballbaby.test:id/btn_login").click()
# #点击我的
driver.find_element_by_id("com.phsxy.footballbaby.test:id/rb04_footballbabymain").click()
# #点击设置
driver.find_element_by_id("com.phsxy.footballbaby.test:id/activity_mycenter_setting_li").click()
# #修改支付密码
driver.find_element_by_id("com.phsxy.footballbaby.test:id/activity_setting_modifyingpaypassword_li").click()
for z in range(1,7):
    driver.find_element_by_id("com.phsxy.footballbaby.test:id/adapter_inputpwd_tv").click()
for z in range(1,7):
    driver.find_element_by_id("com.phsxy.footballbaby.test:id/adapter_inputpwd_tv").click()
for z in range(1,7):
    driver.find_element_by_id("com.phsxy.footballbaby.test:id/adapter_inputpwd_tv").click()


# driver.find_element_by_id("com.phsxy.footballbaby.test:id/activity_setting_forgetpaypassword_li").click()




















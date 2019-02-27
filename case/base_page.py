# -*- coding: UTF-8 -*-
from case.start_appium import driver


class Action(object):
        #初始化
    def __init__(self,se_driver):
            self.driver = se_driver
    #获取屏幕的宽高
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width,height

    #向左边滑动 [100,200]
    def swipe_left(self,num):
        x1 = self.get_size()[0]/10*9
        y1 = self.get_size()[1]/2
        x = self.get_size()[0]/10
        for n in range(1,num):
            driver.swipe(x1,y1,x,y1,1000)
    #向右边滑动 [100,200]
    def swipe_right(self):
        x1 = self.get_size()[0]/10
        y1 = self.get_size()[1]/2
        x = self.get_size()[0]/10*9
        driver.swipe(x1,y1,x,y1,2000)
    #向上滑动 [100,200]
    def swipe_up(self):
        x1 = self.get_size()[0]/2
        y1 = self.get_size()[1]/10*9
        y = self.get_size()[1]/10
        driver.swipe(x1,y1,x1,y,1000)
    #向下滑动 [100,200]
    def swipe_down(self):
        x1 = self.get_size()[0]/2
        y1 = self.get_size()[1]/10
        y = self.get_size()[1]/10*9
        driver.swipe(x1,y1,x1,y,1000)
    def swipe_on(self,direction,num):
        if direction =='up':
            self.swipe_up()
        elif direction =='down':
            self.swipe_down()
        elif direction =='left':
            self.swipe_left(num)
        else:
            self.swipe_right()

    #重写元素定位的方法
    def find_element(self,loc):
            try:
                return self.driver.find_element_by_id(loc)
            except Exception as e:
             print("未找到%s"%(self,loc))
#coding=utf-8
from read_init import ReadIni
class GetByLocal:
    def __init__(self,driver):
        self.driver = driver
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
            self.driver.swipe(x1,y1,x,y1,1000)
    def get_element(self,key):
        #id
        #com.phsxy.footballbaby.test:id/et_login_mobile
        read_ini = ReadIni()
        local = read_ini.get_value(key)

        if local !=None:

            #定位方式
            by = local.split('>')[0]
            #定位置
            local_by = local.split('>')[1]
            if by == 'id':
                return self.driver.find_element_by_id(local_by)
            elif by == 'className':
                return self.driver.find_element_by_class_name(local_by)
            else:
                return self.driver.find_element_by_xpath(local_by)
        else:
            return None


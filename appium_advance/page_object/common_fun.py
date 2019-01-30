#_author_.="wangxixi"
#封装公共类

from appium_advance.page_object.baseView import BaseView
from appium_advance.page_object.desired_caps import appium_desired
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Common(BaseView):
    #以前的方法
    #cancelBtn = driver.find_element_by_id('android:id/button2').click()
    cancelBtn = (By.ID,'android:id/button2')
    skipBtn = (By.ID,'com.tal.kaoyan:id/tv_skip')

    def check_cancleBtn(self):
        logging.info('check cancelBtn')
        try:
            cancel_Btn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('no cancel_Btn')
        else:
            cancel_Btn.click()

    def check_skipBtn(self):
        logging.info('check skipBtn')
        try:
            skip_Btn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('no skip_Btn')
        else:
            skip_Btn.click()

if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)#实例一个对象，Common继承BaseView类，BaseView基类有参数driver
    com.check_cancleBtn()
    com.check_skipBtn()


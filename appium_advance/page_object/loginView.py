#_author_.="wangxixi"
#封装业务类-登录

from appium_advance.page_object.desired_caps import appium_desired
from appium_advance.page_object.common_fun import Common
from selenium.webdriver.common.by import By
import logging

class LoginView(Common):
    usernameBtn = (By.ID,'com.tal.kaoyan:id/login_email_edittext')
    passwordBtn = (By.ID,'com.tal.kaoyan:id/login_password_edittext')
    loginBtn = (By.ID,'com.tal.kaoyan:id/login_login_btn')

    def login_action(self,username,password):
        self.check_cancleBtn()
        self.check_skipBtn()

        logging.info('=================login_action=================')
        logging.info('username is:%s' %username)
        self.driver.find_element(*self.usernameBtn).send_keys(username)

        logging.info('password is:%s' %password)
        self.driver.find_element(*self.passwordBtn).send_keys(password)
        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished!')

if __name__ == '__main__':
    driver = appium_desired()
    l=LoginView(driver)
    l.login_action('自学网2018','zxw2018')

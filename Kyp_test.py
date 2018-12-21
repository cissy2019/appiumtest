#_author_.="wangxixi"
from appium import webdriver

desired_caps={}
desired_caps['platformName']='Android'
# desired_caps['deviceName']='127.0.0.1:62001'
# desired_caps['platformVersion']='4.4.2'

desired_caps['platformVersion']='6.0'
desired_caps['deviceName']='vivo Y67'
desired_caps['udid']='SKMNY57599999999'

desired_caps['app']=r'C:\Users\Xixi\Desktop\kaoyan3.1.0.apk'
desired_caps['appPackage']='com.tal.kaoyan'
desired_caps['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)



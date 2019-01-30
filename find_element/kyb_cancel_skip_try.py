#_author_.="wangxixi"

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='127.0.0.1:62001'
desired_caps['platformVersion']='4.4.2'

desired_caps['app']=r'C:\Users\Xixi\Desktop\kaoyan3.1.0.apk'
desired_caps['appPackage']='com.tal.kaoyan'
desired_caps['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'

desired_caps['noReset']='True'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

def check_cancleBtn():
	print('check cancelBtn')
	try:
		cancel_Btn = driver.find_element_by_id('android:id/button2')
	except NoSuchElementException:
		print('no cancel_Btn')
	else:
		cancel_Btn.click()

def check_skipBtn():
	print('check skipBtn')
	try:
		skip_Btn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
	except NoSuchElementException:
		print('no skip_Btn')
	else:
		skip_Btn.click()

check_cancleBtn()
check_skipBtn()



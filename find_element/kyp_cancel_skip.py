#_author_.="wangxixi"

from appium import webdriver
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

cancleBtn = driver.find_element_by_id('android:id/button2').click()
skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()

if cancleBtn:
	cancleBtn.click()
else:
	print('no cancleBtn')

if skipBtn:
	skipBtn.click()
else:
	print('no skipBtn')

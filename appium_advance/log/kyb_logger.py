#_author_.="wangxixi"

from appium import webdriver
import yaml
import logging
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO,filename='runlog.log',
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

file=open('../yaml/desired_caps.yaml','r')
data=yaml.load(file)

desired_caps = {}
desired_caps['platformName']=data['platformName']
desired_caps['platformVersion']=data['platformVersion']
desired_caps['deviceName']=data['deviceName']
desired_caps['app']=data['app']
desired_caps['appPackage']=data['appPackage']
desired_caps['appActivity']=data['appActivity']
desired_caps['noReset']=data['noReset']

logging.info('start app')

driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub',desired_caps)

def check_cancleBtn():
	logging.info('check cancelBtn')
	try:
		cancel_Btn = driver.find_element_by_id('android:id/button2')
	except NoSuchElementException:
		logging.info('no cancel_Btn')
	else:
		cancel_Btn.click()

def check_skipBtn():
	logging.info('check skipBtn')
	try:
		skip_Btn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
	except NoSuchElementException:
		logging.info('no skip_Btn')
	else:
		skip_Btn.click()

check_cancleBtn()
check_skipBtn()
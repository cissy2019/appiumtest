#_author_.="wangxixi"
#启动app，打印日志

from appium import webdriver
import yaml
import logging
import logging.config

#log.conf配置就是把日志在控制台和runlog里面都输出显示
CON_LOG = '../log/log.conf'#生成的日志在page_object的文件夹下新runlog.log
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def appium_desired():
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

	desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
	desired_caps['resetKeyboard']=data['resetKeyboard']

	logging.info('start app')
	driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub',desired_caps)
	driver.implicitly_wait(8)
	return driver

if __name__ == '__main__':
	appium_desired()
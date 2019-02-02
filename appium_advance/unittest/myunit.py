#_author_.="wangxixi"
#启动app，关闭app

import unittest
import logging
from time import sleep
from appium_advance.page_object.desired_caps import appium_desired

class StartEnd(unittest.TestCase):
	def setUp(self):
		logging.info('===============setUp===============')
		self.driver=appium_desired()

	def tearDown(self):
		logging.info('================tearDown===============')
		sleep(5)
		self.driver.close_app()


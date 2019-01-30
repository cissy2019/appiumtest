#_author_.="wangxixi"

import logging

# logging.basicConfig(level=logging.DEBUG)#调试时用debug
#logging.basicConfig(level=logging.INFO)#普通就用info
logging.basicConfig(level=logging.INFO,filename='runlog.log',
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

logging.debug('logging debug')
logging.info('logging info')
logging.warning('warning info')
logging.error('error info')
logging.critical('critical info')


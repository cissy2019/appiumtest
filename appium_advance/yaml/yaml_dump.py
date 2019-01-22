#_author_.="wangxixi"

import yaml

slogan = ['welcome','to','51zxw'] #列表
website= {'url':'www.51zxw.net'} #字典

print(slogan)
print(website)

#把python转换成yaml
print(yaml.dump(slogan))
print(yaml.dump(website))


#_author_.="wangxixi"
import yaml

file= open('familyInfo.yaml')
data=yaml.load(file)

#把yaml转换成python
print(data)

print(data['name'])
print(data['age'])

print(data['spouse']['name'])
print(data['spouse']['age'])

print(data['children'][1]['age'])

data['name']='Bob'
print(data['name'])






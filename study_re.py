"""
re 正则的模块
"""

import json
import re
admin_user='13825802580'
admin_pwd='a111111'
data={'admin_user':'13825802580','admin_pwd':'a111111'}
s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
p = "\${admin_user}"  # 需要使用转义衣服把$换成一个普通的字符
p1 = "\${(.*?)}"   # 元字符和限定符，()代表组
m = re.search(p1,s)  #任意位置开始找，找到一个就返回match，
# 使用search进行查找，找到的话就返回一个对象，否则返回None
print('匹配对象',m)
g = m.group()  # 不传参的话返回的是整个匹配的字符串，
print('整个匹配的字符串',g)
g1 = m.group(1)  #取第一个组的匹配的字符串
print('第一个组匹配的字符串',g1)
# value = data[g1]
# s = re.sub(p1,value,s,count=1)  #查找并且替换 sub函数
# sub查找使用的是findall的查找方法
# print('使用正则查找并且替换后的结果',s)

l = re.findall(p1,s)
print(l)
#将字符串转成字典，根据key去取值，取到值判断是否需要替换

# dict=json.loads(s)
# if dict['mobilephone']=='${admin_user}':
#     dict['mobilephone']=admin_user
# if dict['pwd']=='${admin_pwd}':
#     dict['pwd']=admin_pwd
# print(dict)


# 字符串的查询、替换

# if s.find('${admin_user}')!=-1:
#     s=s.replace('${admin_user}',admin_user)
# if s.find('${admin_pwd}')!=-1:
#     s=s.replace('${admin_pwd}',admin_pwd)
# print(s)

# 正则表达式使用单个字符来描述，匹配一系列符合某个句法规则的字符串
# 正则表达式一般包含原本字符和元字符
# ()表示一个组，通俗的理解就是可以用它来标记一个表达式组的开始和结束

# 元字符   匹配规则                         限定符     匹配次数
#   .     可以匹配任意单个自读，汉子，字母
#          符号，数字（注意是单个，就是一个）    +      至少匹配一次

#   \d    匹配任意单个数字                    ？      最多匹配一次
#                                          *       匹配零次或者多次
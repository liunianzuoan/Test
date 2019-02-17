"""
用来替换字符串中的标识符方法
"""
# s  是目标字符串
# d  是替换的内容
# 找到目标字符串里面的标识符的key，去d里面拿到替换的值
#  替换到s里面去  然后返回
import re
from common.read_conf import ReadConfig
read = ReadConfig()

class Context:  # 上下文  数据的准备与记录
    admin_user = read.get_value('admin_data','admin_user')
    admin_pwd = read.get_value('admin_data','admin_pwd')
    loan_memberId = read.get_value('loan_data','loan_memberId')
    invest_user = read.get_value('invest_data','invest_user')
    invest_pwd = read.get_value('invest_data','invest_pwd')
    invest_member_id = read.get_value('invest_data','invest_member_id')

    def replace_new(self,s):
        p = "\${(.*?)}"
        while re.search(p,s):
            m = re.search(p,s)
            key = m.group(1)
            if hasattr(Context,key):
                value = getattr(Context,key)  # 利用反射动态的获取属性的值
                s = re.sub(p,value,s,count=1)
            else:
                print('该属性不存在')
                break
        return s
s = "{'mobilephone':'${admin_user}','pwd':'${admin_pwd}'}"

s = Context().replace_new(s)
print(s)

def replace(s,d):
    p = "\${(.*?)}"
    while re.search(p,s):
        m = re.search(p,s)   # 找到目标标识符
        key = m.group(1)   # 找到匹配的字符串
        value = d[key]    #替换的值
        s = re.sub(p,value,s,count=1)
    return s

s = "{'mobilephone':'${admin_user}','pwd':'${admin_pwd}'}"
d={'admin_user':"13825802580","admin_pwd":"a111111"}

s = replace(s,d)
print(type(s),s)
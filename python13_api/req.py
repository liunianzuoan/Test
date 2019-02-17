import requests
class Work:
    def __init__(self):
        self.session=requests.sessions.Session()
        self.register_url='http://test.lemonban.com/futureloan/mvc/api/member/register'
        self.login_url='http://test.lemonban.com/futureloan/mvc/api/member/login'
        self.recharge_url='http://test.lemonban.com/futureloan/mvc/api/member/recharge'
        self.withdraw_url='http://test.lemonban.com/futureloan/mvc/api/member/withdraw'

    #注册接口调用
    def register(self):
        register_data={"mobilephone":"13856451125","pwd":"a111111","regname":"test"}
        register_resp=self.session.request('get',self.register_url,params=register_data)
        print('响应信息为',register_resp.text)

    #登录接口调用
    def login(self):
        login_data={'mobilephone':'13856451125','pwd':'a111111'}
        login_resp=self.session.request('post',self.login_url,data=login_data)
        print('响应信息为',login_resp.text)


    #充值接口调用
    def recharge(self):
        recharge_data={'mobilephone':'13856451125',"amount":'100000'}
        recharge_resp=self.session.request('get',self.recharge_url,params=recharge_data)
        print('响应信息为',recharge_resp.text)

    def withdraw(self):
        withdraw_data={'mobilephone':'13856451125',"amount":'10'}
        recharge_resp=requests.get(self.withdraw_url,params=withdraw_data,cookies=self.login())
        print('响应信息为',recharge_resp.text)



if __name__ == '__main__':
    session=Work()
    session.register()
    session.login()
    session.recharge()




'''接口测试的特点
1.协议 http  webservice  socket  
2.请求方式  get  post  head  put  delete
3.io  input 和output   入参和检查出参, 校验出参
'''

'''
接口测试应该关注的点
1.如何设计测试用例--> 接口的功能，逻辑，异常（超时，不需要写到自动化里面），安全（密码加密，没有cookies能登录吗？？）
2.自动化测试用例规范？-->代码的可读性，可维护性，可扩展性，高性能（用例执行的时间）
3.如何管理测试数据？excel（测试脚本与测试数据的分离，降低维护成功）
基础数据放在配置文件里面，测试数据放在excel里面，临时数据写在脚本里面

'''

'''
request.get就相当于使用Session.session()实例化一个对象来发起请求
'''
#requests.Session.session()

#session=requests.session()  #实例化一个session对象  这个已不用，，新的使用requests.sessions.Session()
# session=requests.sessions.Session()  #实例化一个session对象，
# 同一个session的cookies可以共享，不同sessioncookies不能共享
data={'mobilephone':"13825802580",'pwd':'a111111','regname':'test'}

#登录接口
# resp=session.request('get','http://test.lemonban.com/futureloan/mvc/api/member/login',params=data)
# print(resp.text)

#充值
# data={'mobilephone':'15810447656',"amount":'100000'}
# resp=session.request('get','http://test.lemonban.com/futureloan/mvc/api/member/recharge',params=data)
# print(resp.text)
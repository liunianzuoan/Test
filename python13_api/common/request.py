import requests
from common.read_conf import ReadConfig
from common import contants
from common.logger import get_logger
logger = get_logger('request')


class Request:
    #初始session实例化对象
    def __init__(self):
        self.session=requests.sessions.session()#实例化一个session对象

    def request(self,method,url,data):
        conf_data = ReadConfig()
        conf_url = conf_data.get_value('URL', 'pro_url')
        full_url = conf_url + url
        method=method.upper()  #将方法都转换成大写
        if data is not None and type(data)==str: #把excel中的data转换成字典
            data=eval(data)  #如果是字符串就转成字典
        if method=='GET':
            resp = self.session.request(method,url=full_url,params=data)
            logger.info('response :{0}'.format(resp.text))
            return resp
        elif method=='POST':
            resp = self.session.request(method, url=full_url, params=data)
            logger.info('response :{0}'.format(resp.text))
            return resp
        else:
            logger.error('不支持此请求方法')
    def close(self):
        self.session.close()  #关闭session




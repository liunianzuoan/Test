
'''
1.第三方库的移植：
a.在原来的工程里面导出requirements (原来安装的第三方模块)
使用命令：pip freeze >requirements 都到处到requirements
b.导进来之后把requirements 复制到根目录，然后根据提示直接安装或者是在requirements 所在的目录在敲
使用命令：pip install -r requirements
'''

'''
2.requests学习
a.学习网站：http://cn.python-requests.org/zh_CN/latest/
'''

""" 
hTTP 协议两大部分 
Request： 
请求方法： 
GET 查--获取资源 
POST 改---修改资源 
PUT 增加 
DELETE 删除 
OPTION  获取可以你支持的请求方式，一般是黑客使用
HEADER  不会有返回体，只会返回头部信息（响应头部信息，请求头部信息）
请求URL： 协议://服务器IP地址：端口号/接口路径 
请求参数：不是所有的请求都要传参，传参方式有两种：url传参和表单传参
header 请求头： Content-type   user-agent  请求来源
cookie：放在客户端，服务器返回给你保留在本地，下次请求的时候带过去发给服务器
cookies和session成对存在


response： 
状态码：服务端和客户端交互的几种状态，并不代表成功 
•1XX－信息类(Information),表示收到Web浏览器请求，正在进一步的处理中 

•2XX－成功类（Successful）,表示用户请求被正确接收，理解和处理例如：200 OK 

•3XX-重定向类(Redirection),表示请求没有成功，客户必须采取进一步的动作。 

•4XX-客户端错误(Client 
Error)，表示客户端提交的请求有错误 例如：404 NOT 
Found。 

•5XX-服务器错误(Server 
Error)表示服务器不能完成对请求的处理：如 500 

响应信息：code,msg 
cookie：服务器返回给客户端，存在客户端 
header：服务器的一些信息
"""

import requests

# 构造请求
# resp = requests.get('http://cn.python-requests.org/zh_CN/latest/')
# resp.encoding = 'utf-8' # 解决乱码
# print('响应码', resp.status_code)
# print('响应信息', resp.text)
# with open('index.html', 'w+',encoding='utf-8') as file:
#     file.write(resp.text)


# 登录接口 get ---url传参 ---params
# data = {'mobilephone':'15810447656',"pwd":"123456"}
# resp = requests.get('http://test.lemonban.com/futureloan/mvc/api/member/login',params=data) # PARAMS url传参
# print('请求url',resp.request.url)
# print('请求参数',resp.request.body)
# print('响应码', resp.status_code)
# print('响应信息', resp.text)

#登录接口 post ---表单传参 ---data
# data = {'mobilephone':'15810447656',"pwd":"123456"}
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login',data=data)
# print('请求url',resp.request.url)
# print('请求参数',resp.request.body)
# print('请求headers',resp.request.headers)
# print('请求cookies',resp.request._cookies)#cookies  是protected属性，所以加下划线访问他
# print('响应码', resp.status_code)
# print('响应信息', type(resp.text))
# print('响应信息字典', type(resp.json()))
# print('响应信息字典', resp.json()['status'])
# print('响应信息', resp.text)
# print('响应cookies', resp.cookies)
# print('响应headers', resp.headers)


#以二进制响应内容
# print(resp.content)  #以二进制的形式显示响应信息
# from PIL import Image
# from io import BytesIO
# i=Image.open(BytesIO(resp.content))  #以请求返回的二进制数据创建一张图片  报错了  怎么解决

#json响应内容
# print(resp.json())

#原始响应内容，可以使用resp.raw  请你确保在初始请求中设置了 stream=True
# resp = requests.post('http://test.lemonban.com/futureloan/mvc/api/member/login',data=data,stream=True)
# resp.raw
# print(resp.raw.read())






import os


#获取data.xlsx的绝对路径

#os.path.realpath(__file__)和os.path.abspath(__file__)一样  都是获取当前模块的绝对路径
#os.path.dirname(__file__)获取当前文件的父级目录
dir_path = os.path.dirname(os.path.dirname(__file__))
# path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(dir_path)
#path=os.path.realpath(__file__)
# path=os.path.abspath(__file__)
# print(path)


class ProjectPath:

    def data(self):
        path = os.path.join(dir_path,"datas","data.xlsx")
        return path


base_dir=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  #获取根目录
data_file=os.path.join(base_dir,'datas','data.xlsx')  #使用拼接获取data.xlsx的路径
json_file=os.path.join(base_dir,'datas','data.json')
url_file=os.path.join(base_dir,'conf','url.conf')
url2_file=os.path.join(base_dir,'conf','url2.conf')
switch_file=os.path.join(base_dir,'conf','switch.conf')
report_file=os.path.join(base_dir,'reports','report.html')
logs_dir = os.path.join(base_dir,'logs')
testcases_dir =os.path.join(base_dir,'testcases')   #获取testcases的路径

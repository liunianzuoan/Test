from configparser import ConfigParser
from common import contants


class ReadConfig:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(contants.switch_file)    # 先读取switch.conf里面的值
        open=self.config.getboolean('switch','open')
        if open:              # 如果switch.conf里面的值为True则读取url.conf的数据
            self.config.read(contants.url_file)
        else:              # 如果switch.conf里面的值为False则读取url.conf的数据
            self.config.read(contants.url2_file)

    def get_value(self,section,option):  # 读取出来的数据是str
        return self.config.get(section,option)

    def get_int(self,section,option):    # 读取出来的数据是int
        return self.config.getint(section,option)

if __name__ == '__main__':
    read=ReadConfig()
    print(read.get_value('data','dict_data'))
    print(eval(read.get_value('data','dict_data')))





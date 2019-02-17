import pymysql
from common.read_conf import ReadConfig


class MysqlUtil:
    def __init__(self):   # 建立连接，使用cursor()方法获取操作游标
        conf_data=ReadConfig()
        self.mysql = pymysql.connect(host=conf_data.get_value('db','host'),
                                     user=conf_data.get_value('db','user'),
                                     password=conf_data.get_value('db','password'),
                                     port=conf_data.get_int('db','port'))
        self.cursor = self.mysql.cursor()

    def fetch(self, sql):

        self.cursor.execute(sql)  # 执行sql语句
        result = self.cursor.fetchone()  # 返回结果
        return result

    def close(self):
        self.cursor.close()  # 关闭查询窗口
        self.mysql.close()   # 关闭连接

if __name__ == '__main__':
    mysql=MysqlUtil()
    sql = 'select max(mobilephone) from future.member'
    result=mysql.fetch(sql)
    print(result[0])
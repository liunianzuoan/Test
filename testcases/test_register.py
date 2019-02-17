import unittest
from common.do_excel import DoExcel
from libext.ddt import ddt,data
from common.request import Request
from common import contants
from common.mysql import MysqlUtil
from common.logger import get_logger
logger = get_logger('case')


# excel里面涉及的第一条用例是正常登录
# session保持会话的方式来请求的话，就需要把这个request实例化的对象放在类里面
# 读取excel数据 运行用例
# @unittest skip放在测试方法上装饰的话，表示不运行此用例@unittest skip('不要运行')  就会只打印不要运行
# 不执行用例
@ddt
class TestRegister(unittest.TestCase):

    do_excel = DoExcel(contants.data_file)
    test_data = do_excel.get_data('register')

    @classmethod
    def setUpClass(cls):   # 每个测试类里面运行的操作放在setupclass里面，只执行一次
        cls.request = Request()  # 建立session会话，实例化对象
        cls.mysql = MysqlUtil()

    def setUp(self):   # 每个测试方法里面运行的操作放在setup里面，每执行一次用力都会执行一次setup

        sql = 'select max(mobilephone) from future.member'
        self.result = self.mysql.fetch(sql)

    @data(*test_data)
    def test_register(self, case):
        print('-----开始执行第{}条用例--------'.format(case.case_id))
        import json
        data_dict = json.loads(case.data)
        if data_dict['mobilephone'] == '${mobile}':
            data_dict['mobilephone'] = int(self.result[0])+1
        # 使用封装好的request来进行请求
        res = self.request.request(case.method, case.url, data_dict)
        logger.info(res.text)
        try:
            # 返回结果和实际结果进行断言判断
            self.assertEqual(case.expected, res.text, 'register error')
            # 一致就写回pass，不一致就写回failed
            self.do_excel.write_back(case.case_id+1, res.text, 'PASS')
        except AssertionError as e:
            self.do_excel.write_back(case.case_id+1, res.text, 'Failed')
            logger.error('断言错误:{0}'.format(e))
            raise e  # 处理之后抛出错误

    def tearDown(self):
        print('--------用例执行完毕---------')

    @classmethod
    def tearDownClass(cls):
        cls.mysql.close()
        cls.request.session.close()   # 用例执行完毕关闭session会话，不然的话资源被占用


if __name__ == '__main__':
    unittest.main()

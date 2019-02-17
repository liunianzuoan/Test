import unittest
from ddt import ddt,data
from common.do_excel import DoExcel
from common.read_conf import ReadConfig
from common.request import Request
from common import contants
from common.context import replace

@ddt
class InvestTest(unittest.TestCase):
    do_excel = DoExcel(contants.data_file)
    test_data = do_excel.get_data('invest')   #读取data里面invest表单的数据

    @classmethod
    def setUpClass(cls):
        cls.request = Request()    # 建立session会话，实例化对象
        cls.config = ReadConfig()    #为了后边读取配置文件中的数据

    @data(*test_data)
    def test_invest(self,case):
        print('开始执行第{}条用例'.format(case.case_id))
        print(case.data)
        dict = eval(self.config.get_value('data','dict_data'))   # 把配置文件读取出来的数据转换成字典
        case.data = replace(case.data,dict)

        res = self.request.request(case.method, case.url, case.data)
        print(res.text)
        print(case.data)
        try:
            self.assertEqual(res.json()['code'], case.expected, 'error')
            self.do_excel.write_back(case.case_id + 1, res.json()['code'], 'PASS')
        except AssertionError as e:
            self.do_excel.write_back(case.case_id + 1, res.json()['code'], 'Failed')
            raise e

    def tearDown(self):
        print('用例执行完毕')

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭request 请求会话
        cls.mysql.close()  # 关闭mysql

if __name__ == '__main__':
    unittest.main()



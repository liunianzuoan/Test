import unittest
from common.do_excel import DoExcel
from libext.ddt import ddt,data
from common.request import Request
from common import contants
from common.logger import get_logger
logger = get_logger('case')


@ddt
class TestLoad(unittest.TestCase):
    do_excel = DoExcel(contants.data_file)
    test_data=do_excel.get_data('load')

    @classmethod
    def setUpClass(cls):
        cls.request = Request()  # 建立session会话，实例化对象
    @data(*test_data)
    def test_load(self,case):
        logger.info('开始执行第{}条用例'.format(case.case_id))
        res=self.request.request(case.method,case.url,case.data)
        logger.info(res.text)
        try:
            self.assertEqual(res.json()['code'],case.expected,'error')
            self.do_excel.write_back(case.case_id+1,res.json()['code'],'PASS')
        except AssertionError as e:
            self.do_excel.write_back(case.case_id+1,res.json()['code'],'Failed')
            logger.error('断言错误：{}'.format(e))

    def tearDown(self):
        print('用例执行完毕')
    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()   #关闭request请求

if __name__ == '__main__':
    unittest.main()
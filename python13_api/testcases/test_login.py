import unittest
from common.do_excel import DoExcel
from common import contants
from libext.ddt import ddt,data
from common.request import Request
from common.logger import get_logger
request=Request()

do_excel=DoExcel(contants.data_file)
cases=do_excel.get_data('login')
logger = get_logger('login')
@ddt
class LoginTest(unittest.TestCase):
    def setUp(self):
        pass
    @data(*cases)
    def test_login(self,case):
        logger.info('开始执行第{}条用例'.format(case.case_id))
        res=request.request(case.method,case.url,case.data)
        logger.info(res.text)
        try:
            self.assertEqual(case.expected,res.text,'login error')
            do_excel.write_back(case.case_id+1,res.text,'PASS')
        except AssertionError as e:
            logger.error('断言错误：{}'.format(e))
            do_excel.write_back(case.case_id+1,res.text,'Failed')
            raise e

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        request.session.close()  # 关闭request请求
if __name__ == '__main__':
    unittest.main()
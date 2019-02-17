import unittest
from common.do_excel import DoExcel
from common import contants
from common.request import Request
from libext.ddt import ddt,data
from common.logger import get_logger
logger = get_logger('case')
request=Request()
@ddt
class RechargeTest(unittest.TestCase):
    do_excel=DoExcel(contants.data_file)
    cases=do_excel.get_data('withdraw')
    def setUp(self):
        pass

    @data(*cases)
    def test_recharge(self,case):
        logger.info('开始执行第{}条用例'.format(case.case_id))
        res=request.request(case.method,case.url,case.data)
        logger.info(res.json())
        try:
            self.assertEqual(case.expected,res.json()['code'])
            self.do_excel.write_back(case.case_id+1,res.json()['code'],'PASS')
        except AssertionError as e:
            self.do_excel.write_back(case.case_id+1,res.json()['code'], 'Failed')
            logger.error('断言错误：{}'.format(e))
            raise e
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        request.session.close()  # 关闭request请求
if __name__ == '__main__':
    unittest.main()


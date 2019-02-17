import unittest
from libext.ddt import ddt,data
from common.do_excel import DoExcel
from common.read_conf import ReadConfig
from common.request import Request
from common import contants
from common.context import Context
from common.mysql import MysqlUtil
from common.logger import get_logger
logger = get_logger('case')

@ddt
class InvestTest(unittest.TestCase):
    do_excel = DoExcel(contants.data_file)
    test_data = do_excel.get_data('invest')  # 读取data里面invest表单的数据


    @classmethod
    def setUpClass(cls):
        cls.request = Request()  # 建立session会话，实例化对象
        cls.context = Context()
        cls.mysql = MysqlUtil()  #实例化mysql对象，实例化一次即可
    @data(*test_data)
    def test_invest(self, case):
        logger.info('开始执行第{}条用例'.format(case.case_id))
        logger.info(case.data)  # excel的原始测试数据
        # 查找参数化的测试数据，动态替换
        case.data = self.context.replace_new(case.data)
        res = self.request.request(case.method, case.url, case.data)
        logger.info(res.text)
        logger.info(case.data)   # 替换之后的测试数据
        try:
            self.assertEqual(res.json()['code'], case.expected, 'error')
            self.do_excel.write_back(case.case_id + 1, res.json()['code'], 'PASS')
            # 判断是否加标成功，如果成功就按照借款人ID去数据库查询最新的加标记录
            if res.json()['msg'] == '加标成功':
                sql ="select * from future.loan where MemberId='1117024' order by createtime desc limit 1"
                loan_id = self.mysql.fetch(sql)[0]
                setattr(Context,'loan_id',str(loan_id))  # 后续要通过正则替换，需要换成字符串
        except AssertionError as e:
            self.do_excel.write_back(case.case_id + 1, res.json()['code'], 'Failed')
            logger.error('断言错误：{}'.format(e))
            raise e


    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭request 请求会话
        cls.mysql.close()  # 关闭mysql


if __name__ == '__main__':
    unittest.main()




import unittest
from common.do_excel import DoExcel
from ddt import ddt,data
from common.request import Request
from common import contants
from common.read_conf import ReadConfig
import json


@ddt
class TestLoad(unittest.TestCase):
    do_excel = DoExcel(contants.data_file)
    test_data=do_excel.get_data('invest')

    @classmethod
    def setUpClass(cls):
        cls.request = Request()  # 建立session会话，实例化对象
        cls.read=ReadConfig()
    @data(*test_data)
    def test_load(self,case):
        print('开始执行第{}条用例'.format(case.case_id))
        print(case.data)
        if case.data.find("${admin_user}")!=-1:
            case.data=case.data.replace("${admin_user}",self.read.get_value('admin_data','admin_user'))
        if case.data.find("${admin_pwd}")!=-1:
            case.data =case.data.replace("${admin_pwd}", self.read.get_value('admin_data', 'admin_pwd'))
        if case.data.find("${loan_memberId}")!=-1:
            case.data =case.data.replace("${loan_memberId}", self.read.get_value('loan_data', 'load_member_id'))
        if case.data.find("${loan_id}")!=-1:
            case.data =case.data.replace("${loan_id}", self.read.get_value('loan_data', 'loan_id'))
        if case.data.find("${invest_user}")!=-1:
            case.data =case.data.replace("${invest_user}", self.read.get_value('invest_data', 'invest_user'))
        if case.data.find("${invest_pwd}")!=-1:
            case.data =case.data.replace("${invest_pwd}", self.read.get_value('invest_data', 'invest_pwd'))
        if case.data.find("${invest_member_id}")!=-1:
            case.data =case.data.replace("${invest_member_id}", self.read.get_value('invest_data', 'invest_member_id'))
        print(case.data)
        res=self.request.request(case.method,case.url,case.data)
        print(res.text)
        try:
            self.assertEqual(res.json()['code'],case.expected,'error')
            self.do_excel.write_back(case.case_id+1,res.json()['code'],'PASS')
        except AssertionError as e:
            self.do_excel.write_back(case.case_id+1,res.json()['code'],'Failed')
            raise e
    def tearDown(self):
        print('用例执行完毕')

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 关闭request 请求会话
        cls.mysql.close()  # 关闭mysql

if __name__ == '__main__':
    unittest.main()


import unittest
import HTMLTestRunnerNew
from common import contants

from testcases.test_register import TestRegister
suite=unittest.TestSuite() #加载测试套件

#通过测试类来加载测试用例
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestRegister))


#执行用例
with open(contants.report_file,'wb')as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='前程贷注册接口执行结果',
                                            description='接口测试',
                                            tester='zuoan')
    runner.run(suite)


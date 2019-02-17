#  自动查找testcases目录下，以test_开头的.py文件里面的测试类
import unittest
import HTMLTestRunnerNew
from common import contants

# 找到测试类的测试文件
discover = unittest.defaultTestLoader.discover(contants.testcases_dir,
                                               pattern='test_*.py')

with open(contants.report_file,'wb')as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='前程贷注册接口执行结果',
                                            description='接口测试',
                                            tester='zuoan')
    runner.run(discover)

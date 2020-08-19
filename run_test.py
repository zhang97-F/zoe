# 导包
import  common.HTMLTestRunnerNew as HT
import requests
import unittest
import time
# 设置一个装这些用例的容器
suite = unittest.TestSuite()
# 设置一个发现这些用例的工具
load = unittest.defaultTestLoader
# 用load去发现用例
testcases = load.discover('test_cares',pattern='test*.py',top_level_dir=None)
# 把发现的用例放在容器中
suite.addTests(testcases)
# 设置测试报告的文档名字-----固定的名字reporter+当前系统时间+.html
# currenttime = time.strftime("%Y-%m-%d %H-%M-%S")
filename = r'report/reporter.html'
# 生产测试报告  1、保证HTMLTestRunnerNew包要在commmon文件中  2、导包 import common.HTMLTestRunnerNew
with open(filename,'wb+') as fp:
    runner = HT.HTMLTestRunner(stream=fp,title='学生管理系统接口测试报告',description='balalala',tester="zf")
    runner.run(suite)














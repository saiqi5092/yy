# coding: utf-8
import unittest,time
import HTMLTestRunner
import smtplib

# 用例地址
test_dir = "E:\\self\\python\\scripts\\firstpro\\test_case"

# 收集测试用例
discover = unittest.defaultTestLoader.discover(test_dir , 'test*.py')
print discover

now_format = time.strftime("%Y_%m_%d_%H_%M_%S")
# report 路径
filename = "E:\\self\\python\\scripts\\firstpro\\report\\result.html"
fp = open(filename,"wb")

runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title=u"测试报告主题",
                                       description=u"这是xxx项目的测试报告")
runner.run(discover)




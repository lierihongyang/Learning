# -*-coding:utf-8 -*-

"""
# File       : custom_suite.py
# Time       ：2024/9/7 下午1:52
# Author     ：Li
"""
"""自定义测试套件"""

import unittest
from myfun import *


class MyTest1(unittest.TestCase):

    def setUp(self):
        print("\n----------测试用例前执行----------")

    def tearDown(self):
        print("\n----------测试用例执行后执行----------")

    def test_mul(self):
        print("测试乘法")
        res = mul(1, 2)
        assert res > 0, "减法乘法计算错误"

    def test_divb(self):
        print("测试除法")
        res = div(1, 2)
        assert res < 0, "除法结果计算错误"


if __name__ == '__main__':
    # 自定义测试套件
    suite = unittest.TestSuite()
    # 向套件内添加测试用例
    # 单个添加
    suite.addTest(MyTest1("test_mul"))
    # 多个添加，且可以重复添加
    suite.addTests([MyTest1("test_divb"), MyTest1("test_mul")])

    # 执行测试用例
    # 创建执行器，并指定信息输出级别
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

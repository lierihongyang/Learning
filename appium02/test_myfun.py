# -*-coding:utf-8 -*-

"""
# File       : test_myfun.py
# Time       ：2024/9/7 下午12:46
# Author     ：Li
"""
import unittest
from myfun import *
import retry  # 重复执行


class MyTest(unittest.TestCase):
    count = 1

    def setUp(self):
        print("\n----------测试用例前执行----------")

    def tearDown(self):
        print("\n----------测试用例执行后执行----------")

    @classmethod
    def setUpClass(cls):
        print("\n==========测试类执行前执行==========")

    @classmethod
    def tearDownClass(cls):
        print("\n==========测试类执行后执行==========")

    @unittest.skip("暂时跳过")
    def test_add(self):
        print(f"开始测试add方法")
        res = add(1, 2)
        assert res == 3, "加法结果计算错误"

    @unittest.skipIf(count > 0, reason="count大于1，条件成立")
    def test_minus(self):
        print("测试减法")
        res = minus(1, 2)
        assert res > 0, "减法结果计算错误"

    def test_mul(self):
        print("测试乘法")
        res = mul(1, 2)
        assert res > 0, "减法乘法计算错误"

    @retry.retry(tries=3)
    def test_divb(self):
        print("测试除法")
        res = div(1, 2)
        assert res < 0, "除法结果计算错误"


if __name__ == '__main__':
    # verbosity指定测试结果输出信息的详细程度
    # 详细程度：2 > 1
    # main方法实际会调用testrunner，该方法下方的代码不会被执行
    unittest.main(verbosity=1)

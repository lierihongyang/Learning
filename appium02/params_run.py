# -*-coding:utf-8 -*-

"""
# File       : params_run.py
# Time       ：2024/9/7 下午2:04
# Author     ：Li
"""
"""参数化"""
import unittest
from myfun import *
from ddt import ddt, data, unpack

args = [1, 2, 3, 4, 5, 6]
params_list = [[1, 2], [2, 2], [2, 3], [3, 3]]
params_dict = [{"value1": 1, "value2": 2}, {"value1": 2, "value2": 2}, {"value1": 2, "value2": 3}]


@ddt
class MyTest1(unittest.TestCase):

    # @data(1, 2, 3, 4, 5, 6)
    # @data(*args)  # 单个参数
    # def test_mul(self, value):
    #     print(f"\n参数化-->> {value}")
    #     assert value > 3, "用例失败"

    # @data([1, 2], [1, 1], [2, 3])
    # @data(*params_list)
    # @unpack
    # def test_mult_args(self, value1, value2):
    #     print(f"\n多参数: {value1} ===> {value2}")
    #     assert value1 == value2, '两个数不相等'

    # 字典的kye 名 以及数量 需要和参数的数量以及名字一致
    # @data({"value1": 1, "value2": 2}, {"value1": 2, "value2": 2}, {"value1": 2, "value2": 3})
    @data(*params_dict)
    @unpack
    def test_mult_dict(self, value1, value2):
        print(f"\n多参数: {value1} ===> {value2}")
        assert value1 == value2, '两个数不相等'


if __name__ == '__main__':
    unittest.main(verbosity=2)

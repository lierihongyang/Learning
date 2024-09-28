# -*-coding:utf-8 -*-

"""
# File       : 1-生成器与协程.py
# Time       ：2024/9/28 下午8:02
# Author     ：Li
"""
import time


# 生成器回顾

def func():
    print("生成器函数")
    while True:
        yield "生成器返回的数据"


# 这里返回的是一个生成器对象
obj = func()
print(obj)
print(next(obj))
print(next(obj))


# ==========================================================
# 利用生成器来实现任务的切换
def func_a():
    while True:
        print("这里是func a")
        yield
        time.sleep(0.5)


def func_b(func):
    for _ in func:
        print("这里是func b")
        func.__next__()


a = func_a()
func_b(a)

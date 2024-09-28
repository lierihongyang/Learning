# -*-coding:utf-8 -*-

"""
# File       : 多进程-基本使用.py
# Time       ：2024/9/7 下午4:33
# Author     ：Li
"""
import time
from multiprocessing import Process


def fun(name):
    time.sleep(3)
    print(f"多进程: {name}")


if __name__ == '__main__':
    ps = [Process(target=fun, args=(f"proc_{i}",)) for i in range(4)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()

    print("main结束")

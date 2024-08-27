# -*- coding: UTF-8 -*-
import re
import time


def create_data():
    """创建800w行数据"""
    with open("./test_data.txt", "r", encoding="utf-8") as rf:
        data = rf.read()

    with open("./data.txt", "w+", encoding="utf-8") as wf:
        for i in range(0, 8000):
            wf.write(data)


def get_func_run_time(func):
    """一个装饰器，计算被装饰函数的运行时间"""

    def inner():
        start = time.time()
        func()
        end = time.time()
        print(f"函数共运行{end - start}秒")

    return inner


@get_func_run_time
def get_strong_tag1():
    """获取strong标签中的数据，正则表达编译模式
    """
    # pattern = r"<strong>学习如何创建高质量的web网站</strong></a>"
    pattern = r"<strong>(.*?)</strong></a>"
    com_pat = re.compile(pattern)
    match_res = []
    i = 0
    with open("./data.txt", "r", encoding="utf-8") as rf:
        while True:
            line = rf.readline()
            i += 1
            res = com_pat.findall(line)
            if len(res) > 0:
                match_res.append(res[-1])
            if line == "":
                print(f"end ==> {i}")
                break
    print(match_res)


@get_func_run_time
def get_strong_tag2():
    """获取strong标签中的数据"""
    # pattern = r"<strong>学习如何创建高质量的web网站</strong></a>"
    pattern = r"<strong>(.*?)</strong></a>"
    match_res = []
    i = 0
    with open("./data.txt", "r", encoding="utf-8") as rf:
        while True:
            line = rf.readline()
            i += 1
            res = re.findall(pattern, line)
            if len(res) > 0:
                match_res.append(res[-1])
            if line == "":
                print(f"end ==> {i}")
                break
    print(match_res)


if __name__ == '__main__':
    # create_data()
    get_strong_tag1()  # 编译 8.196558237075806秒
    # get_strong_tag2()  # 未编译 9.60498595237732秒

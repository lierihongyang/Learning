# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：demo.py
@Author  ：LiChunBo
@Date    ：2024/7/29 下午4:33
"""
import time


class Demo1:
    def run(self):
        print("demo1 run......")


class Demo2:
    def run(self):
        print("demo2  run----->")

    def print_attr(self):
        print(f"width: {self.width}")
        print(f"height: {self.height}")


class Demo3:
    def __init__(self):
        self.height = 800
        self.width = 800

    def info(self):
        print(f"height: {self.height}; width: {self.width}")


class Demo4:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def __str__(self):
        return f"height: {self.height}; width: {self.width}"

    def __del__(self):
        print(f"资源释放: {self.height}; {self.width}")


if __name__ == "__main__":
    # d1 = Demo1()
    # d1.run()
    # d2 = Demo2()
    # d2.height = 100
    # d2.width = 100
    # d2.print_attr()
    # d2_ = Demo2()
    # d2_.print_attr()
    # d3 = Demo3()
    # d3.info()
    # d3_ = Demo3()
    # d3_.info()
    d4 = Demo4(600, 800)
    print(d4)
    del d4
    time.sleep(5)

    d4_ = Demo4(100, 100)
    print(d4_)

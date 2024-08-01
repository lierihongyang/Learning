# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：Attr.py
@Author  ：LiChunBo
@Date    ：2024/8/1 下午2:43
"""


class Dog:
    tooth = 10

    def __init__(self, name):
        self.name = name

    @staticmethod
    def static_fun():
        print("静态方法调用")

    @classmethod
    def class_fun(cls):
        print(f"类方法调用: {cls.tooth}")

    def self_fun(self):
        print(f"实例方法调用: {self.name}")


if __name__ == '__main__':
    xh = Dog("小黑")
    xx = Dog("xx")
    print(f"访问类属性：xh: {xh.tooth}; xx: {xx.tooth}; Dog: {Dog.tooth}")
    xh.tooth = 8
    print(f"访问对应属性：xh: {xh.tooth}; xx: {xx.tooth}; Dog: {Dog.tooth}")
    # 修改类属性
    Dog.tooth = 12
    print(f"访问对应属性：xh: {xh.tooth}; xx: {xx.tooth}; Dog: {Dog.tooth}")
    print("*" * 60)

    # 实例对象、类对象都能够调用静态方法
    xh.static_fun()
    xx.static_fun()
    Dog.static_fun()
    print("*" * 60)
    # 实例对象、类对象都能调用实例方法，但是类对象需要传递实例对象
    xh.self_fun()
    xx.self_fun()
    Dog.self_fun(xx)
    print("*" * 60)
    # 实例对象、类对象都能调用类方法
    xh.class_fun()
    xx.class_fun()
    Dog.class_fun()

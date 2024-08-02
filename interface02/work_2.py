# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：work_2.py
@Author  ：LiChunBo
@Date    ：2024/8/2 上午9:29
"""


class Cat:
    def __init__(self, shape: str):
        self.shape = shape

    def eat(self):
        print(f"{self.shape}正在吃鱼")

    def drink(self):
        print(f"{self.shape}正在喝水")


class Human:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.hobby = []

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1

    def __str__(self):
        return f"name: {self.name}, weight: {self.weight}, hobby: {self.hobby}"


if __name__ == "__main__":
    cat = Cat("小猫")
    cat.eat()
    cat.drink()

    xh = Human("小红", 45)
    xm = Human("小明", 75)
    print(xm)
    xm.run()
    print(xm)
    xm.eat()
    print(xm)
    print(xh)

# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：work_1.py
@Author  ：LiChunBo
@Date    ：2024/7/30 上午9:32
"""


class Cat:
    def __init__(self):
        self.shape = "小"

    def eat(self):
        print(f"{self.shape}猫在吃鱼")

    def drink(self):
        print(f"{self.shape}猫在喝水")


class People:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.hobby = "吃东西"

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1

    def __str__(self):
        return f"name: {self.name}, hobby: {self.hobby}, weight: {self.weight}kg."


if __name__ == "__main__":
    cat = Cat()
    cat.eat()
    cat.drink()
    print("*" * 60)
    xiao_ming = People("小明", 75)
    xiao_hong = People("小红", 45)
    print(xiao_hong)
    xiao_hong.run()
    xiao_hong.run()
    print(xiao_hong)
    xiao_hong.eat()
    print(xiao_hong)

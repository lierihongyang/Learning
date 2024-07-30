# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：烤地瓜.py
@Author  ：LiChunBo
@Date    ：2024/7/29 下午6:52
"""


class RoastPotato:
    def __init__(self):
        self.cook_time = 0
        self.status = "生的"
        self.seasoning = []

    def cooking(self, t):
        self.cook_time += t
        if 0 <= self.cook_time < 3:
            self.status = "生的"
            print()
        elif 3 <= self.cook_time < 5:
            self.status = "半生不熟的"
        elif 5 <= self.cook_time <= 8:
            self.status = "熟的"
        elif self.cook_time > 8:
            self.status = "糊了"
        else:
            print("烘烤时间非法")

    def add_seasoning(self, *args):
        self.seasoning.extend(args)

    def __str__(self):
        return f"烘培时间：{self.cook_time}分钟, 地瓜状态：{self.status}, 添加了{self.seasoning}"


if __name__ == '__main__':
    rp = RoastPotato()
    rp.cooking(5)
    rp.add_seasoning("糖", "糖")
    print(rp)

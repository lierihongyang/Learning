# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：work_3.py
@Author  ：LiChunBo
@Date    ：2024/8/2 上午9:37
"""


class Furniture:
    """家具"""

    def __init__(self, name: str, area: float):
        self.name = name
        self.area = area


class Home:
    """房子类"""

    def __init__(self, home_type: str, area: float):
        self.home_type = home_type
        self.area = area
        self.rema_area = area
        self.furs = []

    def add_fur(self, fur: Furniture):
        """摆放家具"""
        if self.rema_area > fur.area:
            self.furs.append(fur.name)
            self.rema_area -= fur.area
        else:
            print(f"房屋剩余面积无法摆放该家具: {fur.name}")

    def __str__(self):
        return f"户型：{self.home_type}, 总面积: {self.area}, 剩余面积: {self.rema_area}, 已摆放家具：{self.furs}"


class Arms:
    """武器"""

    def __init__(self, name):
        self.name = name
        self.bullet_count = 0

    def add_bullet(self, count):
        if count <= 0:
            return
        self.bullet_count += count

    def lanuch_bullet(self, count):
        if count <= 0:
            return
        if self.bullet_count == 0:
            print(f"弹夹中没有子弹，请装填子弹")
        elif self.bullet_count <= count:
            print(f"弹夹已清空")
            self.bullet_count = 0
        else:
            self.bullet_count -= count


class Soldiers:
    """士兵"""

    def __init__(self, name: str, arms: Arms):
        self.name = name
        self.arms = arms

    def add_bullet(self, count: int):
        self.arms.add_bullet(count)

    def fire(self, count: int):
        self.arms.lanuch_bullet(count)

    def __str__(self):
        return f"士兵{self.name}, 有一把{self.arms.name}, 剩余子弹{self.arms.bullet_count}发"


if __name__ == '__main__':
    home = Home("两室一厅", 100)
    print(home)
    f1 = Furniture("床", 4)
    f2 = Furniture("衣柜", 2)
    f3 = Furniture("餐桌", 1.5)
    home.add_fur(f1)
    home.add_fur(f2)
    home.add_fur(f3)
    print(home)
    home.add_fur(Furniture("冰箱", 100))
    print("*" * 60)
    ak47 = Arms("AK47")
    s = Soldiers("瑞恩", ak47)
    print(s)
    s.add_bullet(10)
    s.add_bullet(-4)
    print(s)
    s.fire(90)
    print(s)
    s.fire(1)
    s.add_bullet(100)
    print(s)

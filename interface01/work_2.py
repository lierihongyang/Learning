# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：work_2.py
@Author  ：LiChunBo
@Date    ：2024/7/30 上午9:39
"""


class Furniture:
    """家具类"""

    def __init__(self, fur_name: str, fur_area: float):
        self.fur_name = fur_name
        self.fur_area = fur_area


class Home:
    """房子类"""

    def __init__(self, home_type: str, area: float):
        self.home_type = home_type  # 户型
        self.area = area  # 面积
        self.rema_area = self.area  # 剩余面积
        self.furs = []  # 家具

    def add_fur(self, fur: Furniture):
        """摆放家具"""
        if self.area - fur.fur_area > 0:  # 剩余面积大于家具面积才允许摆放
            self.furs.append(fur.fur_name)
            self.rema_area -= fur.fur_area
        else:
            print(f"家具：{fur.fur_name}面积太大，无法摆放")
            return

    def __str__(self):
        return f"房屋户型: {self.home_type}, 总面积：{self.area}, 剩余面积：{self.rema_area}, 已摆放家具：{self.furs}"


if __name__ == '__main__':
    hose = Home("三室一厅", 100)
    print(hose)
    f1 = Furniture("床", 4)
    f2 = Furniture("衣柜", 2)
    f3 = Furniture("餐桌", 1.5)
    hose.add_fur(f1)
    print(hose)
    hose.add_fur(f2)
    hose.add_fur(f3)
    print(hose)
    hose.add_fur(Furniture("hose", 100))
    print(hose)

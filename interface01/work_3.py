# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：work_3.py
@Author  ：LiChunBo
@Date    ：2024/7/30 上午10:03
"""


class Arms:
    """武器"""

    def __init__(self, name):
        self.name = name
        self.bullet_count = 0  # 子弹数量

    def add_bullet(self, count):
        """装填子弹"""
        if count < 0:
            return
        self.bullet_count += count

    def launch_bullet(self, count):
        """发射子弹"""
        if count <= 0:
            return
        if self.bullet_count == 0:
            print(f"当前子弹数量为0，请装填子弹")
        elif self.bullet_count <= count:
            self.bullet_count = 0
            print("清空弹夹")
        else:
            self.bullet_count -= count


class Soldiers:
    """士兵"""

    def __init__(self, name: str, arms: Arms):
        self.name = name
        self.arms = arms

    def add_bullet(self, count: int):
        """装填子弹"""
        self.arms.add_bullet(count)

    def fire(self, count: int):
        """开火"""
        self.arms.launch_bullet(count)

    def __str__(self):
        return f"士兵{self.name}, 有一把{self.arms.name}, 剩余子弹{self.arms.bullet_count}发"


if __name__ == "__main__":
    ak47 = Arms("AK47")
    s = Soldiers("瑞恩", ak47)
    print(s)
    s.add_bullet(10)  # 士兵装子弹
    ak47.add_bullet(10)  # 枪装填子弹
    ak47.add_bullet(-10)  # 子弹装填数为负
    print(s)
    s.fire(10)  # 开火
    print(s)
    s.fire(100)  # 清空弹夹

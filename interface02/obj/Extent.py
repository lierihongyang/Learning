# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：Extent.py
@Author  ：LiChunBo
@Date    ：2024/8/1 上午10:49
"""
"""继承"""


class Master:
    def __init__(self):
        self.kongfu = "[五香配方]"
        self.mas_ju = "苹果"

    def make_cake(self):
        print(f"使用：{self.kongfu}制作了煎饼果子")

    def make_mas_judle(self):
        print(f"运用{self.mas_ju}榨果汁")


class School:
    def __init__(self):
        self.kongfu = "[香辣配方]"
        self.mas_ju = "山楂"

    def make_cake(self):
        print(f"唱着歌使用：{self.kongfu}制作了煎饼果子")

    def make_sch_judle(self):
        print(f"运用{self.mas_ju}榨果汁")


class Prentice(School, Master):
    def __init__(self):
        # 将父类的属性继承
        # super().__init__()
        School.__init__(self)
        Master.__init__(self)

        self.kongfu = "[独创配方]"

    def make_cake(self):
        print(f"唱着歌跳着舞使用：{self.kongfu}制作了煎饼果子")

    """调用父类的方法"""

    def make_master_cake(self):
        Master.__init__(self)  # 初始化Master
        Master.make_cake(self)

    def make_school_case(self):
        School.__init__(self)  # 初始化School
        School.make_cake(self)


if __name__ == '__main__':
    p = Prentice()
    # p.make_cake()
    # p.make_judle()
    p.make_master_cake()
    p.make_school_case()

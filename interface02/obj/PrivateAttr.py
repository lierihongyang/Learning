# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：PrivateAttr.py
@Author  ：LiChunBo
@Date    ：2024/8/1 下午1:55
"""


class Master:
    def __init__(self):
        self.kongfu = "[五香]"
        self.__money = 200

    def __get_money(self):
        return self.__money

    def cooke(self):
        print(f"使用了{self.kongfu}")

    def get_money(self):
        print(f"money: {self.__get_money()}")

    def set_money(self, n):
        return self.__money + n


class Pri(Master):
    pass


if __name__ == '__main__':
    xx = Pri()
    xx.cooke()
    # print(xx.__money)

    # 查看类有哪些属性
    print(f"Master类的属性: \n{Master.__dict__}")
    print(f"Pri类的属性: \n{Pri.__dict__}")

    # print(f"强行获取私有属性:  {xx._Master__money}")
    # print(xx._Master__get_money())
    xx.set_money(100)
    xx.get_money()

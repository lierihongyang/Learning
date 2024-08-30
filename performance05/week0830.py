# -*- coding: UTF-8 -*-


class Television:
    """
    电视机类(Television)
        属性:品牌(brand)、型号(model)、颜色(color)、价格(price)
        方法:打开(turnOn)、关闭(turnOff)、切换频道(changeChannel)
        实现一个方法来检查电视是否已打开，只有在打开状态下才能切换频道
    """

    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.status = False  # 电视机状态 默认关闭

    def turn_on(self):
        print(f"{self.model}型号电视机已打开")
        self.status = True

    def turn_off(self):
        print(f"{self.model}型号电视机已关闭")
        self.status = False

    def change_channel(self, channel):
        if self.status:
            print(f"切换到{channel}频道")
        else:
            print(f"电视机已关闭，无法切换频道。请打开电视机")


def generate_fibe(num: int):
    """
    题目二: 递归实现斐波那契,注意:封装成函数,调用该函数输入数字,比如输入8, 则返回一个含有八个元素的斐波那契列表
    """
    res = []

    def fibe(num: int):
        if num == 1 or num == 2:
            return 1
        return fibe(num - 1) + fibe(num - 2)

    for i in range(1, num + 1):
        res.append(fibe(i))
    return res


if __name__ == '__main__':
    t = Television("小米", "Readmi", "black", 1000)
    print(f"电视机状态：{t.status}")
    t.change_channel("CCTV-1")
    t.turn_on()
    t.change_channel("CCTV-1")
    t.turn_off()
    print("-" * 50)
    print(generate_fibe(8))

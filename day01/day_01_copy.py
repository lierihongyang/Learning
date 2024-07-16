# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@IDE     ：PyCharm
@File    ：day_01_copy.py
@Author  ：LiChunBo
@Date    ：2024/7/16 上午9:31
"""


def format_str():
    name = "李明"
    age = 19
    weight = 66.66

    print("My name is %s." % name)
    print("My weight is %f." % weight)
    print("My weight is %.2f" % weight)
    print("My age is %d." % age)
    print("My age is % 4d" % age)

    print(f"I'm {name}, age: {age}, weight: {weight}")
    print(f"I'm {name}, age: {age}, weight: {weight:.4f}")  # f-string格式化

    print(r"原始字符串，\t所见即所得。\n")
    print("普通字\\符串，\t带转义。\n")


def input_msg():
    num = input("输入一个数字：")
    print(f"输入的内容是：{num}, 类型是：{type(num)}, 转换为int类型：{int(num)}")

    l1 = [1, 2, 3]
    t1 = [4, 5, 6]
    print(f"l1原始类型：{type(l1)}, 转换为元组：{tuple(l1)}")
    print(f"t1原始类型：{type(t1)}, 转换为元组：{list(t1)}")

    str1 = "123"
    str2 = "[1, 2, 3]"
    str3 = "'name'"
    print(f"str1: eval转换后的结果: {eval(str1)}, 类型: {type(eval(str1))}")
    print(f"str2: eval转换后的结果: {eval(str2)}, 类型: {type(eval(str2))}")
    print(f"str3: eval转换后的结果: {eval(str3)}, 类型: {type(eval(str3))}")


def operator():
    """运算符"""
    a, b, c = 1, 2, 3
    print(f"a > b: {a > b}")
    print(f"a > c: {a > c}")
    print(f"a = b = c: {a == b == c}")

    print(f"a != b != c: {a != b != c}")
    print(f"bool(0): {bool(0)}")
    print(f"bool(''): {bool('')}")

    print(True or False)
    print(True and False)
    print(True and True)
    print(not True and True)
    print(not (True and False))
    print(not False)


def branch():
    """分支"""
    age = int(input("请输入年龄："))
    if 0 < age < 18:
        print("未成年")
    elif 18 <= age < 60:
        print("成年劳动力")
    elif age >= 60:
        print("老年")
    else:
        print("输入非法")


def while_():
    """计算100以内偶数累加和"""
    i = 0
    res = 0
    while i <= 100:
        if i %2 ==0:
            res += i
        i += 1
    print(f"100以内偶数累加和为：{res}")
    print(f"100以内偶数累加和为：{sum(i for i in range(0, 101, 2))}")
    print(f"100以内偶数累加和为：{sum(i for i in range(101) if i % 2 == 0)}")


def while_2():
    """break continue"""
    i = 0
    while i < 10:
        if i == 3:
            print(f"\tif 判断，当前i == {i}, continue.")
            i += 1
            continue
        elif i == 8:
            print(f"\tif 判断，当前i == {i}, break 退出循环")
            break
        print(f"主循环中：i == {i}")
        i += 1


if __name__ == '__main__':
    # format_str()
    # input_msg()
    # operator()
    # branch()
    # while_()
    while_2()

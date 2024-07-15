# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@IDE     ：PyCharm
@File    ：day_01.py
@Author  ：LiChunBo
@Date    ：2024/7/15 上午11:14
"""


def format_str():
    name = "小明"
    age = 20
    weight = 60.2

    print("My name is %s." % name)
    print("My weight is %f" % weight)
    print("My weight is %.2f" % weight)
    print("My age is %04d" % age)
    print("My age is %d" % age)

    print(f"I'm {name}, age: {age}, weight: {weight}")
    print(f"f-string格式化：{123.123:.2f}")

    print("转义\t转\n义")
    print(r"转义\t转\n义")
    print("end.end", end="\t")
    print("end.end")


def input_msg():
    print("开始：")
    msg = input("请输入要打印的信息：")
    print(type(msg))
    print(f"你输入的信息是：{msg}")


def type_con():
    num = input("请输入一个数字：")
    print(f"类型转化前：{type(num)}, 类型转化后：{int(num)}")

    l = [1, 2, 3]
    t = (4, 5, 6)
    print(f"l 转化前：{type(l)}, l转化后：{tuple(l)}")
    print(f"t 转化前：{type(t)}, l转化后：{list(t)}")

    str1 = "10"
    str2 = "[0, 1, 2]"
    str3 = "'name'"
    print(f"str1: eval: {eval(str1)}, type: {type(eval(str1))}")
    print(f"str2: eval: {eval(str2)}, type: {type(eval(str2))}")
    print(f"str3: eval: {eval(str3)}, type: {type(eval(str3))}")


def operator():
    """运算符"""
    a = 3
    b = 0
    c = 9
    print(f"a > b: {a > b}")
    print(f"a < b: {a < b}")
    print(f" a == c: {a == c}")

    print(f"a != b: {a != b}")
    print(f"a and b: {a and b}")
    print(f"a or b: {a or b}")
    print(f"not a and b: {not a and b}")

    if True and False or True:
        print(f"and or: {True}")

    if (True or False) and True:
        print(f"or and: {True}")

    if 0:
        print(00000000000)
    elif "0":
        print(11111111111111111)


def branch():
    """分支判断"""
    age = int(input("请输入年龄："))
    if age >= 18:
        print("可以上网")
    else:
        print("未满18周岁，不可以上网")
    print("判断结束")


def mul_branch():
    """多重判断"""
    age = int(input("请输入年龄："))
    if 0 <= age < 18:
        print("童工")
    elif 18 <= age < 60:
        print("工作")
    elif age >= 60:
        print("养老")
    else:
        print("输入非法")


def nest():
    """条件嵌套"""
    cash = int(input("请输入余额："))
    if cash > 0:
        print("上车")
        seat = int(input("公交车剩余座位："))
        if seat > 0:
            print("在公交车上坐着")
        else:
            print("在公交车上站着")
    else:
        print("走路上班")


def while_1():
    """循环5次"""
    i = 0
    while i  < 5:
        print(f"正在循环--->{i+1}")
        i += 1


def while_2():
    """计算5以内累加和"""
    i = 0
    res = 0
    while i <= 5:
        res += i
        i += 1
    print(f"5以内数字的累加和为：{res}")
    print(f"5以内数字的累加和为：{sum(i for i in range(6))}")


def while_3():
    """计算100以内偶数累加和"""
    i = 0
    res = 0
    while i <= 100:
        if i % 2 == 0:
            res += i
        i += 1
    print(f"100以内偶数累加和：{res}")
    print(f"100以内偶数累加和：{sum(i for i in range(0, 101, 2))}")


def break_1():
    """break"""
    i = 0
    while i < 10:
        if i == 4:
            print("没有工具了")
            break
        print(f"已完成：{i + 1}次工作")
        i += 1


def continue_1():
    """continue"""
    i = 0
    while i < 10:
        if i == 4:
            print("这个工具是坏的")
            i += 1
            continue
        print(f"已完成：{i + 1}次工作")
        i += 1


def print_square():
    """打印正方形"""
    i = 0
    while i < 5:
        j = 0
        while j < 5:
            print("*", end="")
            j += 1
        print()
        i += 1


def while_else_1():
    """循环正常结束"""
    i = 0
    while i < 3:
        print(f"正常循环{i}")
        i += 1
    else:
        print("循环正常结束")


def while_else_2():
    """循环break"""
    i = 0
    while i < 3:
        if i == 2:
            print(f"i={i}, break")
            break
        print(f"正常循环：{i}")
        i += 1
    else:
        print("循环异常")


def while_else_3():
    """循环break"""
    i = 0
    while i < 3:
        if i == 2:
            print(f"i={i}, continue")
            i += 1
            continue
        print(f"正常循环：{i}")
        i += 1
    else:
        print("continue 循环正常结束")


if __name__ == "__main__":
    # format_str()
    # input_msg()
    # type_con()
    # operator()
    # branch()
    # mul_branch()
    # nest()
    # while_1()
    # while_2()
    # while_3()
    # break_1()
    # continue_1()
    # print_square()
    # while_else_1()
    # while_else_2()
    while_else_3()

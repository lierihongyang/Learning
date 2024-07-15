# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@IDE     ：PyCharm
@File    ：work.py
@Author  ：LiChunBo
@Date    ：2024/7/15 下午4:57
"""

import random
import sys


def play_fist_game():
    """猜拳游戏"""
    # 0, 1, 2 分别代表石头、剪刀、布
    people_res = int(input("输入你的结果："))
    if not (0 <= people_res <= 2):
        sys.exit("输入错误，退出游戏")
    computer_res = random.randint(0, 2)
    print(f"电脑结果：{computer_res}")
    if people_res == computer_res:
        print("平局")
    elif people_res == 0 and computer_res == 1:
        print("你赢了")
    elif people_res == 1 and computer_res == 2:
        print("你赢了")
    elif people_res == 2 and computer_res == 0:
        print("你赢了")
    else:
        print("你输了")


def play_fist_game2():
    """猜拳游戏2"""
    # 0, 1, 2 分别代表石头、剪刀、布
    people_res = int(input("输入你的结果："))
    if not (0 <= people_res <= 2):
        sys.exit("输入非法，退出游戏")
    computer_res = random.randint(0, 2)
    print(f"电脑结果：{computer_res}")
    res = people_res - computer_res
    if res == 0:
        print("平局")
    elif res == -1 or res == 2:
        print("你赢了")
    else:
        print("你输了")


def print_mult_tables():
    """打印九九乘法表"""
    column = 1
    while column <= 9:
        line = 1
        while line <= column:
            print(f"{line}*{column}={column*line}", end="\t")
            line += 1
        print()
        column += 1
    print("="*50)
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f"{j}*{i}={j*i}", end="\t")
        print()


def print_square():
    """打印正方形"""
    for i in range(5):
        for j in range(5):
            print("*  ", end="")
        print()


def print_triangle_left():
    """打印左对齐三角形"""
    for i in range(1, 8):
        print("*" * i, end="")
        print()


def print_triangle_right():
    """打印右对齐三角形"""
    lines = 8
    for i in range(1, lines + 1):
        print(" " * (lines - i) + "*" * i, end="")
        print()


def print_isosceles_triangle():
    """打印等腰三角形"""
    lines = 5
    for i in range(1, lines + 1):
        print(" " * (lines - i) + "*" * (2 * i - 1) + " " * (lines - i))


if __name__ == '__main__':
    # play_fist_game()
    # play_fist_game2()
    # print_mult_tables()
    # print_square()
    # print_triangle_left()
    # print_triangle_right()
    print_isosceles_triangle()

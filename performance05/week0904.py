# -*- coding: UTF-8 -*-
"""
1-列表[1,7,3,4,3,9,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
2-求100以内的质数(只能被1和它本身整除
3-文件data.txt内存在以下内容(请自行创建,lucy:21,tom:30xiaoming:18,xiaohong:15xiaowang:20,xiaohei:19
请结合正则的方法找到最大年龄和最小年龄
"""
import re


def ans_1():
    """
    1-列表[1,7,3,4,3,9,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
    """
    l = [1, 7, 3, 4, 3, 9, 2, 5, 5, 8, 9, 7]
    res = list(set(l))
    print(f"res: {res}")


def ans_2():
    """
    2-求100以内的质数(只能被1和它本身整除
    """
    res = []
    for i in range(2, 101):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            res.append(i)
    print(f"100以内的质数: {res}")


def ans_3():
    """
    3-文件data.txt内存在以下内容(请自行创建,lucy:21,tom:30xiaoming:18,xiaohong:15xiaowang:20,xiaohei:19
请结合正则的方法找到最大年龄和最小年龄
    """
    name_pattern = re.compile(r"(.*?):\d\d")
    age_pattern = re.compile(r":(\d\d)")
    info = {}
    with open("./data.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            names = name_pattern.findall(line)
            ages = age_pattern.findall(line)
            tmp = zip(names, ages)
            info.update(dict(tmp))
    res = sorted(info.items(), key=lambda ele: int(ele[1]))
    print(f"""{res[-1][0].replace(',', '')} 的年龄是: {res[-1][-1]},
{res[0][0].replace(',', '')} 的年龄是: {res[0][-1]}
""")


if __name__ == '__main__':
    ans_1()
    print("*" * 50)
    ans_2()
    print("*" * 50)
    ans_3()

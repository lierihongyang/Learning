# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：work_1.py
@Author  ：LiChunBo
@Date    ：2024/7/18 下午2:49
"""
import random


# 1.需求：有三个办公室，8位老师，8位老师随机分配到3个办公室
def answer_1():
    teachers = [i for i in range(1, 9)]
    rooms = [[], [], []]
    for teacher in teachers:
        index = random.randint(0, 2)
        rooms[index].append(teacher)
    for room in rooms:
        print(room)


# 2、求100以内能被3整除的数，并将作为列表输出
def answer_2():
    res = [i for i in range(101) if i % 3 == 0]
    print(res)


# 3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表  # 不允许用强制类型转化
def answer_3_1():
    nums = [1, 2, 3, 4, 3, 4, 2, 5, 5, 8, 9, 7]
    res = []
    for ele in nums:
        if ele not in res:
            res.append(ele)
    print(res)


def answer_3_2():
    nums = [1, 2, 3, 4, 3, 4, 2, 5, 5, 8, 9, 7]
    num_info = {ele: nums.count(ele) for ele in nums}
    res = list(num_info.keys())
    print(res)


# 4、求斐波那契数列 1 1 2 3 5 8 13 ……    12个
def answer_4():
    res = []
    a, b = 1, 1
    for i in range(1, 13):
        if i == 1 or i == 2:
            res.append(1)
        else:
            a, b = b, a + b
            res.append(b)
    print(res)


def ans_wer_4_2(n):
    if n == 1 or n == 2:
        return 1
    return ans_wer_4_2(n - 1) + ans_wer_4_2(n - 2)


# 5、求100以内的质数（只能被1和它本身整除）
def answer_5():
    res = [0, 1]
    for i in range(2, 101):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            res.append(i)
    print(res)


# 6、有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef #不允许用类型转化
def answer_6():
    s = "aabbbcddef"
    s_info = {ele: s.count(ele) for ele in s}
    new_s = ""
    for k, v in s_info.items():
        if v == 1:
            new_s += k
    print(new_s)


# 7、有一堆字符串，“welocme to super&Test”，打印出superTest，#不能查字符的索引
def answer_7():
    str1 = "welocme to super&Test"
    tmp_list = str1.split(" ")
    for ele in tmp_list:
        if "super" in ele:
            print(ele.replace("&", ""))


# 8、有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ... #不允许用reverse,和reversed
def answer_8_1():
    str1 = "welocme to super&Test"
    tmp_list = list(str1)
    res_str = ""
    for _ in range(len(tmp_list)):
        res_str += tmp_list.pop()
    print(res_str)


def answer_8_2():
    str1 = "welocme to super&Test"
    tmp_list = list(str1)
    str_length = len(str1)  # 21  10
    for i in range(str_length // 2):
        tmp_list[i], tmp_list[str_length - 1 - i] = tmp_list[str_length - 1 - i], tmp_list[i]
    res = "".join(tmp_list)
    print(res)


# 9、有一堆字符串，“abcdef”，将首尾反转，结果：fedcba，不能使用用reverse,和reversed,不允许用步长
def answer_9():
    str1 = "abcdef"
    tmp_list = list(str1)
    res = ""
    for _ in range(len(tmp_list)):
        res += tmp_list.pop()
    print(res)


# 10、有一堆字符串，“aabbbcddef”，输出abcdef # 不允许用set
def answer_10():
    str1 = "aabbbcddef"
    str_info = {ele: str1.count(ele) for ele in str1}
    res = ""
    for s in str_info.keys():
        res += s
    print(res)


if __name__ == '__main__':
    # answer_1()
    # answer_2()
    # answer_3_1()
    # answer_3_2()
    # answer_4()
    # res_4 = []
    # for i in range(1, 13):
    #     res_4.append(ans_wer_4_2(i))
    # print(res_4)

    # answer_5()
    # answer_6()
    # answer_7()
    answer_8_1()
    answer_8_2()
    # answer_9()
    # answer_10()

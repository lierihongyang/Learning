# -*-coding:utf-8 -*-

"""
# File       : week_work.py
# Time       ：2024/7/23 下午2:44
# Author     ：Li
"""
import random
import sys


class Day1:
    def __init__(self):
        print("day01".center(60, '='))

    def format_str(self):
        """字符串格式化"""
        name = "Ll"
        age = 21
        weight = 60.2
        print("name: %s" % name)
        print("weight: %f" % weight)
        print("weight: %.2f" % weight)
        print("age: %d" % age)
        print("age: %04d" % age)
        print(f"name: {name}, age: {age}, weight: {weight},,,{weight:.2f}")

    def type_con(self):
        """将字符串转化为python表达式"""
        s1 = "10"
        s2 = "[1, 2, 3]"
        s3 = "'name'"
        print(f"转换前s1：{type(s1)}, 转换后：{type(eval(s1))}")
        print(f"转换前s2：{type(s2)}, 转换后：{type(eval(s2))}")
        print(f"转换前s3：{type(s3)}, 转换后：{type(eval(s3))}")

    def operator(self):
        """运算符"""
        print(f"1>2: {1 > 2}")
        print(f"1<2: {1 < 2}")
        print(f"1!=2: {1 != 2}")
        print(f"True and False: {True and False}")
        print(f"True or False: {True or False}")
        print(f"not True: {not True}")

    def play_game(self):
        """猜拳游戏"""
        people = int(input("请输入结果："))
        if not (0 <= people <= 2):
            sys.exit("输入非法")
        com = random.randint(0, 2)
        print(f"电脑结果：{com}")
        res = people - com
        if res == 0:
            print("平局")
        elif res == -1 or res == -2:
            print("玩家赢")
        else:
            print("电脑赢")

    def print_mult_tables(self):
        """打印九九乘法表"""
        for i in range(1, 10):
            for j in range(1, i + 1):
                print(f"{j}*{i}={i * j}", end="\t")
            print()

    def print_graph(self):
        """打印图形"""
        print("打印正方形".center(60, '-'))
        for i in range(5):
            for j in range(5):
                print("*  ", end="")
            print()
        print("打印左对齐三角形".center(60, '-'))
        for i in range(1, 8):
            print("*" * i, end="")
            print()
        print("打印右对齐三角形".center(60, '-'))
        for i in range(1, 9):
            print(" " * (9 - i) + "*" * i, end="")
            print()
        print("打印等腰三角形".center(60, '-'))
        for i in range(1, 6):
            print(" " * (6 - i) + "*" * (2 * i - 1) + " " * (6 - i))


class Day2:
    def __init__(self):
        print("day02".center(60, '='))

    def str_concat(self):
        """字符串练习"""
        print("字符串切片".center(60, '-'))
        s = "123456abcdefg"
        print(f"截取全部字符串s[::]：{s[::]}")
        print(f"开始位置超出索引s[:100::]: {s[100::]}。")
        print(f"结束位置超出索引s[:100:]: {s[:100:]}")
        print(f"逆序截取s[::-1]: {s[::-1]}")
        # print(f"下标越界：{s[100]}")
        print(f"设置步长为2：{s[::2]}")
        print(f"设置步长为负：{s[3::-2]}")
        print("字符串常用方法--查找".center(60, '-'))
        mystr = "hello world and supertest and chenghao and Python"
        print(f"find(str, start, end): {mystr.find('and', 20, 50)}")
        print(f"find(str, start, end): {mystr.find('ands', 20, 50)}")
        print(f"find(): {mystr.find('and')}")
        print(f"index(str, start, end): {mystr.index('and', 10, 30)}")
        # print(f"index(str, start, end): {mystr.index('ands', 10, 30)}")
        print(f"index(): {mystr.index('and')}")
        print(f"count()统计字符串数量：{mystr.count('and')}")
        print(f"count()统计字符串数量：{mystr.count('ands')}")
        print(f"字符串常用方法--修改".center(60, '-'))
        print(f"字符串首字母大写：{mystr.capitalize()}")
        print(f"所有字母大写：{mystr.upper()}")
        print(f"所有字母小写：{mystr.lower()}")
        print(f"替换：{mystr.replace('and', '-->')}")
        print(f"替换：{mystr.replace('and', '-->', 2)}")
        print(f"分割：{mystr.split()}")
        print(f"字符串拼接：{'='.join('abc')}")
        print(f"字符串拼接：{'='.join('a')}")
        print(f"字符串拼接：{'='.join('')}")
        print(f"移除两端空白：{'  abc '.strip()}")
        print(f"左对齐：{'aaa'.ljust(30, '-')}")
        print(f"居中：{'aaa'.center(30, '-')}")
        print(f"右对齐：{'aaa'.rjust(30, '-')}")
        print(f"字符串常用方法--判断".center(60, '-'))
        print(f"字符串开头判断：{mystr.startswith('hello')}")
        print(f"字符串结尾判断：{mystr.endswith('hello')}")
        print(f"判断字符串是否全部由字母组成：{'abc'.isalpha()}")
        print(f"判断字符串是否仅由数字 or 字母 or 两者构成：{'abc_123'.isalnum()}")  # False
        print(f"判断字符串是否仅由数字 or 字母 or 两者构成：{'abc123'.isalnum()}")  # True
        print(f"判断字符串是否仅由数字 or 字母 or 两者构成：{'123'.isalnum()}")  # True
        print(f"判断字符串是否仅由数字 or 字母 or 两者构成：{'abc'.isalnum()}")  # True
        print(f"判断字符串是否仅由数字 or 字母 or 两者构成：{'_'.isalnum()}")  # False
        print(f"判断字符串是否由数字组成：{'234'.isalnum()}")
        print(f"判断字符串是否由数字组成：{'234abc'.isdigit()}")

    def list_concat(self):
        """列表的练习"""
        name_list = ["Tom", "Lily", "Jack", "Rose"]
        print(f"查找相关".center(60, '-'))
        print(f"根据索引取元素：{name_list[0]}")
        print(f"index(ele, start, end)获取元素下标，不存在就报错：{name_list.index('Tom')}")
        print(f"获取元素个数：{len(name_list)}")
        print(f"修改相关".center(60, '-'))
        name_list.append('abc')
        print(f"append(ele),在列表末尾添加元素：{name_list}")
        name_list.extend('abc')
        name_list.extend([1, 2])
        print(f"extend(eles), 将序列拆分并逐个加入到列表: {name_list}")
        name_list.insert(100, '-->')
        name_list.insert(0, '-->')
        print(f"insert(index, ele), 在指定位置插入元素，下标越界时，则追加在末尾：{name_list}")
        name_list.remove('Tom')
        print(f"remove(ele), 移除指定元素，元素不存在就报错：{name_list}")
        print(f"pop(index),移除指定索引的元素，默认最后一个元素并返回: {name_list.pop(3)}")
        print(f"pop(index),移除指定索引的元素，默认最后一个元素并返回: {name_list.pop()}")
        print(f"clear(), 清空列表")
        nums = [1, 5, 3, 2, 8]
        print(f"原列表：{nums}\n排序后：{nums.sort()}==> {nums}")
        print(f"不改变原列表排序：{sorted(nums, reverse=True)}")
        print(f"逆序前：{nums}\n逆序后：{nums.reverse()} ==> {nums}")
        print(f"不改变原列表逆序：{list(reversed(nums))}")

    def tuple_concat(self):
        """元组练习"""
        print("元组查找系列方法".center(60, '-'))
        tuple1 = (1, 2, 3, 'a', 'b', [4, 5, 6])
        print(f"根据下标获取元素：{tuple1[0]}")
        print(f"index(ele, start, end),获取指定元素下标，不存在就报错: {tuple1.index('a')}")
        print(f"获取元素个数：{len(tuple1)}")
        print(f"判断某元素是否在元组中：{1 in tuple1}")
        print(f"修改前元素地址：{id(tuple1[-1])}")
        tuple1[-1][0] = 0
        print(f"修改元组内的可变元素(不建议)：{tuple1}")
        print(f"修改后元素地址：{id(tuple1[-1])}")

    def dict_concat(self):
        """字典练习"""
        dict1 = {"name": "ll", "age": 23, "sex": "男"}
        print(f"字典查询、修改操作".center(60, '-'))
        print(f"根据键获取值，键不存在时会报错：{dict1['name']}")
        print(f"根据键获取值，键不存在则返回默认值：{dict1.get('aa', 0)}")
        dict1["country"] = "China"
        print(f"添加键值对：{dict1}")
        print(f"获取所有键值对：{dict1.items()}")
        print(f"获取所有的键：{dict1.keys()}")
        print(f"获取所有的值：{dict1.values()}")
        dict1.update({"height": 170})
        print(f"合并字典：{dict1}")
        print(f"删除指定的键的值，并将其返回：{dict1.pop('height')}")
        print(f"清空字典：{dict1.clear()} ==> {dict1}")

    def set_concat(self):
        """集合练习"""
        print(f"集合相关方法".center(60, '-'))
        set1 = {1, 2, 3, 'z', 'b', 'c'}
        set1.add('123')
        print(f"向集合中追加元素，add(): {set1}")
        print(f"合并两个集合：{set1.update({'ele1', 'ele2'})}")
        print(f"移除指定元素，不存在就报错：{set1.remove(1)}\n移除后：{set1}")
        print(f"移除指定元素，不存在则舞动着，discard(ele): {set1.discard('0')}")
        print(f"随机移除一个元素并将其返回：{set1.pop()}")
        new_set = {True, False, 0, 1, 3}
        print(f"new set: {new_set}")
        s1 = {1, 2, 3, 4}
        s2 = {3, 4, 5, 6}
        print(f"两个集合取交集：{s1 & s2}")
        print(f"两个集合取并集：{s1 | s2}")
        print(f"两个集合取差集：{s1 - s2}")

    def pub_func(self):
        """一些公共的方法"""
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        print(f"`+`: {l1 + l2}")
        d = {1: "a", 2: "b"}
        print(f"判断`1`是否在dict中：{1 in d}")
        print(f"最大值：{max(l1)}")
        print(f"最小值：{min(l2)}")
        print(f"列表推导式：{[i for i in range(10)]}")
        # 找出字符串中所有的字母`o`及其下标
        for i, e in enumerate("ajkfafoofasfaoasfasdofasofasdfagdo"):
            if e == 'o':
                print(f"index: {i}, value: {e}")

    def genex_concat(self):
        """生成式练习"""
        print(f"生成式练习".center(60, '-'))
        print(f"生成一个偶数列表：{[i for i in range(10) if i % 2 == 0]}")
        # 生成如下示例的列表：[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        l = [(i, j) for i in range(1, 3) for j in range(3)]
        print(l)
        print(f"字典推导式".center(60, '-'))
        l1 = [1, 2, 3]
        l2 = ['a', 'b', 'c']
        d = {l2[i]: l1[i] for i in range(len(l1))}
        print(d)
        # 筛选出数量大于200的电脑型号
        counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
        d2 = {k: v for k, v in counts.items() if v > 200}
        print(f"型号大于200的电脑型号：{d2}")
        print("集合推导式".center(60, '-'))
        nums = [2, 4, 6]
        s = {i ** 2 for i in nums}
        print(f"set: {nums}")

    def ans_1(self):
        """有三个办公室，8位老师，8位老师随机分配到3个办公室"""
        teachers = [i for i in range(1, 9)]
        rooms = [[], [], []]
        for tea in teachers:
            room = random.randint(0, 2)
            rooms[room].append(tea)
        for room in rooms:
            print(room)

    def ans_2(self):
        """计算100以内能被3整除的数"""
        print(f"100以内能被3整除的数：{[i for i in range(100) if i % 3 == 0]}")

    def ans_3(self):
        """列表去重，不使用强制类型转化"""
        nums = [1, 2, 3, 4, 3, 4, 2, 5, 5, 8, 9, 7]
        res = []
        for ele in nums:
            if ele not in res:
                res.append(ele)
        print(res)

    def ans_4(self):
        """斐波那契数列"""
        res = []
        a, b = 1, 1
        for i in range(1, 13):
            if i == 1 or i == 2:
                res.append(1)
            else:
                a, b = a, a + b
                res.append(b)
        print(f"前12位斐波那契数：{res}")

    def ans_5(self):
        """计算100以内质数"""
        res = [0, 1]
        for i in range(2, 101):
            for j in range(2, i):
                if i % 2 == 0:
                    break
            else:
                res.append(i)
        print(f"100以内质数：{res}")

    def ans_6(self):
        """有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef 不使用类型转化"""
        s = "aabbbcddef"
        res = ""
        for e in s:
            if s.count(e) == 1:
                res += e
        print(f"结果：{res}")

    def ans_7(self):
        str1 = "welocme to super&Test"
        tmp_list = str1.split(" ")
        for ele in tmp_list:
            if "&" in ele:
                print(ele.replace("&", ""))

    def ans_8(self):
        """有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ... #不允许用reverse,和reversed"""
        str1 = "welocme to super&Test"
        tmp_list = list(str1)
        res = ""
        for _ in range(len(tmp_list)):
            res += tmp_list.pop()
        print(res)

    def ans_9(self):
        """有一堆字符串，“abcdef”，将首尾反转，结果：fedcba，不能使用用reverse,和reversed,不允许用步长"""
        str1 = "abcdef"
        res = ""
        for s in str1:
            res = s + res
        print(res)

    def ans_10(self):
        """有一堆字符串，“aabbbcddef”，输出abcdef # 不允许用set"""
        str1 = "aabbbcddef"
        res = ""
        for s in str1:
            if s not in res:
                res += s
        print(res)


if __name__ == '__main__':
    # day1 = Day1()
    # day1.format_str()
    # day1.type_con()
    # day1.operator()
    # day1.play_game()
    # day1.print_mult_tables()
    # day1.print_graph()
    day2 = Day2()
    # day2.str_concat()
    # day2.list_concat()
    # day2.tuple_concat()
    # day2.dict_concat()
    # day2.set_concat()
    # day2.pub_func()
    # day2.genex_concat()
    # day2.ans_1()
    # day2.ans_2()
    # day2.ans_3()
    # day2.ans_4()
    # day2.ans_5()
    # day2.ans_6()
    # day2.ans_7()
    # day2.ans_8()
    # day2.ans_9()
    day2.ans_10()

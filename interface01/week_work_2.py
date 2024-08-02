# -*-coding:utf-8 -*-

"""
# File       : week_work1.py
# Time       ：2024/7/30 下午3:01
# Author     ：Li
"""
import json
import os
import random
import shutil
import sys

import requests


class Day1:
    def __init__(self):
        print("day01".center(60, '='))

    def format_str(self):
        print("name: %s" % "Lll")
        print("age: %d" % 20)
        print("weight: %f" % 60.0)
        print("weight: %.2f" % 60.0)
        print("age: %04d" % 10)

    def type_con(self):
        print(f"转换前数据类型：{type('10')}, 转换后类型：{type(eval('10'))}")
        print(f"转换前数据类型：{type('[1, 2, 3]')}, 转换后类型：{type(eval('[1, 2, 3]'))}")

    def operator(self):
        """运算符"""
        print(f"1 == 1: {1 == 1}")
        print(f"1 > 1: {1 > 1}")
        print(f"True and False: {True and False}")
        print(f"True or False: {True or False}")
        print(f"not False: {not False}")

    def play_game(self):
        """猜拳游戏"""
        people_res = int(input("输入结果："))
        if not (0 <= people_res <= 2):
            sys.exit("输入非法")
        com_res = random.randint(0, 2)
        print(f"电脑结果：{com_res}")
        res = people_res - com_res
        if res == 0:
            print("平局")
        elif res == -1 or res == -1:
            print(f"你赢了")
        else:
            print("你输了")

    def print_mult_tables(self):
        """九九乘法表"""
        for i in range(1, 10):
            for j in range(1, i + 1):
                print(f"{j} * {i} = {i * j}", end="\t")
            print()

    def print_graph(self):
        """打印图形系列"""
        print("正方形".center(60, '-'))
        for i in range(5):
            for j in range(5):
                print("*  ", end="")
            print()
        print("左对齐三角形".center(60, '-'))
        for i in range(1, 8):
            print("*" * i, end="")
            print()
        print("右对齐三角形".center(60, '-'))
        for i in range(1, 9):
            print(" " * (9 - i) + "*" * i, end="")
            print()
        print("等腰三角形".center(60, '-'))
        for i in range(1, 6):
            print(" " * (6 - i) + "*" * (2 * i - 1) + " " * (6 - i))


class Day2:
    def __init__(self):
        print("day02".center(60, "="))

    def str_concat(self):
        """字符串练习"""
        print(f"字符串切片".center(60, "-"))
        s = "123456qwertyuiop"
        print(f"截取全部：{s[::]}")
        print(f"开始位置索引越界：{s[100::]}")
        print(f"结束位置索引越界：{s[:100:]}")
        print(f"逆序截取：{s[::-1]}")
        # print(f"下标越界：{s[100]}")
        print(f"设置步长：{s[::2]}")
        print(f"设置步长为负：{s[6::-2]}")
        print("字符串查找系列方法".center(60, "-"))
        mystr = "hello world and supertest and chenghao and Python"
        print(f"find(ele, start, end): {mystr.find('and', 10, 20)}")
        print(f"find(ele, start, end): {mystr.find('ands', 10, 20)}")
        print(f"index(ele, start, end: {mystr.index('and', 10, 20)}")
        # print(f"index(ele, start, end: {mystr.index('ands', 10, 20)}")
        print(f"count(), 统计次数: {mystr.count('and')}")
        print(f"count(), 统计次数: {mystr.count('ands')}")
        print(f"修改系列方法".center(60, "-"))
        print(f"字符串首字母大写：{mystr.capitalize()}")
        print(f"所有字母大写：{mystr.upper()}")
        print(f"所有字母小写：{mystr.lower()}")
        print(f"替换：{mystr.replace('and', '==>')}")
        print(f"分割：{mystr.split(' ')}")
        print(f"字符串拼接：{'-'.join('abc')}")
        print(f"字符串拼接：{''.join('abc')}")
        print(f"字符串拼接：{'123'.join('')}")
        print(f"移除两侧空白：{' aa   '.strip()}")
        print(f"左对齐：{'abc'.ljust(20, '-')}")
        print(f"右对齐：{'abc'.rjust(20, '-')}")
        print("字符串判断系列".center(60, '-'))
        print(f"字符串开头判断：{mystr.startswith('hello')}")
        print(f"字符串结尾判断：{mystr.endswith('hello')}")
        print(f"判断字符串是否全部都是字母：{'abc'.isalpha()}")
        print(f"判断字符串是否只包含数字或字母：{'ab'.isalnum()}")
        print(f"判断字符串是否只包含数字或字母：{'12'.isalnum()}")
        print(f"判断字符串是否只包含数字或字母：{'12ab'.isalnum()}")
        print(f"判断字符串是否只包含数字或字母：{'12_ab'.isalnum()}")
        print(f"判断字符串是否只包含数字：{'123'.isdigit()}")

    def list_concat(self):
        """列表"""
        list1 = ["1", "a", "3", "2"]
        print("查找系列方法".center(60, "-"))
        print(f"根据索引获取元素：{list1[2]}")
        print(f"index(ele, start, end): {list1.index('a')}")
        print(f"元素个数：{len(list1)}")
        print("修改相关".center(60, "-"))
        list1.append("abc")
        print(f"append(): {list1}")
        list1.extend("qaz")
        print(f"extend: {list1}")
        list1.insert(0, "==>")
        list1.insert(100, "==>")
        print(f"insert: {list1}")
        list1.remove("a")
        print(f"remove: {list1}")
        print(f"pop()默认最后一个:{list1.pop()}")
        print(f"pop(0)指定索引:{list1.pop(0)}")
        nums = [1, 3, 9, 2, 7]
        print(f"原列表：{nums}\n排序后：{nums.sort()}==> {nums}")
        print(f"不改变原列表排序：{sorted(nums, reverse=True)}")
        print(f"逆序前：{nums}\n逆序后：{nums.reverse()} ==> {nums}")
        print(f"不改变原列表逆序：{list(reversed(nums))}")

    def tuple_concat(self):
        tuple1 = (1, 2, 3, 'a', 'b', [4, 5, 6])
        print("元组查找系列方法".center(60, "-"))
        print(f"根据下标获取元素：{tuple1[0]}")
        print(f"index(ele, start, end): {tuple1.index('a')}")
        print(f"获取元素个数：{len(tuple1)}")
        print(f"判断元素是否在元组中: {1 in tuple1}")
        print(f"修改前元素地址：{id(tuple1[-1])}")
        tuple1[-1][0] = 0
        print(f"修改元组内的可变元素(不建议)：{tuple1}")
        print(f"修改后元素地址：{id(tuple1[-1])}")

    def dict_concat(self):
        """字典练习"""
        dict1 = {"name": "l", "age": 25, "sex": "男"}
        print(f"根据键获取值: {dict1['name']}")
        print(f"根据键获取值: {dict1.get('age')}")
        dict1["country"] = "China"
        print(f"添加键值对：{dict1}")
        print(f"获取所有的键值对：{dict1.items()}")
        print(f"所有的键：{dict1.keys()}")
        print(f"所有的值：{dict1.values()}")
        dict1.update({"height": 170})
        print(f"合并字典：{dict1}")
        print(f"删除指定的键值对：{dict1.pop('height')}")
        print(f"清空字典：{dict1.clear()} ==> {dict1}")

    def set_concat(self):
        """集合"""
        print(f"集合".center(60, "-"))
        set1 = {1, 2, 3, 'a', 'b', 'c'}
        set1.add('s')
        print(f"add(ele): {set1}")
        print(f"移除指定元素，元素不存在就报错：{set1.remove(1)} >> {set1}")
        print(f"移除指定元素，元素不存在就无动作：{set1.discard(1)}")
        print(f"pop()随机移除一位，并将其返回{set1.pop()}")
        new_set = {1, 2, 0, False, True}
        print(f"new set: {new_set}")
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        print(f"交集：{s1 & s2}")
        print(f"并集：{s1 | s2}")
        print(f"差集：{s1 - s2}")
        print(f"差集：{s2 - s1}")

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
        """计算100以内能被3整除的整数"""
        print(f"100以内能被3整除的整数：{[i for i in range(101) if i % 3 == 0]}")

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
        a, b = 1, 1
        for i in range(1, 13):
            if i == 1 or i == 2:
                print(1, end=" ")
            else:
                a, b = b, a + b
                print(b, end=" ")

    def ans_5(self):
        """100以内质数"""
        res = [0]
        for i in range(2, 101):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                res.append(i)
        print(f"100以内的质数：{res}")

    def ans_6(self):
        """有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef 不使用类型转化"""
        s = "aabbbcddef"
        res = ""
        for e in s:
            if s.count(e) == 1:
                res += e
        print(f"res： {res}")

    def ans_7(self):
        """提取并打印superTest"""
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


class Day3:
    def __init__(self):
        print("day03".center(60, "="))

    def return_values(self):
        return 1, "a"

    def fun_params(self, name, age, default="default", *args, **kwargs):
        strs = f"""
name: {name};
age: {age};
default: {default};
args: {args}
kwargs: {kwargs}
"""
        print(strs)

    def file_operator(self):
        """文件操作"""
        with open("./烤地瓜.py", "r") as f:
            print(f"读取文件前10个字节：{f.read(10)}")
            print(f"查看当前指针位置：{f.tell()}")
            print(f"文件剩余内容：{f.read()}")
            print(f"将指针移动到开始：{f.seek(0, 0)}")
            print(f"查看当前指针位置：{f.tell()}")
            print(f"文件第一行内容：{f.readline()}")
            print(f"文件剩余内容：{f.readlines()}")
            print(f"将指针移动到5的位置：{f.seek(5, 0)}")
            print(f"将指针移动到文件末：{f.seek(0, 2)}")

    def os_model(self):
        """os模块的一些方法"""
        print("os.mkdir(), 创建一个空文件夹")
        # os.mkdir("tmp")
        print("os.makedirs(), 递归创建多级目录")
        # os.makedirs("tmp/1/2")
        print("os.remove()删除空文件夹")
        # os.remove("tmp")
        print("shutil.rmtree()删除非空文件夹")
        # shutil.rmtree("tmp/1/2")
        print("os.rename(old, new)文件重命名")
        print(f"获取当前目录：{os.getcwd()}")
        print(f"切换目录：{os.chdir('../')}")
        print(f"获取父级目录：{os.path.dirname(os.getcwd())}")
        print(f"列举目录中的文件、文件夹：{os.listdir()}")


class Day4:
    def __init__(self):
        print("day04".center(60, "="))

    def ans_1(self):
        """列表[1,2,3,4,5,5,2,3,2,4]去重"""
        l = [1, 2, 3, 4, 5, 5, 2, 3, 2, 4]
        res = []
        for ele in l:
            if ele not in res:
                res.append(ele)
        print(f"去重后：{res}")

    def ans_2(self):
        strs = "lucy:21,tom:30,xiaoming:18,xiaohong:15,xiaowang:20,xiaohei:19"
        tmp_list = strs.split(",")
        for ele in tmp_list:
            tmp = ele.split(":")
            if int(tmp[1]) > 18:
                print(f"name: {tmp[0]}, age: {tmp[1]}")

    def ans_3(self):
        """1-100之间能被3整除的数"""
        print(f"res: {[i for i in range(1, 101) if i % 3 == 0]}")

    def ans_4(self):
        """字符串中的每个单词反转"""
        strs = "welocme to super&Test"
        tmp_strs = strs.split(" ")
        res = ""

        def str_rev(s: str) -> str:
            tmp = ""
            for e in s:
                tmp = e + tmp
            return tmp

        for s in tmp_strs:
            res += f"{str_rev(s)} "
        print(res.strip())

    def ans_5(self, n: int):
        """递归实现斐波那契"""
        if n == 1 or n == 2:
            return 1
        return self.ans_5(n - 1) + self.ans_5(n - 2)

    def ans_6(self):
        """将列表中个元素转换成int类型"""
        l = ["1", "2", "3"]
        print(f"res: {[int(i) for i in l]}")


class RoastPotato:
    """烤地瓜"""

    def __init__(self):
        print("烤地瓜".center(60, "="))
        self.cook_time = 0
        self.status = "生的"
        self.seasoning = []

    def cooking(self, t):
        self.cook_time += t
        if 0 <= self.cook_time < 3:
            self.status = "生的"
            print()
        elif 3 <= self.cook_time < 5:
            self.status = "半生不熟的"
        elif 5 <= self.cook_time <= 8:
            self.status = "熟的"
        elif self.cook_time > 8:
            self.status = "糊了"
        else:
            print("烘烤时间不合理")

    def add_sea(self, *args):
        """添加调料"""
        self.seasoning.extend(args)

    def __str__(self):
        return f"烘培时间：{self.cook_time}分钟, 地瓜状态：{self.status}, 添加了{self.seasoning}"


class ReqCont:
    """请求的练习"""

    def __init__(self, url, data=None, params=None):
        self.url = url
        self.data = data
        self.params = params

    def req_get(self):
        """get请求"""
        # params接受的数据会被拼接到url中
        response = requests.get(url=self.url, params=self.params)

        print(f"响应对象: {response}")
        print(f"请求对象: {response.request}")
        print(f"状态码: {response.status_code}")
        print(f"响应体: {response.text}")
        print(f"json格式响应: {response.json()}")
        print(f"字节格式响应: {response.content}")
        print("=" * 60)
        print(f"请求头: {response.request.headers}")
        print(f"请求体(get请求没有): {response.request.body}")
        print(f"请求地址: {response.url}")

    def post_frame(self):
        # data接收的参数会被传递到请求体中
        response = requests.post(self.url, data=self.data)
        print(f"响应体: {response.text}")

    def post_json(self):
        # response = requests.post(self.url, data=json.dumps(self.data))
        response = requests.post(self.url, json=self.data)
        print(f"响应体: {response.json()}")


if __name__ == '__main__':
    day1 = Day1()
    # day1.format_str()
    # day1.type_con()
    # day1.operator()
    # day1.play_game()
    # day1.print_mult_tables()
    day2 = Day2()
    # day2.str_concat()
    # day2.list_concat()
    # day2.tuple_concat()
    # day2.dict_concat()
    # day2.set_concat()
    # day2.ans_1()
    # day2.ans_2()
    # day2.ans_3()
    # day2.ans_4()
    # day2.ans_5()
    # day2.ans_6()
    # day2.ans_7()
    # day2.ans_8()
    # day2.ans_9()
    # day2.ans_10()
    day3 = Day3()
    # print(day3.return_values())
    # day3.fun_params("lll", 25)
    # day3.fun_params("lll", age=25, default="默认")
    # day3.fun_params("lll", 25, "默认", "a", "b", "c", key1="value", key2="value")
    # day3.fun_params("lll", 25, "默认", ("a", "b", "c"), {"key1": "value", "key2": "value"})
    # day3.fun_params("lll", 25, "默认", *("a", "b", "c"), **{"key1": "value", "key2": "value"})
    # day3.file_operator()
    # day3.os_model()
    day4 = Day4()
    # day4.ans_1()
    # day4.ans_2()
    # day4.ans_3()
    # day4.ans_4()
    # print(day4.ans_5(10))
    # day4.ans_6()
    r = RoastPotato()
    # print(r)
    # r.cooking(1)
    # print(r)
    # r.cooking(2)
    # r.add_sea("椒盐", "糖")
    # r.cooking(2)
    # print(r)
    print("请求".center(60, "="))
    # url = "https://www.kuaidi100.com/query"
    # params = {"type": "shunfeng", "postid": "SF1409812533370"}
    # get_req = ReqCont(url, params=params)
    # get_req.req_get()
    # print("*" * 60)
    url = "http://httpbin.org//post"
    data = {"username": "liangchao", "password": "123456"}
    post_res = ReqCont(url=url, data=data)
    post_res.post_frame()
    post_res.post_json()

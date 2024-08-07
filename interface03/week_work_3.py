# -*- coding: UTF-8 -*-
import json
import os
import random
import shutil

import requests


class Day2:
    def __init__(self):
        print("day02".center(60, "="))

    def str_concat(self):
        """字符串练习"""
        print("字符串切片".center(60, "-"))
        s = "1234qwertyasdfgvcxz"
        print(f"截取全部: {s[::]}")
        print(f"起始位置越界: ->{s[100::]}<-")
        print(f"结束位置越界: {s[:100:]}")
        print(f"逆序截取: {s[::-1]}")
        # print(f"获取某一元素，下标越界: {s[100]}")
        print(f"设置步长: {s[::2]}")
        print(f"设置步长为负值: {s[::-2]}")
        print("查找相关".center(60, "-"))
        s = "hello world and supertest and chenghao and Python"
        print(f"index(str, start, end): {s.index('and')}")
        print(f"index(str, start, end): {s.index('and', 20, 30)}")
        # print(f"index(str, start, end): {s.index('ands/=', 20, 30)}")
        print(f"find(str, start, end): {s.find('and')}")
        print(f"find(str, start, end): {s.find('and', 20, 30)}")
        print(f"find(str, start, end): {s.find('ands', 20, 30)}")
        print(f"count(), 统计次数: {s.count('and')}")
        print(f"count(), 统计次数: {s.count('ands')}")
        print("修改相关".center(60, "-"))
        print(f"段落首字母大写: {s.capitalize()}")
        print(f"全部字母转大写: {s.upper()}")
        print(f"全部字母转小写: {s.lower()}")
        print(f"分割: {s.split(' ')}")
        print(f"替换: {s.replace('and', '-->')}")
        print(f"字符串拼接: {'-'.join('a')}")
        print(f"字符串拼接: {'-'.join('abc')}")
        print(f"字符串拼接: {''.join('abc')}")
        print(f"移除两侧空白: {' af     '.strip()}")
        print(f"左对齐: {'fdsalf'.ljust(20, '-')}")
        print(f"居中: {'fdsalf'.center(20, '-')}")
        print(f"右对齐: {'fdsalf'.rjust(20, '-')}")
        print(f"字符串判断相关".center(60, "-"))
        print(f"结尾判断: {'abcd'.endswith('d')}")
        print(f"开头判断: {'abc'.startswith('a')}")
        print(f"是否全部都是字母: {'abcd'.isalpha()}")
        print(f"是否全部都是字母: {'abc1d'.isalpha()}")
        print(f"是否全部都是字母: {'abc_d'.isalpha()}")
        print(f"是否全部由字母或数字或字母数字组成: {'abc'.isalnum()}")
        print(f"是否全部由字母或数字或字母数字组成: {'abc1'.isalnum()}")
        print(f"是否全部由字母或数字或字母数字组成: {'123'.isalnum()}")
        print(f"是否全部由字母或数字或字母数字组成: {'ab_12'.isalnum()}")
        print(f"是否仅由数字组成: {'123'.isdigit()}")
        print(f"是否仅由数字组成: {'123_123'.isdigit()}")
        print(f"是否仅由数字组成: {'123abc'.isdigit()}")

    def list_concat(self):
        """列表练习"""
        print("查找相关".center(60, "-"))
        lis = [1, 2, 3, "a", "b", "c"]
        print(f"根据索引获取元素：{lis[1]}")
        print(f"index(ele, start, end): {lis.index(2)}")
        print(f"获取元素个数: {len(lis)}")
        print("修改相关".center(60, "-"))
        lis.append("abc")
        print(f"append(ele): {lis}")
        lis.extend("qaz")
        print(f"extend(item): {lis}")
        lis.insert(0, "==>")
        lis.insert(100, "-->")
        print(f"insert(ele, index): {lis}")
        lis.remove("-->")
        print(f"remove: {lis}")
        print(f"pop(): {lis.pop()}")
        print(f"pop(index): {lis.pop(0)} ===> {lis}")
        nums = [15, 2, 4, 9]
        print(f"原列表: {nums}\n排序后: {nums.sort()} ==> {nums}")
        print(f"不改变原列表: {sorted(nums, reverse=True)}")
        print(f"逆序前: {nums}\n逆序后: {nums.reverse()} ==> {nums}")
        print(f"不改变原列表: {list(reversed(nums))}")

    def tuple_concat(self):
        """元组练习"""
        print("元组系列方法".center(60, "-"))
        tuple1 = (1, 2, 3, "a", "b", [4, 5, 6])
        print(f"根据下标获取元素: {tuple1[0]}")
        print(f"index(ele, start, end): {tuple1.index(2)}")
        print(f"判断元素是否在元组中: {1 in tuple1}")
        print(f"修改前内存地址: {id(tuple1[-1])}")
        tuple1[-1][0] = 0
        print(f"修改了元组内的可变数据: {tuple1}")
        print(f"修改后内存地址: {id(tuple1[-1])}")

    def dict_concat(self):
        """字典练习"""
        dict1 = {"name": "ll", "age": 20, "sex": "男"}
        print(f"通过键取值: {dict1['name']}")
        print(f"通过键取值: {dict1.get('name')}")
        dict1["Country"] = "China"
        print(f"添加键值对: {dict1}")
        print(f"取出所有的键: {dict1.keys()}")
        print(f"取出所有的值: {dict1.values()}")
        print(f"取出所有的键值对: {dict1.items()}")
        dict1.update({"height": 170})
        print(f"合并字典: {dict1}")
        print(f"删除指定键值对: {dict1.pop('height')}")
        print(f"情况字典: {dict1.clear()}  ===> {dict}")

    def set_concat(self):
        """集合练习"""
        set1 = {1, 3, 4, 'a', 'b'}
        set1.add('1')
        print(f"add(ele): {set1}")
        print(f"移除指定元素: remove(ele): {set1.remove('1')}")
        print(f"移除指定元素,元素不存在则无动作: {set1.discard('1')}")
        print(f"随机移除一个元素，并返回: {set1.pop()}")
        new_set = {1, 2, 0, True, False}
        print(f"new set: {new_set}")
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        print(f"交集: {s1 & s2}")
        print(f"并集: {s1 | s2}")
        print(f"差集: {s1 - s2}")
        print(f"差集: {s2 - s1}")

    def ans1(self):
        """有三个教室，8名老师，随机给老师分配教师"""
        teachers = [i for i in range(1, 9)]
        rooms = [[], [], []]
        for ter in teachers:
            room = random.randint(0, 2)
            rooms[room].append(ter)
        for room in rooms:
            print(room)

    def ans2(self):
        """计算100以内能被3整除的数"""
        print(f"100以内能被3整除的数: {[i for i in range(1, 101) if i % 3 == 0]}")

    def ans3(self):
        """列表去重，不使用类型转化"""
        nums = [1, 2, 3, 4, 3, 4, 2, 5, 5, 8, 9, 7]
        res = []
        for ele in nums:
            if ele not in res:
                res.append(ele)
        print(res)

    def ans4(self, n):
        """斐波那契数列"""
        a, b = 1, 1
        for i in range(1, n):
            if i == 1 or i == 2:
                print(1, end=" ")
            else:
                a, b = b, a + b
                print(b, end=" ")

    def ans5(self):
        """计算100以内质数"""
        res = []
        for i in range(2, 101):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                res.append(i)
        print(f"100以内的质数: {res}")

    def ans6(self):
        """有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef 不使用类型转化"""
        s = "aabbbcddef"
        res = ""
        for ele in s:
            if s.count(ele) == 1:
                res += ele
        print(f"res: {res}")

    def ans7(self):
        """提取并打印superTest"""
        str1 = "welocme to super&Test"
        tmp_s = str1.split(" ")
        for ele in tmp_s:
            if "&" in ele:
                ele.replace("&", "")
                print(ele)

    def ans8(self):
        """有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ... #不允许用reverse,和reversed"""
        str1 = "abcdef"
        res = ""
        for s in str1:
            res = s + res
        print(res)

        res = ""
        tmp = list(str1)
        for _ in range(len(tmp)):
            res += tmp.pop()
        print(res)

    def ans9(self):
        """有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ... #不允许用reverse,和reversed"""
        str1 = "welocme to super&Test"
        tmp_list = list(str1)
        res = ""
        for _ in range(len(tmp_list)):
            res += tmp_list.pop()
        print(res)

    def ans10(self):
        """有一堆字符串，“aabbbcddef”，输出abcdef # 不允许用set"""
        str1 = "aabbbcddef"
        res = ""
        for e in str1:
            res = e + res
        print(res)


class Day3:
    def __init__(self):
        print("day03".center(60, "="))

    def return_values(self):
        """多个返回值"""
        return 1, 2

    def fun_params(self, name, age, default="default", *args, **kwargs):
        strs = f"""
name: {name};
age: {age};
default: {default};
args: {args}
kwargs: {kwargs}"""
        print(strs)

    def file_operator(self):
        """文件操作"""
        with open("./data.json", "r") as f:
            print(f"读取文件前10个字节：{f.read(10)}")
            print(f"查看当前指针位置：{f.tell()}")
            print(f"文件剩余内容：{f.read()}")
            print(f"将指针移动到开始：{f.seek(0, 0)}")
            print(f"查看当前指针位置：{f.tell()}")
            print(f"文件第一行内容：{f.readline()}")
            print(f"文件剩余内容：{f.readlines()}")
            print(f"将指针移动到5的位置：{f.seek(5, 0)}")
            print(f"将指针移动到文件末：{f.seek(0, 2)}")
            print(f"打印剩余内容: {f.read()}")

    def os_model(self):
        """os模块的一些方法"""
        print("os.mkdir(d): 创建一个文件夹")
        # os.mkdir("tmp")
        print("os.remove(d): 移除空文件夹")
        # os.remove("tmp")
        print("os.makedirs(t/t1/t2): 创建多层目录")
        # os.makedirs("tmp/t1/t2")
        print("shutil.rmtree(d): 删除非空文件夹")
        # shutil.rmtree("tmp")
        print("os.rename(old, new): 文件重命名")
        print(f"获取当前目录: {os.getcwd()}")
        print(f"切换目录: {os.chdir('..')}")
        print(f"获取父级目录: {os.path.dirname(os.getcwd())}")
        print(f"列举当前目录: {os.listdir()}")


class Day4:
    def __init__(self):
        print("day04".center(60, "="))

    def ans1(self):
        """列表去重"""
        l = [1, 1, 1, 2, 2, 3, 3, 9]
        res = []
        for e in l:
            if e not in res:
                res.append(e)
        print(res)

    def ans2(self):
        """筛选出大于18岁的人"""
        info = "lucy:21,tom:30,xiaoming:18,xiaohong:15,xiaowang:20,xiaohei:19"
        tmp_list = info.split(",")
        for user in tmp_list:
            tmp = user.split(":")
            if int(tmp[1]) > 18:
                print(f"name: {tmp[0]}, age: {tmp[1]}")

    def ans3(self):
        """1-100之间能被2整除的数"""
        print(f"1-100之间能被2整除的数: {[i for i in range(1, 101) if i % 2 == 0]}")

    def ans4(self):
        """将字符串中的每个单词反转"""
        strs = "welocme to super&Test"
        tmp_strs = strs.split(" ")
        res = ""

        def str_rev(s: str) -> str:
            t = ""
            for e in s:
                t = e + t
            return t

        for s in tmp_strs:
            res += f"{str_rev(s)} "
        print(res.strip())

    def ans5(self, n: int):
        """递归实现斐波那契数列"""
        if n == 1 or n == 2:
            return 1
        return self.ans5(n - 1) + self.ans5(n - 2)

    def ans6(self):
        """将列表中的元素转换为int"""
        l = ["1", "2", "3"]
        print(f"int: {[int(i) for i in l]}")


class RoastPotato:
    """烤地瓜"""

    def __init__(self):
        print("烤地瓜".center(60, "-"))
        self.cook_time = 0
        self.status = "生的"
        self.seasoning = []

    def cooking(self, t: float):
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
        return f"烘培时间: {self.cook_time}分钟; 地瓜状态: {self.status}; 添加了: {self.seasoning} 调料"


class ReqCont:
    """requests 模块练习"""

    def __init__(self, url, data=None, params=None):
        self.url = url
        self.data = data
        self.params = params

    def req_get(self):
        """get请求"""
        # get 请求中，params接收的参数会被拼接到url中
        response = requests.get(url=self.url, params=self.params)

        print(f"响应对象: {response}")
        print(f"响应体: {response.text}")
        print(f"状态码: {response.status_code}")
        print(f"json格式响应: {response.json()}")  # 如果返回的不是json格式会报错
        print(f"字节格式响应: {response.content}")
        print("-" * 60)
        print(f"请求头: {response.request.headers}")
        print(f"请求体(get请求没有该项): {response.request.body}")
        print(f"请求地址: {response.url}")

    def post_form(self):
        """form表单"""
        # data接收的参数会被传递到请求体中
        response = requests.post(url=self.url, data=self.data)
        print(f"响应体: {response.text}")
        print(f"请求体: {response.request.body}")

    def post_json(self):
        """json格式数据"""
        # response = requests.post(url=self.url, data=json.dumps(self.data))
        response = requests.post(url=self.url, json=self.data)
        print(f"响应体: {response.json()}")
        print(f"请求体: {response.request.body}")

    def use_default_cookie(self):
        response = requests.post(url=self.url, data=self.data)
        cookies = response.cookies

        info = "https://wanandroid.com//user/lg/userinfo/json"
        res = requests.get(url=info, cookies=cookies)  # 将cookies作为参数传递下去
        print(f"info: {res.text}")

    def use_custom_cookie(self):
        """使用自定义的cookie
        无论鉴权字段在响应体中还是请求头中，都可以手动的将其取出，并向下传递，灵活性更高
        """
        response = requests.post(url=self.url, data=self.data)
        print(response.text)

        headers = {"Cookie": response.headers["Set-Cookie"]}
        info = "https://wanandroid.com//user/lg/userinfo/json"
        res = requests.get(url=info, headers=headers)
        print(f"info: {res.text}")

    def use_session_obj(self):
        """使用session对象传递cookie
        使用于鉴权字段在响应头中的情况，session对象会自动给获取cookie并将其传递下去
        但是不适用于鉴权字段不在响应体中的情况
        """
        s = requests.session()
        response = s.post(url=self.url, data=self.data)
        print(response.text)

        res = s.get("https://wanandroid.com//user/lg/userinfo/json")
        print(res.text)


if __name__ == '__main__':
    d2 = Day2()
    # d2.str_concat()
    # d2.list_concat()
    # d2.tuple_concat()
    # d2.dict_concat()
    # d2.set_concat()
    # d2.ans1()
    # d2.ans2()
    # d2.ans3()
    # d2.ans4(10)
    # d2.ans5()
    # d2.ans6()
    # d2.ans8()
    # d2.ans9()
    # d2.ans10()
    d3 = Day3()
    # print(d3.return_values())
    # d3.fun_params("ll", 12)
    # d3.fun_params("ll", age=12)
    # d3.fun_params("ll", 12, "NNNN", 1, 2, 3, key1="000", key2="111")
    # d3.fun_params("lll", 25, "默认", *("a", "b", "c"), **{"key1": "value", "key2": "value"})
    # d3.file_operator()
    # d3.os_model()
    d4 = Day4()
    # d4.ans1()
    # d4.ans2()
    # d4.ans3()
    # d4.ans4()
    # print(d4.ans5(10))
    # d4.ans6()
    # roa = RoastPotato()
    # roa.cooking(2)
    # print(roa.status)
    # roa.cooking(2)
    # roa.cooking(1)
    # roa.add_sea("12", "ab")
    # print(roa)
    get_url = "https://www.kuaidi100.com/query"
    post_url = "http://httpbin.org//post"
    params = {"type": "shunfeng", "postid": "SF1409812533370"}
    data = {"username": "liangchao", "password": "123456"}
    req = ReqCont(get_url, params=params, data=data)

    # req.req_get()
    # req.url = post_url
    # req.post_form()
    # req.post_json()
    req.url = "https://wanandroid.com/user/login"
    req.data = {"username": "ymw001", "password": "123456"}
    # req.use_default_cookie()
    # req.use_custom_cookie()
    req.use_session_obj()

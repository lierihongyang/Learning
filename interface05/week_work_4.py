# -*- coding: UTF-8 -*-
import random

import requests


class Day2:
    def __init__(self):
        print("day03".center(60, "+"))

    def str_concat(self):
        """字符串练习"""
        s = "123abcdef"
        print(f"截取全部: {s[::]}")
        print(f"起始位置越界: {s[100:]}")
        print(f"结束位置越界: {s[:100]}")
        print(f"逆序截取: {s[::-1]}")
        # print(f"下标越界: {s[100]}")
        print(f"设置步长: {s[::2]}")
        print(f"设置步长为负: {s[::-3]}")
        s = "hello world and supertest and chenghao and Python"
        print(f"index: {s.index('and')}")
        # print(f"index: {s.index('ands')}")
        print(f"find: {s.find('and')}")
        print(f"find: {s.find('ands')}")
        print(f"count: {s.count('and')}")
        print(f"count: {s.count('ands')}")
        print(f"段落首字母大写: {s.capitalize()}")
        print(f"所有字母转大写: {s.upper()}")
        print(f"所有字母转小写: {s.lower()}")
        print(f"分割: {s.split(' ')}")
        print(f"替换: {s.replace('and', '-->')}")
        print(f"字符串拼接: {'_'.join('123')}")
        print(f"字符串拼接: {'_'.join('1')}")
        print(f"移除两侧空白: {'  131 '.strip()}")
        print(f"左对齐: {'abc'.ljust(20, '-')}")
        print(f"居中: {'abc'.center(20, '-')}")
        print(f"右对齐: {'abc'.rjust(20, '-')}")
        print(f"结尾判断: {'abc'.endswith('c')}")
        print(f"开头判断: {'abc'.startswith('a')}")
        print(f"是否全部由字母或数字或字母数字组成: {'abc'.isalnum()}")
        print(f"是否全部由字母或数字或字母数字组成: {'123'.isalnum()}")
        print(f"是否全部由字母或数字或字母数字组成: {'12ab'.isalnum()}")
        print(f"是否全部由字母或数字或字母数字组成: {'12_a'.isalnum()}")
        print(f"是否全部由字母或数字或字母数字组成: {'_'.isalnum()}")
        print(f"是否全部由字母组成: {'abc'.isalpha()}")
        print(f"是否全部由字母组成: {'12'.isalpha()}")
        print(f"是否全部由字母组成: {'ab_'.isalpha()}")
        print(f"是否全部由数字组成: {'123'.isdigit()}")
        print(f"是否全部由数字组成: {'123_'.isdigit()}")
        print(f"是否全部由数字组成: {'123a'.isdigit()}")

    def list_concat(self):
        """列表练习"""
        lis = [1, 2, 3, 'a', 'b', 'c']
        print(f"通过索引获取元素: {lis[2]}")
        # print(f"index: {lis.index('2')}")
        print(f"index: {lis.index(2)}")
        print(f"获取元素个数: {len(lis)}")
        lis.append('abc')
        print(f"append: {lis}")
        lis.extend('000')
        print(f"extend: {lis}")
        lis.insert(10, '9')
        lis.insert(100, 'qqq')
        print(f"insert: {lis}")
        lis.remove('0')
        print(f"remove: {lis}")
        print(f"pop: {lis.pop(0)} ==> {lis}")
        nums = [1, 4, 6, 3, 0]
        print(f"原列表: {nums}\n排序后: {nums.sort()} ==> {nums}")
        print(f"不改变原列表: {sorted(nums, reverse=True)}")
        print(f"逆序前: {nums}\n逆序后: {nums.reverse()} ==> {nums}")
        print(f"不改变原列表: {list(reversed(nums))}")

    def tuple_concat(self):
        tuple1 = (1, 2, 3, 4, 'a', 'b', [6, 7, 8])
        print(f"根据下标获取元素: {tuple1[-1]}")
        print(f"index: {tuple1.index(3)}")
        print(f"修改前内存地址: {id(tuple1[-1])}")
        tuple1[-1][0] = 0
        print(f"修改前内存地址: {id(tuple1[-1])}")

    def dict_concat(self):
        """字典练习"""
        dict1 = {"name": "a", "age": 1}
        print(f"通过键取值: {dict1['age']}")
        print(f"通过键取值: {dict1.get('age')}")
        dict1['country'] = 'cccc'
        print(f"添加键值对: {dict1}")
        print(f"取出所有的键: {dict1.keys()}")
        print(f"所有的值: {dict1.values()}")
        print(f"所有的键值对: {dict1.items()}")
        print(f"name是否在字典中: {'name' in dict1}")
        dict1.update({'aaa': "aaa"})
        print(f"update合并字典: {dict1}")
        print(f"删除键值对: {dict1.pop('aaa')}")
        print(f"清空字典: {dict1.clear()} ==> {dict1}")

    def set_count(self):
        """集合"""
        set1 = {1, 3, 5, 'a', 'b'}
        set1.add(4)
        print(f"add: {set1}")
        print(f"移除指定元素: {set1.remove(4)}")
        print(f"随机移除一个元素: {set1.pop()}")
        s = {1, 0, 2, True, False}
        print(f"s: {s}")
        s1 = {1, 2, 3, 4}
        s2 = {3, 4, 5, 6}
        print(f"交集: {s1 & s2}")
        print(f"并集: {s1 | s2}")
        print(f"差集: {s1 - s2}")
        print(f"差集: {s2 - s1}")
        print(f"差集: {s2 - s2}")

    def ans1(self):
        teas = [1, 2, 3, 4, 5, 6, 7, 8]
        rooms = [[], [], []]
        for t in teas:
            room = random.randint(0, 2)
            rooms[room].append(t)
        for room in rooms:
            print(room)

    def ans2(self):
        print(f"100以内能被3整除的数: {[i for i in range(1, 101) if i % 3 == 0]}")

    def ans3(self):
        nums = [1, 2, 3, 4, 3, 4, 2, 5, 5, 8, 9, 7]
        res = []
        for ele in nums:
            if ele not in res:
                res.append(ele)
        print(res)

    def ans4(self, n):
        a, b = 1, 1
        for i in range(n):
            if i == 1 or i == 2:
                print(1, end=" ")
            else:
                a, b = b, a + b
                print(b, end=" ")

    def ans5(self, n):
        if n == 1 or n == 2:
            return 1
        return self.ans5(n - 1) + self.ans5(n - 2)

    def ans6(self):
        res = []
        for i in range(2, 101):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                res.append(i)
        print(res)

    def ans7(self):
        s = "aabbbcddef"
        res = ''
        for e in s:
            if s.count(e) == 1:
                res += e
        print(res)

    def ans8(self):
        str1 = "welocme to super&Test"
        tmp = str1.split(' ')
        for e in tmp:
            if '&' in e:
                e.replace('&', "")
                print(e)

    def ans9(self):
        """有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ... #不允许用reverse,和reversed"""
        str1 = "welocme to super&Test"
        tmp = list(str1)
        res = ""
        for _ in range(len(tmp)):
            res += tmp.pop()
        print(res)


class Day3:
    def __init__(self):
        print("day03".center(60, "="))

    def fun_params(self, name, age, default="default", *args, **kwargs):
        s = f"""
name: {name};
age: {age};
default: {default};
args: {args}
kwargs: {kwargs}"""
        print(s)

    def file_operator(self):
        with open("../.gitignore", "r") as f:
            print(f"读取前10个字节: {f.read(10)}")
            print(f"查看当前指针位置: {f.tell()}")
            print(f"查看剩余内容: {f.read()}")
            print(f"移动指针到开头: {f.seek(0, 0)}")
            print(f"第一行内容: {f.readline()}")
            print(f"剩余内容: {f.readlines()}")
            print(f"移动指针到5的位置: {f.seek(5, 0)}")
            print(f"移动指针到末尾: {f.seek(0, 2)}")


class Day4:
    def __init__(self):
        print("day04".center(60, "="))

    def ans1(self):
        info = "lucy:21,tom:30,xiaoming:18,xiaohong:15,xiaowang:20,xiaohei:19"
        tmp = info.split(',')
        for u in tmp:
            t = u.split(":")
            if int(t[1]) > 18:
                print(f"name: {t[0]}, age{t[1]}")

    def ans2(self):
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


class ReqCont:
    def __init__(self, url, data=None, params=None):
        self.url = url
        self.data = data
        self.params = params

    def req_get(self):
        response = requests.get(url=self.url, params=self.params)
        print(f"响应体: {response.text}")
        print(f"响应体-json: {response.json()}")
        print(f"响应体-字节格式: {response.content}")
        print(f"请求头: {response.request.headers}")
        print(f"请求地址: {response.url}")

    def post_form(self):
        response = requests.post(url=self.url, data=self.data)
        print(f"请求体: {response.request.body}")
        print(f"请求体: {response.text}")

    def post_json(self):
        response = requests.post(url=self.url, json=self.data)
        print(f"请求体: {response.request.body}")
        print(f"请求体: {response.text}")

    def use_default_cookie(self):
        response = requests.post(url=self.url, data=self.data)
        cookies = response.cookies

        info = "https://wanandroid.com//user/lg/userinfo/json"
        res = requests.get(url=info, cookies=cookies)
        print(f"info: {res.text}")

    def use_custom_cookie(self):
        response = requests.post(url=self.url, data=self.data)
        print(response.text)

        headers = {"Cookie": response.headers["Set-Cookie"]}  # 从响应头中获取cookies
        info = "https://wanandroid.com//user/lg/userinfo/json"
        res = requests.get(url=info, headers=headers)
        print(f"info: {res.text}")

    def use_session_obj(self):
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
    d2.set_count()

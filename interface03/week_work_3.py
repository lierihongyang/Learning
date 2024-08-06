# -*- coding: UTF-8 -*-
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


if __name__ == '__main__':
    d2 = Day2()
    # d2.str_concat()
    # d2.list_concat()
    # d2.tuple_concat()
    # d2.dict_concat()
    d2.set_concat()

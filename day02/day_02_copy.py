# -*-coding:utf-8 -*-

"""
# File       : day_02_copy.py
# Time       ：2024/7/19 上午9:33
# Author     ：LiChunBo
"""


def str_concat():
    """字符串练习"""
    print("字符串切片".center(60, '-'))
    s = "123456abcdef"
    print(f"截取全部字符串：{s[::]}")
    print(f"开始位置超出索引：{s[100::]}...")
    print(f"结束位置超出索引：{s[:100]}")
    print(f"逆序截取：{s[::-1]}")
    # print(f"下标越界：{s[100]}")
    print(f"设置步长为2：{s[::2]}")
    print(f"步长为负：{s[3::-1]}")
    print("字符串中用于查找的方法".center(60, '-'))
    mystr = "hello world and supertest and chenghao and Python"
    print(f"find(str, start, end): {mystr.find('and', 20, 50)}")
    print(f"find(str): {mystr.find('and')}")
    print(f"find: 字串不存在{mystr.find('ands')}")
    print(f"index(str, start, end): {mystr.index('and', 20, 50)}")
    print(f"index(str): {mystr.index('and')}")
    # print(f"index, 字串不存在：{mystr.index('ands')}")
    print(f"count(str, start, end): {mystr.count('and')}")
    print(f"count(str): {mystr.count('and')}")
    print(f"count, 字串不存在：{mystr.count('ands')}")
    print(f"rfind: {mystr.rfind('and')}")
    print(f"rindex: {mystr.rindex('and')}")
    print("字符串修改系列方法".center(60, '-'))
    print(f"首字母大写，其余字母小写：{mystr.capitalize()}")
    print(f"所有字母大写：{mystr.upper()}")
    print(f"所有字母小写：{mystr.lower()}")
    print(f"replace(old, new, count): {mystr.replace(' ', '-->', 2)}")
    print(f"replace(old, new): {mystr.replace(' ', '-->')}")
    print(f"split 分割：{mystr.split(' ')}")
    print(f"join() 字符串拼接：{'-'.join('ab')}")
    print(f"join() 字符串拼接：{'-'.join('a')}")
    print(f"移除两端空白：{'   string '.strip()}")
    print(f"移除两端指定字符：{'a string b'.strip(' a b')}")
    print(f"字符串居中：{'abcdef'.center(20, '-')}")
    print(f"字符串右对齐：{'abcdef'.rjust(20, '-')}")
    print(f"字符串左对齐：{'abcdef'.ljust(20, '-')}")
    print("字符串判断系列方法".center(60, '-'))
    print(f"字符串开头判断：{mystr.startswith('hello')}")
    print(f"字符串开头判断，指定区间：{mystr.startswith('hello', 20, 50)}")
    print(f"字符串结尾判断：{mystr.endswith('thon')}")
    print(f"字符串结尾判断，指定区间：{mystr.endswith('and', 20, 50)}")
    print(f"字符串是否全部由字母组成'abc': {'abc'.isalpha()}")
    print(f"字符串是否全部由数字组成'abc123': {'abc123'.isdigit()}")
    print(f"字符串是否全部由数字组成'123': {'123'.isdigit()}")
    print(f"字符串是否由数字和字母组成'123abc': {'123abc'.isalnum()}")


def list_concat():
    """列表的练习"""
    name_list = ["Tom", "Lily", "Jack", "Rose"]
    print("列表查找相关的方法".center(60, '-'))
    print(f"根据索引取元素：{name_list[1]}")
    print(f"index(ele, start, end),获取对应的下标：{name_list.index('Tom', 0, 3)}")
    # print(f"index(ele, start, end),元素不存在：{name_list.index('Tom1', 0, 3)}")
    print(f"获取元素个数：{len(name_list)}")
    print("列表元素修改相关方法".center(60, '-'))
    name_list.append('LiMing')
    print(f"追加元素，append: {name_list}")
    name_list.extend('abc')
    print(f"列表扩展extend: {name_list}")
    print(f"列表扩展`+`：{name_list + [9, 0, 6]}")
    name_list.insert(0, '->')
    print(f"在指定位置插入元素insert(index, ele)：{name_list}")
    print("列表元素修改系列方法".center(60, '-'))
    name_list[0] = '======>'
    print(f"第一个元素修改后：{name_list}")
    print(f"移除指定索引的元素，pop(0): {name_list.pop(0)}")
    print(f"默认移除最后一个元素，pop(): {name_list.pop()}")
    # print(f"下标越界，pop(100): {name_list.pop(100)}")
    print(f"元素移除后的列表：{name_list}")
    name_list.remove('Tom')
    print(f"移除指定元素, remove(ele): {name_list}")
    print(f"情况列表：{name_list.clear()} ===> 列表清空后：{name_list}")
    del name_list
    print("列表排序".center(60, '-'))
    nums = [1, 4, 3, 6, 8]
    print(f'原列表：{nums}\n排序后：{nums.sort()} ==> {nums}')
    print(f"不改变原列表：{sorted(nums, reverse=True)}")
    print(f"源列表：{nums}, {nums.reverse()} 列表逆序后：{nums}")
    print(f"不改变源列表，逆序：{list(reversed(nums))}")


def tuple_concat():
    """元组练习"""
    print("元组查找系列方法".center(60, '-'))
    tuple1 = (1, 2, 3, 'a', 'b', [4, 5, 6])
    print(f"根据下标获取元素：{tuple1[0]}")
    print(f"index, 获取指定元素下标，元素不存在会报错：{tuple1.index('a')}")
    print(f"获取元素个数：{len(tuple1)}")
    print(f"判断元素'1'是否在元组中：{'1' in tuple1}")
    print(f"修改前可变元素的内存地址：{id(tuple1[-1])}")
    tuple1[-1][0] = 0
    print(f"修改元组中可变元素的值（不建议）：{tuple1}")
    print(f"修改后可变元素的内存地址：{id(tuple1[-1])}")


def dict_concat():
    """字典练习"""
    dict1 = {"name": "Tom", "age": 20, "sex": "男"}
    print(f"字典查询、修改操作".center(60, '-'))
    print(f"根据键获取值，键不存在时，会报错：{dict1['name']}")
    print(f"根据键获取值，键不存在时，返回默认值：{dict1.get('ages', 0)}")
    dict1["Country"] = "China"
    print(f"添加键值对：{dict1}")
    print(f"获取所有键值对：{dict1.items()}")
    print(f"获取所有的键：{dict1.keys()}")
    print(f"获取所有的值：{dict1.values()}")
    dict1.update({"height": 170})
    print(f"合并两个字典，update: {dict1}")
    print(f"根据键删除元素，pop(key): {dict1.pop('height')}")
    print(f"情况字典：{dict1.clear()} ==> {dict1}")


def set_concat():
    """集合练习"""
    print("集合相关方法".center(60, '-'))
    set1 = {1, 2, 3, 'a', 'b', 'c'}
    set1.add('123')
    print(f"添加元素，add(ele): {set1}")
    print(f"合并两个集合：{set1.update({'ele1', 'ele2'})} ==> {set1}")
    print(f"移除指定元素，remove(ele)元素不存在报错: {set1.remove('ele1')} ==> {set1}")
    print(f"移除指定元素，元素不存在则无动作，discard(ele):{set1.discard('ele')}")
    print(f'随机移除一个元素，并获取返回值，pop(ele): {set1.pop()}')
    new_set = {True, False, 0, 1, 2, 3}  # 0与False、1与True会触发去重效果
    print(f"new set: {new_set}")
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}
    print(f"两个集合取交集：{s1 & s2}")
    print(f"两个集合取并集：{s1 | s2}")
    print(f"两个集合取差集：{s1 - s2}")


def pub_concat():
    """公共操作"""
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    print(f"`+`: {l1 + l2}")
    print(f"`*`: {l1 * 3}")
    d = {1: 2, 3: 4}
    print(f"判断1是否在字典中：{1 in d}")
    print(f"取最大值：{max(l1)}")
    print(f"取最小值：{min(l2)}")

    print(f"列表推导式：{[i for i in range(10)]}")
    # 获取列表各元素及下标
    for i, e in enumerate(['a', 'b', 'c']):
        print(f"index: {i}, value: {e}")
    print("-"*50)

    # 取出所有字母`o`的下标
    s = 'afdjasofasfoafdaoooadfafoafasdfo'
    for i, e in enumerate(s):
        if e == 'o':
            print(f"index: {i}, value: {e}")


def genex_concat():
    """生成式练习"""
    print("生成式练习".center(60, '-'))
    nums = [i for i in range(0, 10, 2)]
    print(f"一个偶数列表：{nums}")
    """
        [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2),
    """
    demo = [(i, j) for i in range(1, 3) for j in range(3)]
    print(demo)
    l = []
    for i in range(1, 3):
        for j in range(3):
            l.append((i, j))
    print(l)
    print("字典推导式".center(60, '-'))
    l1 = [1, 2, 3]
    l2 = ['a', 'b', 'c']
    d1 = {l1[i]: l2[i] for i in range(len(l1))}
    print(f"字典推导式：{d1}")
    """
        取出数量大于200的机型
    """
    counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
    for k, v in counts.items():
        if v > 200:
            print(f"机型：{k}, 数量：{v}")
    d2 = {k: v for k, v in counts.items() if v > 200}
    print(f"数量大于200的机型：{d2}")
    print("集合推导式".center(60, '-'))
    """
    创建一个集合，元素分别为下述列表个元素的平方
    """
    nums  = [2, 4, 6]
    set1 = {ele**2 for ele in nums}
    print(f"set: {set1}")


if __name__ == '__main__':
    # str_concat()
    # list_concat()
    # tuple_concat()
    # dict_concat()
    # set_concat()
    # pub_concat()
    genex_concat()
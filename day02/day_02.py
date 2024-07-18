# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：day_02.py
@Author  ：LiChunBo
@Date    ：2024/7/18 上午10:30
"""


def str_slice():
    """字符串切片"""
    s = "123456abcdef"
    print(f"截取全部：{s[::]}")
    print(f"开始位置超出索引：{s[100::]}")
    print(f"结束位置超出索引：{s[1:100]}")
    print(f"逆序截取：{s[::-1]}")
    print(f"步长为2：{s[::2]}")
    # print(f"索引超出：{s[100]}")
    print(f"逆序截取：{s[-3:-1]}")
    print(f"步长为负：{s[3::-1]}")


def str_find():
    """字符串中用于查找的方法"""
    mystr = "hello world and supertest and chenghao and Python"
    print(f"find: {mystr.find('and')}")
    print(f"find(字串, 开始, 结束): {mystr.find('and', 25, 50)}")
    print(f"find, 未找到子串: {mystr.find('ands', )}")

    print(f"index: {mystr.index('and')}")
    print(f"index(字串, 开始, 结束): {mystr.index('and', 25, 50)}")
    # print(f"index, 未找到字串: {mystr.index('ands')}")

    print(f"count: {mystr.count('and')}")
    print(f"count(字串, 开始, 结束): {mystr.count('and', 25, 50)}")
    print(f"count, 字串未找到: {mystr.count('ands')}")

    print(f"rfind: {mystr.rfind('and')}")
    print(f"rindex: {mystr.rindex('and')}")


def str_modify():
    """字符串修改"""
    mystr = "hello world and supertest and chenghao and Python"
    print(f"首字母大写，其余字母小写：{mystr.capitalize()}")
    print(f"所有字母大写：{mystr.upper()}")
    print(f"所有单词首字母大写：{mystr.title()}")
    print(f"所有单词首字母小写：{mystr.lower()}")
    print(f"replace 替换：{mystr.replace(' ', '-->')}")
    print(f"replace 替换，指定替换次数：{mystr.replace(' ', '-->', 2)}")
    print(f"split 分割：{mystr.split(' ')}")
    print(f"字符串拼接：join: {'123'.join('abc')}")
    print(f"字符串拼接：{'b'.join('ac')}")
    print(f"字符串去除两侧空白: {'  abc  '.strip()}")
    print(f"字符串去除左侧空白: {'  abc  '.lstrip()}")
    print(f"字符串去除右侧空白: {'  abc  '.rstrip()}")
    print(f"字符串去除两侧指定字符: {'2  abc  1'.strip(' 1 2')}")  # 这里' 1 2'使用空格隔开，不分先后
    print(f"居中：{'abcdef'.center(20, '=')}")
    print(f"右对齐：{'abcdef'.rjust(20, '=')}")
    print(f"左对齐：{'abcdef'.ljust(20, '=')}")


def str_judge():
    """字符串判断"""
    mystr = "hello world and supertest and chenghao and Python"
    print(f"字符串开头判断：{mystr.startswith('hello')}")
    print(f"字符串开头判断, 指定区间：{mystr.startswith('hello', 20, 50)}")
    print(f"字符串结尾判断：{mystr.endswith('thon')}")
    print(f"字符串结尾判断, 指定区间：{mystr.endswith('thon', 20, 50)}")
    print(f"字符串是否全都是字母'abc'：{'abc'.isalpha()}")
    print(f"字符串是否全都是数字'123abc'：{'123abc'.isdigit()}")
    print(f"字符串是否由数字和字母组成'123abc：{'123abc'.isalnum()}")


def list_concat():
    """列表的联系"""
    name_list = ["Tom", "Lily", "Jack", "Rose"]
    print("列表查找相关的方法".center(50, '='))
    print(f"取出索引对应的元素：name_list[1] {name_list[1]}")
    print(f"index(元素, 开始, 结束) 查找原素，返回对应的下标{name_list.index('Tom', 0, 3)}:")
    # print(f"index(元素, 开始, 结束) 查找原素，返回对应的下标{name_list.index('Tom1', 0, 3)}:")
    print(f"列表元素个数：{len(name_list)}")
    print("列表修改列表相关的方法".center(50, '='))
    name_list.append('123')
    print(f"追加元素，append, {name_list}")
    name_list.append(['a', 'b', 'c'])
    print(f"追加元素，append, {name_list}")
    name_list.extend('abcd')
    print(f"列表扩展，extend，{name_list}")
    new_list = name_list + [123, 456]
    print(f"列表扩展，`+` {new_list}")
    name_list.insert(2, '11111111111')
    print(f"在指定位置插入新元素：insert(下标, 元素) {name_list}")
    print("列表元素修改相关的方法".center(50, '='))
    name_list[0] = '汤姆'
    print(f"根据下标修改元素：列表[下标]=新值。{name_list}")
    print(f"根据下标删除元素，pop()默认值：{name_list.pop()}")
    print(f"根据下标删除元素，pop(0)指定索引：{name_list.pop(0)}")
    print(f"移除元素后：{name_list}")
    name_list.remove('Lily')
    print(f"移除指定元素，remove(元素): {name_list}")
    print(f"情况列表clear()：{name_list.clear()}")
    del name_list
    print("列表排序".center(50, '='))
    nums = [1, 2, 4, 8, 6, 0, 7]
    print(f"原列表：{nums}")
    nums.reverse()
    print(f"列表逆序：reverse后：{nums}")
    print(f"不修改原列表 reversed：{list(reversed(nums))}")
    nums.sort()
    print(f"直接对原列表进行修改：sort() {nums}")
    print(f"不修改原列表：sorted() {sorted(nums, reverse=True)}")


def tuple_concat():
    """元组练习"""
    print("元素查找相关".center(50, '='))
    tuple1 = ("a", "b", "c", 1, 2, 3, [4, 5, 6])
    print(f"根据下标获取元素：tuple1[1]: {tuple1[1]}")
    print(f"index，获取指定元素下标，元素不存在报错：{tuple1.index('a')}")
    print(f"获取元素个数：{len(tuple1)}")
    print(f"判断元素是否在元组中：{1 in tuple1}")
    print(f"原元组：{tuple1}")
    print(f"修改前可变元素内存地址：{id(tuple1[6])}")
    tuple1[6][0] = '四'
    print(f"修改元组内的可变元素（不建议）：{tuple1}")
    print(f"修改后可变元素内存地址：{id(tuple1[6])}")


def dict_concat():
    """字典练习"""
    dict1 = {"name": "Tom", "age": 20, "sex": "男"}
    print("字典查询、修改操作".center(50, '='))
    print(f"根据键获取值，键不存在时，报错：{dict1['name']}")
    print(f"根据键获取值，键不存在时，返回默认值：{dict1.get('ages', 0)}")
    dict1["Country"] = "China"
    print(f"添加键值对：{dict1}")
    print(f"所有的键：{dict1.keys()}")
    print(f"所有的值：{dict1.values()}")
    print(f"所有的键值对：{dict1.items()}")
    dict1.update({"height": 170})
    print(f"字典更新(将两个字典合并)：{dict1}")
    # print(f"清空字典：{dict1.clear()}")
    print(f"根据key删除元素：dict1.pop('height') {dict1.pop('height')}")
    print(dict.fromkeys(dict1))


def set_concat():
    """集合练习"""
    print("集合".center(50, '='))
    set1 = {1, 2, 3, 'a', 'b', 'c', 'e'}
    set1.add('123')
    print(f"新增元素：add(ele) {set1}")
    print(f"合并两个集合：update(item)")
    set1.update({'new set', 'new ele'})
    print(f"{set1}")
    set1.remove('a')
    print(f"移除指定元素：remove(ele) {set1}")
    # set1.remove('a')  # "移除指定元素，元素不存在会报
    set1.discard('a')
    print(f"移除指定元素，元素不存在就无动作：discard('a')  {set1}")
    print(f"随机移除一个元素，并获取被移除的元素{set1.pop()}")
    new_set = {0, 1, 2, 3, True, False}     # 0 和 False、1和True会触发去重
    print(f"new set: {new_set}")
    d1 = {1, 2, 3, 4}
    d2 = {3, 4, 5, 6}
    print(f"两个集合取交集：{d1 & d2}")
    print(f"两个集合取并集：{d1 | d2}")
    print(f"两个集合取差集：{d1 - d2}")


def pub_operator():
    """公共操作"""
    print("公共操作".center(50, '='))
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    print(f"+：{l1 + l2}")
    print(f"*: {l1 * 3}")
    d = {1: 2, 3: 4}
    print(f"1 in d: {1 in d}")
    print(f"max：{max(l1)}")
    print(f"min: {min(l2)}")
    nums = range(1, 10, 2)

    li = ['a', 'b', 'c', 'd']
    for i,e in enumerate(li):
        print(f"index: {i}, value: {e}")
    print()

    s = "kfdjasldpofaoafaoafdfaewofdao"
    for i, e in enumerate(s):
        if e == 'o':
            print(f"index: {i}, value: {e}")


def genex_concat():
    """生成式练习"""
    print(f"生成式练习".center(50, '='))
    nums = [i for i in range(0, 10, 2)]
    print(f"偶数列表：{nums}")
    """
    [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2),
    """
    ll = [(i, j) for i in range(1, 3) for j in range(3)]
    print(ll)
    l = []
    for i in range(1, 3):
        for j in range(3):
            l.append((i, j))
    print(l)
    print("字典推导式练习".center(50, '='))
    l1 = ['a', 'b', 'c']
    l2 = [1, 2, 3]
    d1 = {l1[i]: l2[i] for i in range(len(l1))}
    print(f"字典d1 {d1}")
    """
    取出数量大于200的机型
    """
    counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
    for k, v in counts.items():
        if v > 200:
            print(f"机型：{k}, 数量：{v}")
    d2 = {k: v for k, v in counts.items() if v > 200}
    print(f"数量大于200的机型：{d2}")
    print("集合推导式练习".center(50, '='))
    """
    创建一个集合，元素分别为下述列表各元素的平方
    """
    nums = [1, 3, 5]
    set1 = {ele ** 2 for ele in nums}
    print(f"set：{set1}")


if __name__ == '__main__':
    # slice()
    # str_find()
    # str_modify()
    # str_judge()
    # list_concat()
    # tuple_concat()
    # dict_concat()
    # set_concat()
    # pub_operator()
    genex_concat()

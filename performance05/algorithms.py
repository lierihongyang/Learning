# -*- coding: UTF-8 -*-
"""算法"""


def mao_pao():
    """冒泡排序"""
    arr = [3, 6, 1, 7, 4, 2]
    length = len(arr)
    for i in range(length):
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


def select_sort():
    """选择排序"""
    arr = [7, 4, 2, 1, 3, 9]
    length = len(arr)
    for i in range(length - 1):
        min_index = i  # 记录最小值的索引
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:  # 条件成立，说明最小值的索引是j
                min_index = j  # 修改最小值索引
        if i != min_index:  # 当i不是最小值索引时，将值进行替换
            arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)


def binary_search(num: int):
    """二分查找"""
    arr = [0, 1, 2, 3, 4, 5, 6, 7]
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > num:
            right = mid - 1
        elif arr[mid] < num:
            left = mid + 1
        else:
            print(f"{num} 在列表中的索引是: {mid}")
            return
    print("不存在")


def double_sum(num: int):
    """两数之和"""
    arr = [0, 1, 2, 3, 4, 5, 6, 7]
    length = len(arr) - 1
    """
    arr[0] + arr[1]
    arr[0] + arr[2]
    arr[0] + arr[3]
    arr[0] + arr[4]
    arr[0] + arr[5]
    arr[0] + arr[6]
    arr[0] + arr[7]
    arr[1] + arr[2]
    arr[1] + arr[3]
    arr[1] + arr[4]
    arr[1] + arr[5]
    arr[1] + arr[6]
    arr[1] + arr[7]"""
    for i in range(length):
        for j in range(i + 1, length):
            if arr[i] + arr[j] == num:
                print(f"arr[{i}] + arr[{j}]: {arr[i]}+{arr[j]}={num}")


def hui_wen(s: str):
    """回文字符串, 一个字符串正向读取和反向读取时一样的，那它就是回文字符串"""
    st = "abccba"
    tmp_list = list(st)
    length = len(st) - 1
    print(tmp_list)
    """
    ab
    abc
    abcc
    abccb
    abccba
    bc
    bcc
    bccb
    bccba
    cc
    ccb
    ccba
    cb
    cba
    ba
    """
    # for i in range(length):


def pub_prefix():
    """找出最长的公共前缀"""
    strs = ["abcaaa", "abcdef", "abcdef", "abc", "aaa", "c"]
    """
    1.找到最短的字符串, 公共前缀的长度不会超过该字符串的长度
    2.遍历最短的字符串
        判断同一位置处的字符是否相等
    """
    str_info = {s: len(s) for s in strs}  # 得到各字符串长度信息
    # 获取最短的那个字符串
    sort_str = sorted(str_info.items(), key=lambda ele: ele[1])
    short_str, length = sort_str[0]
    print(short_str, length)

    pub_pre = ""
    # 遍历最短的字符串
    for i in range(length):
        tmp_set = set()  # 每次循环都进行重置
        for ele in strs:
            tmp_set.add(ele[i])
        if len(tmp_set) == 1:  # 等于1说明这几个字符相等
            pub_pre += short_str[i]
    print(f"公共前缀：{pub_pre}")


if __name__ == '__main__':
    # mao_pao()
    # select_sort()
    # binary_search(8)
    # double_sum(8)
    # hui_wen("a")
    pub_prefix()

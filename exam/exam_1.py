# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：exam_1.py
@Author  ：LiChunBo
@Date    ：2024/7/25 上午9:52
"""
"""
1  python的数据类型都有哪些(5分)
答：字符串、整型、浮点型、布尔型、列表、元组、集合、字典
"""
"""
注：开头字母都应该是小写
2  列表，元组、字典、集合如何定义，分别举例（5分）
"""


# 列表，元组、字典、集合 分别为：
def ans_2():
    list1 = list()
    tuple1 = tuple()
    set1 = set()
    dict1 = dict()


"""
3  列表[1,2,3,4,5,5,2,3,2,4]    去重，不能使用set函数（10分）
"""


def ans_3():
    l = [1, 2, 3, 4, 5, 5, 2, 3, 2, 4]
    res = []
    for ele in l:
        if ele not in res:
            res.append(ele)
    print(f"去重后：{res}")


"""
4  比如有这样一个文件data.txt内存在以下内容（15分）
----------------------------
lucy:21,tom:30,xiaoming:18,xiaohong:15,xiaowang:20,xiaohei:19
----------------------------
请通过代码读取文件并输出年龄大于18岁的人名
"""


def ans_4():
    with open("./tmp.txt", "r", encoding="utf-8") as f:
        content = f.read()
        tmp_strs = content.split(",")
        res = dict()
        for ele in tmp_strs:
            t = ele.split(":")
            res[t[0]] = t[1]
        for name, age in res.items():
            if int(age) > 18:
                print(f"{name}的年龄为：{age}")


"""
5  请用列表推导式得出1-100能被3整除的数（5分）
"""


def ans_5():
    print(f"1-100能被 3整除的数：{[i for i in range(101) if i % 3 == 0]}")


"""
6  continue和break的区别（5分）
答： 
    continue 会结束当前循环，并开始下一次循环；
    break 会终止循环
""""""
7  有一堆字符串，“welocme to super&Test”，打印出emcolew ot tseT&repus全部单词原位置反转，不能使用索引[::-1]输出或者reverse/reversed函数实现，自己写字符串首尾交换方法（15分）
"""


def ans_7():
    strs = "welocme to super&Test"
    tmp_strs = strs.split(" ")
    res = ""

    def str_parse(s: str) -> str:
        tmp = ""
        for ele in s:
            tmp = ele + tmp
        return tmp

    for s in tmp_strs:
        res += f"{str_parse(s)} "
    print(f"字符串反转结果：{res.strip()}")


"""
8  怎么在函数内修改/使用全局变量（5分）
答：使用global关键字
"""
"""
9  python可变数据类型和不可变数据类型都有哪些（5分）
答：
    可变数据类型：列表、集合、字典
    不可变数据类型：字符串、整型、浮点型、元组、布尔型
"""
"""
10 递归实现斐波那契数列（10分）
"""


def ans_10(n):
    if n == 1 or n == 2:
        return 1
    return ans_10(n - 1) + ans_10(n - 2)


"""

11)    debug的快捷键：f8/f7/f9分别的作用（5分）
答：
    F8 debug跳出函数，直接执行到函数结束
    F7 debug执行函数的每一行
    F9 debug到下一个断点
"""

"""
12、如何实现["1","2","3"]变成[1,2,3] ?（5分）
"""


def ans_12():
    tmp = ["1", "2", "3"]
    print(f"转换数据类型后：{[int(i) for i in tmp]}")


"""
13、开发一个注册系统，界面可以用print打印，保存姓名和年龄，存在的用户提示已注册，不存在的可以注册成功（提示建议使用函数划分不同的功能，比如查询用户，新增用户）（10分）
"""


def ans_13():
    users = []

    def is_exists(name: str) -> bool:
        """判断用户是否存在"""
        if len(users) == 0:
            return False
        for user in users:
            if user.get("name") == name:
                return True
        return False

    def add_user():
        name = input("请输入姓名：")
        if not is_exists(name):
            age = int(input("请输入年龄："))
            users.append({"name": name, "age": age})
            print(f"已填加用户：{name}, 年龄：{age}")
        else:
            print(f"用户已存在：{name}")

    def search_users():
        if len(users) == 0:
            print("当前没有用户信息，可通过功能1添加")
        else:
            for user in users:
                print(f"用户：{user.get('name')}, 年龄：{user.get('age')}")

    def main():
        while True:
            print("* " * 25)
            print("*   欢迎使用学生信息管理系统")
            print("*   输入1，新增用户")
            print("*   输入2，查询用户信息")
            print("*   输入3，退出系统")
            print("* " * 25)
            num = input("请输入功能选项：")
            if num == "1":
                add_user()
            elif num == "2":
                search_users()
            elif num == "3":
                print("退出系统")
                break
            else:
                print("输入非法，请重新输入")

    main()


if __name__ == '__main__':
    # ans_3()
    # ans_4()
    # ans_5()
    # ans_7()
    # for i in range(1, 10):
    #     print(ans_10(i), end=" ")
    # ans_12()
    ans_13()

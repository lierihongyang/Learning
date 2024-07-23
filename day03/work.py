# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：work.py
@Author  ：LiChunBo
@Date    ：2024/7/22 下午7:37
"""
"""
1.使用列表推导式生成能被5整除的数（100以内）"""


def answer_1():
    res = [i for i in range(1, 101) if i % 5 == 0]
    print(res)


# 2.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
# list1 = ["小明","小红"]
# list2 = [18,19]
# {"小明":18,"小红":19}
def answer_2():
    list1 = ["小明", "小红"]
    list2 = [18, 19]
    res = {list1[i]: list2[i] for i in range(len(list1))}
    print(res)


"""
3.开发一个注册系统，
页面：
[{name:xxx,age:xxx},{name:xxx,age:xxx},{name:xxx,age:xxx}]
----------------

*   1-新增用户 
*   2-查询单个用户信息
*   3-查询全部用户信息
*   4-删除用户
----------------
功能1：新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
功能2：查询学生信息
功能3：删除学生信息
"""
stu_infos = []  # 用于保存学生信息的列表


def is_exists(name: str) -> bool:
    """判断对应的学生是否存在"""
    if len(stu_infos) == 0:  # 列表长度为0，则直接返回False
        return False
    for stu in stu_infos:  # 遍历每一个学生信息
        if stu.get("name") == name:
            return True
    return False


def search_stu():
    """查询单个学生信息"""
    name = input("请输入学生姓名：")
    if not is_exists(name):
        print(f"学生：{name}不存在")
    else:
        for stu in stu_infos:
            if stu.get("name") == name:
                print(f"已查到学生：{name}, 年龄：{stu.get('age')}")


def add_stu():
    """添加学生信息"""
    name = input("请输入学生姓名：")

    if is_exists(name):
        print(f"name：{name}学生已存在")
    else:
        age = int(input("请输入年龄："))
        stu = {"name": name, "age": age}
        stu_infos.append(stu)
        print(f"已填加学生：{stu.get('name')}, 年龄：{stu.get('age')}")


def get_all_student():
    """获取所有的学生信息"""
    if len(stu_infos) == 0:
        print("当前没有学生信息，可以通过功能 1 添加")
    else:
        for stu in stu_infos:
            print(f"学生姓名：{stu.get('name')}, 年龄：{stu.get('age')}")


def delete_stu():
    """删除学生信息"""
    name = input("请输入要删除的学生姓名：")
    if not is_exists(name):
        print("您要删除的学生不存在")
    else:
        for stu in stu_infos:
            if stu.get("name") == name:
                print(f"删除学生：{name}, age: {stu.get('age')}")
                stu_infos.remove(stu)


def main():
    while True:
        print("* " * 25)
        print("*   欢迎使用学生信息管理系统")
        print("*   输入1，新增用户")
        print("*   输入2，查询单个用户信息")
        print("*   输入3，查询所有用户信息")
        print("*   输入4，删除用户")
        print("*   输入5，退出系统")
        print("* " * 25)
        num = input("请输入功能选项：")
        if num == "1":
            add_stu()
        elif num == "2":
            search_stu()
        elif num == "3":
            get_all_student()
        elif num == "4":
            delete_stu()
        elif num == "5":
            print("退出系统")
            break
        else:
            print("输入非法，请重新输入")


if __name__ == '__main__':
    # answer_1()
    # answer_2()
    main()
    # print(is_exists("l1i"))

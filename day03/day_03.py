# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：day_03.py
@Author  ：LiChunBo
@Date    ：2024/7/22 上午10:40
"""
import os
import shutil


def add_fun(x, y):
    """定义一个函数，计算并打印1+2的结果"""
    print(f"{x} + {y} = {x + y}")


def add_return(x, y):
    return x + y


def print_line():
    print("=" * 20)


def print_lines(n: int):
    for i in range(n):
        print_line()


def add_res(x, y, z):
    return x + y + z


def avg_res(x, y, z):
    return add_res(x, y, z) / 3


global_var = 10


def get_var():
    """访问变量"""
    print(f"初始化全局变量 global var:{global_var}")
    local_var = 0
    print(f"初始化局部变量 local var: {local_var}")


def set_var():
    """修改全局变量"""
    global global_var
    print(f"修改全局变量：{global_var + 1}")
    # print(f"访问局部变量 local var: {local_var}")


def get_var2():
    global global_var
    print(f"访问局部变量：global var: {global_var}")


def fun_return():
    """函数返回多个值"""
    return 1, 2, 3, 'a'


# 函数的参数
def user_info(name, age, sex, country="China"):
    print(f"My name is {name}, age {age}, sex{sex}, country {country}.")


def users(*args):
    print(f"users: {args}")


def users2(**kwargs):
    print(f"kwargs: {kwargs}")


def users3(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


def var_swap():
    a, b = 0, 1
    print(f"交换前：a={a}, b={b}")
    a, b = b, a
    print(f"交换后，a={a}, b={b}")


def unpackage():
    return 'a', 'b'


def get_var_id(var):
    print(f"修改前：var={var}, id={id(var)}")
    var += var
    print(f"修改后：var={var}, id={id(var)}")


def file_operator():
    """文件操作"""
    f = open("./test.txt", "r", encoding="utf-8")
    print(f"文件10个字节的内容：\n{f.read(10)}")
    print(f"当前指针位置：{f.tell()}")
    print(f"文件剩余的全部内容：\n{f.read()}")
    print(f"当前指针位置：{f.tell()}")
    print(f"设置指针位置至文件起始处：{f.seek(0, 0)}")
    print(f"当前指针位置：{f.tell()}")
    print(f"读取一行文件：\n{f.readline()}")
    print(f"当前指针位置：{f.tell()}")
    print(f"剩余文件内容：\n{f.readlines()}")
    print(f"设置指针至文件5的位置：{f.seek(5, 0)}")
    print(f"当前指针位置：{f.tell()}")
    print(f"将指针移至文件末尾：{f.seek(0, 2)}")
    print(f"当前指针位置：{f.tell()}")
    f.close()


def os_concat():
    """os包的一些方法"""
    print(f"os.mkdir()创建一个空文件夹")
    # os.mkdir("d3_test")
    print(f"os.makedirs()递归创建目录")
    # os.makedirs("d3/1/2/3")
    # print(f"os.remove()删除文件")
    # os.remove("test.txt")
    # os.remove("d3_test")    # 无法删除目录
    print("os.rmdir()删除空文件夹")
    print("删除非空目录，shutil.")
    shutil.rmtree("d3")
    # os.rmdir("d3_test")
    print("os.rename()文件重命名")
    # os.rename("tt.tt", "tt.txt")
    print(f"当前目录：{os.getcwd()}")
    print(f"切换目录：{os.chdir('../')}")
    print(f"切换目录后：{os.getcwd()}")
    print(f"当前目录的父级目录：{os.path.dirname('./')}")
    print(f"获取目录中的内容：{os.listdir()}")


def lambda_concat():
    """lambda"""
    fn1 = lambda x: x + 1
    fn2 = lambda x, y: x * y
    print(f"fn1: {fn1(1)}")
    print(f"fn2: {fn2(2, 3)}")
    fn3 = lambda x, y, z=10: x + y + z
    print(f"fn3: {fn3(1, 2)}")
    print(f"fn3: {fn3(1, 2, 3)}")
    fn4 = lambda *args: args
    fn5 = lambda **kwargs: kwargs
    print(f"fn4: {fn4(1, 2, 3)}")
    print(f"fn5: {fn5(name='a', age=20)}")
    t = (4, 5, 6)
    print(f"fn4: {fn4(*t)}")
    d = {"name": "b", "age": 20}
    print(f"fn5: {fn5(**d)}")
    print()

    fn6 = lambda x, y: x if x > y else y
    print(f"fn6: {fn6(4, 8)}")

    ll = [
        {"name": "a", "age": 27},
        {"name": "b", "age": 24},
        {"name": "c", "age": 29},
    ]
    ll.sort(key=lambda x: x["age"])
    print(ll)


def high_fun():
    print(f"abs(-1): {abs(-1)}")
    print(f"abs(1): {abs(1)}")
    print(f"round(1.1): {round(1.1)}")
    print(f"round(1.4): {round(1.4)}")
    print(f"round(1.5): {round(1.5)}")
    print(f"round(1.6): {round(1.6)}")
    print(f"round(2.5): {round(2.5)}")
    print(f"round(2.6): {round(2.6)}")
    print(f"round(3.5): {round(3.5)}")
    print(f"round(4.5): {round(5.5)}")
    print(f"round(5.5): {round(5.5)}")

    def inner(a, b, fun):
        return fun(a) + fun(b)

    print(inner(2, -2, abs))

    print(inner(2.2, 3.5, round))


def sum_1(n):
    """递归求n的累加和"""
    if n == 1:
        return 1
    return n + sum_1(n - 1)


if __name__ == '__main__':
    # add_fun(3, 2)
    # print(1 + 1)
    # print_lines(5)
    # print(avg_res(1, 2, 3))
    # get_var()
    # set_var()
    # get_var2()
    # res = fun_return()
    # print(res)
    # user_info("小明", 20, "男")
    # user_info("小红", sex=20, age="女", country="China")
    # user_info("小芳", 20, "女", "China")
    # users("l", 1, 2)
    # args = [0, 'a', 'b']
    # users(*args)
    # users(args)
    # users2(name="z", age=10, sex="男")
    # info = {"name": "abc", "age": 100, "sex": None}
    # users2(**info)
    # # users2(info)
    # users3(1, 2, 3, abc="abc", dba="dba")
    # var_swap()
    # a, b = unpackage()
    # print(f"拆包：a={a}, b={b}")
    # get_var_id(10)
    # get_var_id([1, 2, 3])
    # file_operator()
    # os_concat()
    # lambda_concat()
    high_fun()
    print(f"5的累加和：{sum_1(5)}")
"""
可变数据类型：列表、字典、集合
不可变数据类型：字符串、数值型（整形、浮点型）、布尔型、None
"""

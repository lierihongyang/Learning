# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：my_module.py
@Author  ：LiChunBo
@Date    ：2024/7/29 下午1:57
"""
# 通过 `from *` 语法导入时，该列表中的项目会被导入；该列表不存在时，`from *`语法会将模块中的全部内容都导入
__all__ = ["add"]


def add(n1, n2):
    print(f"{n1} + {n2} = {n1 + n2}")


def mul(a, b):
    print(f"{a} * {b} = {a * b}")


if __name__ == '__main__':
    pass

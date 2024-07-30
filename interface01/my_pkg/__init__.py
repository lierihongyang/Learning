# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：__init__.py.py
@Author  ：LiChunBo
@Date    ：2024/7/29 下午2:41
"""
# 在包中的__all__，通过`from *`语法导包时，如果没有定义该列表，则全部都不导入，这是为了节省内存
# 如果定义了该列表，则`from *`语法，会将列表中的内容都导入
__all__ = ["m1"]

# -*-coding:utf-8 -*-

"""
# File       : 2-异步.py
# Time       ：2024/9/28 下午8:17
# Author     ：Li
异步使用
"""

import asyncio
import time

now = lambda: time.time()
start = now()


# 定义协程函数
async def func(i):
    await asyncio.sleep(1)
    print(i)


for i in range(5):
    asyncio.run(func(i))

print(f"异步共执行{now() - start}s")

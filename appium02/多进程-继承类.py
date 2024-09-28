# -*-coding:utf-8 -*-

"""
# File       : 多进程-继承类.py
# Time       ：2024/9/7 下午4:52
# Author     ：Li
"""
import json
import os
import random
import time
from multiprocessing import Process, Lock


class Demo(Process):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"running: {self.name}")
        time.sleep(random.randint(1, 3))
        print(f"end...: {self.name}")


data = {"count": 100}


class DemoLock(Process):
    """模拟加锁"""

    def __init__(self, name, lock):
        super().__init__()
        self.name = name
        self.lock = lock

    def search(self) -> int:
        count = data.get("count")
        print(f"剩余票数: {count}")
        return count

    def get(self):
        time.sleep(0.1)  # 模拟延迟

        if self.search() > 0:
            self.lock.acquire()
            data["count"] -= 1
            self.lock.release()
            time.sleep(0.1)
            print(f"{self.name}: 买票完成")
        else:
            return

    def run(self):
        self.get()


if __name__ == '__main__':
    # ps = [Demo(f"process_{i}") for i in range(4)]
    # for p in ps:
    #     p.start()
    # for p in ps:
    #     p.join()
    # print("main end...")
    # print("=" * 100)
    lock = Lock()

    ps = [DemoLock(f"name_{os.getpid()}", lock) for _ in range(100)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    print("main end...")

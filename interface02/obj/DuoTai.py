# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：DuoTai.py
@Author  ：LiChunBo
@Date    ：2024/8/1 下午2:21
"""


class Dog:
    def work(self):
        print("work....")


class ArmDog(Dog):
    def work(self):
        print("arm 追击")


class DrugDog(Dog):
    def work(self):
        print("追缉毒品")


class Human:
    def work_on_dog(self, _dog: Dog):
        _dog.work()


if __name__ == '__main__':
    dog = Dog()
    ag = ArmDog()
    dg = DrugDog()

    h1 = Human()
    h1.work_on_dog(dog)
    h1.work_on_dog(ag)
    h1.work_on_dog(dg)

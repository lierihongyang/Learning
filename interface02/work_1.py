# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：work_1.py
@Author  ：LiChunBo
@Date    ：2024/8/1 下午7:25
"""


class Dog:
    # 类属性
    tooth = 15

    def __init__(self, name: str):
        self.name = name
        self.__sex = "保密"

    @staticmethod
    def static_fun():
        print("这里是Dog static fun no params")

    @staticmethod
    def static_func(a: int, b: int) -> None:
        print(f"这里是Dog static func: {a} + {b} {a + b}")

    @classmethod
    def cls_fun(cls):
        print(f"这里是Dog class fun, tooth: {cls.tooth}")

    def self_fun(self):
        print(f"这里是Dog self fun, name: {self.name}")

    def get_sex(self):
        print(f"{self.name}'s sex {self.__get_sex()}")

    def set_sex(self, sex: str):
        self.__sex = sex

    def __get_sex(self):
        return self.__sex

    def work(self):
        print(f"The dog {self.name} 正在啃骨头")


class Arm(Dog):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        print(f"The arm dog {self.name} 正在追击敌人")


class DrugDog(Dog):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        print(f"The drug dog {self.name} 正在追缉毒品")


class Human:
    def work_on_dog(self, _dog: Dog):
        _dog.work()


if __name__ == '__main__':
    print("封装".center(60, "-"))
    dog = Dog("大黄")
    dog.get_sex()
    dog.set_sex("baomi")
    # print(dog._Dog__get_sex())
    dog.get_sex()
    print("继承".center(60, "-"))
    arm = Arm("斗犬")
    arm.get_sex()  # 继承的方法
    print(arm.tooth)  # 继承的属性
    # print(arm._Dog__get_sex())
    dg = DrugDog("小黑")
    print(f"{dg.name}原来有{dg.tooth}颗牙齿")
    dg.tooth = 10
    print(f"{dg.name}现在有{dg.tooth}颗牙齿")
    print("多态".center(60, "-"))
    h = Human()
    h.work_on_dog(dog)
    h.work_on_dog(arm)
    h.work_on_dog(dg)
    print("类方法-实例方法-静态方法".center(60, "-"))
    dog.self_fun()
    dog.static_func(1, 2)
    dog.static_fun()
    Dog.self_fun(dog)
    Dog.static_fun()
    Dog.static_func(2, 3)
    dog.cls_fun()
    Dog.cls_fun()

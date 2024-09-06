# -*- coding: UTF-8 -*-
import json

import requests


class ReqCont:
    """请求-requests模块"""

    def __init__(self, url):
        self.url = url
        self.data = None
        self.params = None
        self.headers = None
        self.response = None
        self.cookies = None

    def req_get(self):
        """get请求"""
        # params中的参数会被拼接到url中
        self.response = requests.get(url=self.url, params=self.params, headers=self.headers)
        print(f"请求地址: {self.response.url}")
        print(f"请求头: {self.response.request.headers}")
        print(f"响应体: {self.response.text}")
        print(f"响应体-json: {self.response.json()}")
        print(f"响应体-byte: {self.response.content}")

    def post_form(self):
        # 传递到data中的数据，格式是 application/x-www-form-urlencoded表单
        self.response = requests.post(url=self.url, data=self.data)
        print(f"请求体: {self.response.request.body}")
        print(f"请求体: {self.response.text}")

    def post_json(self):
        # 传递到json中的，格式是application/json格式
        self.response = requests.post(url=self.url, json=self.data)
        print(f"请求体: {self.response.request.body}")
        print(f"请求体: {self.response.text}")

    def use_default_cookie(self):
        self.response = requests.get(url=self.url, cookies=self.cookies)
        print(f"请求体: {self.response.request.body}")
        print(f"请求体: {self.response.text}")


class Animal:
    name = "动物"

    def run(self):
        print("正在追赶猎物")


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def run(self):
        print(f"狗子: {self.name} 正在奔跑")


class PoliceDog(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"警犬: {self.name}正在追犯人")


class HoundDog(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"猎犬: {self.name}正在追捕猎物")


class People:
    def __init__(self, name):
        self.name = name

    def run(self, animal: Animal):
        print(f"{self.name}的动物")
        animal.run()


if __name__ == '__main__':
    base_url = "http://127.0.0.1:5000/"
    req = ReqCont(base_url)
    data = {
        "username": "user1",
        "password": "p001"
    }
    # 登录
    req.url = base_url + "login"
    req.data = data
    req.post_form()

    # 获取cookie
    headers = req.response.headers
    req.cookies = req.response.cookies
    # 获取用户信息
    req.url = base_url + "profile"
    req.headers = {"Cookie": headers["Set-Cookie"]}
    req.req_get()
    print("-" * 50)
    # 注册
    req.url = base_url + "register"
    req.data = {
        "username": "xiaoming",
        "password": "123",
        "age": 20,
        "sex": "男"
    }
    req.post_json()
    print("-" * 50)
    req.url = base_url + "profile"
    req.use_default_cookie()
    print("-" * 50)
    s = requests.session()
    res = s.post(url=base_url + "login", data=data)
    print(res.text)
    res2 = s.get(url=base_url + "profile")
    print(res2.text)
    print("=" * 60)
    pd = PoliceDog("小黑")
    dd = Dog()
    hd = HoundDog("大黄")
    xiaoming = People("小明")
    xiaoming.run(pd)
    xiaoming.run(dd)
    xiaoming.run(hd)

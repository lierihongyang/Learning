# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：work_4.py
@Author  ：LiChunBo
@Date    ：2024/8/2 上午10:06
"""
import json

import requests


def req_get():
    url = "https://www.kuaidi100.com/query"
    data = {"type": "shunfeng", "postid": "SF1409812533370"}
    # params接收的数据会被拼接到url中
    response = requests.request("get", url=url, params=data)

    print(f"response-obj: {response}")
    print(f"响应头：{response.status_code}")
    print(f"请求url: {response.url}")
    print(f"响应: {response.text}")
    print(f"json格式响应: {response.json()}")
    print(f"字节格式响应: {response.content}")
    print(f"耗时: {response.elapsed}")
    print("=" * 60)
    print(f"请求-obj: {response.request}")
    print(f"请求头: {response.request.headers}")
    print(f"请求体(get请求没有请求体，所以这里是): {response.request.body}")
    print(f"cookies: {response.cookies}")
    print(f"将cookies转换为dict类型: {response.cookies.get_dict()}")


def post_frame():
    """frame表单"""
    url = "http://httpbin.org//post"
    data = {"username": "liangchao", "password": "123456"}
    response = requests.post(url, data=data)
    print(f"响应体: {response.text}")


def post_json():
    """json格式请求体"""
    url = "http://httpbin.org//post"
    data = {"username": "liangchao", "password": "123456"}
    response = requests.post(url=url, data=json.dumps(data))
    # response = requests.post(url=url, json=data)
    print(f"响应体: {response.json()}")


if __name__ == '__main__':
    # req_get()
    post_frame()
    post_json()

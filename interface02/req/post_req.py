# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：post_req.py
@Author  ：LiChunBo
@Date    ：2024/8/1 下午5:43
"""
import json

import requests


def dict_str():
    """字典&字符串相互转化"""
    s = r'{"data":{"admin":false,"chapterTops":[],"coinCount":67703,"collectIds":[12489,12554,20867,20535,20932,20931,20925,20923,21681,1165,2334,-1,23168,23646,24990,25477,26578,26503,26583,12240,24206,26795,-1,-1,18615,-1,21498,8652,26624,28069,27996,18281,8857],"email":"rainshine1190@126.com","icon":"","id":17180,"nickname":"liangchao","password":"","publicName":"liangchao","token":"","type":0,"username":"liangchao"},"errorCode":0,"errorMsg":""}'
    print(f"s type: {type(s)}")
    dict_s = json.loads(s)
    print(f"dict s type: {type(dict_s)}")
    print(f"dict s: {(dict_s)}")

    d = {"name": "小红", "age": 20, "对象": None}
    print(f"d type: {type(d)}")
    s_d = json.dumps(d, ensure_ascii=False)
    print(f"s d type: {type(s_d)}")
    print(f"s d: {s_d}")


def post_from():
    """from表单的方式"""
    url = "http://httpbin.org//post"
    # 准备数据
    data = {"username": "liangchao", "password": "123456"}
    # data中的参数会传递到请求体中
    res = requests.post(url=url, data=data)
    print(f"响应体：\n{res.text}")


def post_json():
    """json的方式"""
    url = "http://httpbin.org//post"
    data = {"username": "liangchao", "password": "123456"}
    res = requests.post(url=url, json=data)
    # res = requests.post(url=url, data=json.dumps(data))
    print(f"响应体：\n{res.text}")


if __name__ == '__main__':
    # dict_str()
    # post_from()
    post_json()

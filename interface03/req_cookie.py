# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：req_cookie.py
@Author  ：LiChunBo
@Date    ：2024/8/5 上午9:50
"""
import requests


def default_cookie():
    url = "https://wanandroid.com/user/login"
    data = {"username": "ymw001", "password": "123456"}
    res = requests.post(url, data=data)
    cookies = res.cookies
    print(cookies)

    url2 = "https://wanandroid.com//user/lg/userinfo/json"
    info = requests.get(url2, cookies=cookies)
    print(f"info: {info.text}")


def custom_headers():
    """自定义请求体headers
    无论鉴权字段在响应头中还是在响应体中，都可以手动地将其取出，然后传递下去，更灵活一些
    """
    url = "https://wanandroid.com/user/login"
    data = {"username": "ymw001", "password": "123456"}
    res = requests.post(url, data=data)
    print(res.text)
    # cookies = res.cookies
    # print(cookies)

    headers = {"Cookie": res.headers["Set-Cookie"]}
    url2 = "https://wanandroid.com//user/lg/userinfo/json"
    info = requests.get(url2, headers=headers)
    print(f"info: {info.text}")


def use_session_obj():
    """使用session对象
    适用于鉴权字段在响应头中的情况session对象会将响应头中的信息作为请求头传递下去；
    所以不适用于鉴权字段在响应体中的情况。
    """
    s = requests.session()
    data = {"username": "ymw001", "password": "123456"}
    res = s.post("https://wanandroid.com/user/login", data=data)
    print(res.text)

    r = s.get("https://wanandroid.com//user/lg/userinfo/json")
    print(r.text)


if __name__ == '__main__':
    # default_cookie()
    # custom_headers()
    use_session_obj()

# -*- coding: UTF-8 -*-

"""
@Project ：Learning
@File    ：get_req.py
@Author  ：LiChunBo
@Date    ：2024/8/1 下午5:12
"""
import requests

url1 = 'https://www.kuaidi100.com/query'
data = {"type": "shunfeng", "postid": "SF1409812533370"}
# params中的数据会拼接到url中
res = requests.get(url1, params=data)

print(f"res:{res}")
print(f"响应头:\n{res.headers}")
print(f"状态码：{res.status_code}")
print(f"请求地址：{res.url}")
print(f"请求头：\n{res.request.headers}")
print(f"请求体：{res.request.body}")
print(f"cookie: {res.cookies}")
print(f"获取字典格式的cookies: {res.cookies.get_dict()}")
print(f"响应体: \n{res.text}")
print(f"json格式的响应体:\n{res.json()}")
print(f"获取字节格式的响应：\n{res.content}")
print(f"耗时：{res.elapsed}")

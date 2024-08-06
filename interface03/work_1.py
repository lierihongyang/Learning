# -*- coding: UTF-8 -*-
import json
import requests
import xlrd
import yaml


def use_cookie():
    """使用cookie保存登录状态"""
    url = "https://wanandroid.com/user/login"  # 登录接口
    data = {"username": "ymw001", "password": "123456"}  # 用户数据
    res = requests.post(url, data=data)  # 用户登录使用的是form表单的传参方式，这里使用data
    # 获取cookie
    cookie = res.cookies
    print(f"cookie: {cookie}")

    # 用户信息获取接口，用户需要是登录状态才能查询
    get_info = "https://wanandroid.com//user/lg/userinfo/json"
    info = requests.get(url=get_info, cookies=cookie)  # cookie传递
    print(f"info: {info.text}")


def custom_headers():
    """自定义请求体
    无论鉴权字段在响应头中还是在响应体中，都可以手动地将其取出，在下一次请求时将其传递，使用更灵活
    """
    url = "https://wanandroid.com/user/login"
    data = {"username": "ymw001", "password": "123456"}
    response = requests.post(url, data=data)
    print(f"header: \n{response.headers}")

    headers = {"Cookie": response.headers["Set-Cookie"]}
    get_info = "https://wanandroid.com//user/lg/userinfo/json"
    info = requests.get(get_info, data=data, headers=headers)
    print(f"info: {info.text}")


def use_session_obj():
    """通过session对象传递cookie
    适用于鉴权字段在请求头中的情况，session对象会将请求头中的信息传递下去；
    但是当鉴权字段在相应体中时，该方法就不适用了
    """
    s = requests.session()
    url = "https://wanandroid.com/user/login"
    data = {"username": "ymw001", "password": "123456"}
    res = s.post(url=url, data=data)
    print(res.text)

    get_info = "https://wanandroid.com//user/lg/userinfo/json"
    info = s.get(get_info)
    print(info.text)


class ReadData:
    def __init__(self, file_name: str):
        if file_name.endswith(".xls"):
            self.file = xlrd.open_workbook(file_name)
        else:
            self.file = open(file_name)

    def read_xlsx(self) -> list[dict]:
        """读取excel中的数据"""
        data = []
        sheet = self.file.sheet_by_index(0)
        rows = sheet.nrows  # 总行数
        cols = sheet.ncols  # 总列数

        keys = sheet.row_values(0)  # 将第一行(表头)作为key
        for row in range(1, rows):
            value = sheet.row_values(row)
            tmp_data = zip(keys, value)
            data.append(dict(tmp_data))
        return data

    def read_json(self) -> list[dict]:
        data = json.load(self.file)
        return list(data.values())

    def read_yaml(self) -> list[dict]:
        data = yaml.load(self.file, Loader=yaml.FullLoader)
        return data

    def __del__(self):
        del self.file


if __name__ == '__main__':
    # use_cookie()
    # custom_headers()
    # use_session_obj()
    rd = ReadData("data.xls")
    print(rd.read_xlsx())
    # print(rd.read_json())
    # print(rd.read_yaml())

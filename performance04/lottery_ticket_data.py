# -*- coding: UTF-8 -*-
"""获取最近500期彩票数据"""
import json
import random
import time
import requests
from bs4 import BeautifulSoup

"""
pip install beautifulsoup4
pip install lxml
"""


def get_html_info(n: int):
    """发起请求
    网页一共17页，通过接收参数，动态拼接url
    """
    url = f"https://www.ydniu.com/open/ssq-500/{n}.html"
    # 构建请求头
    headers = {
        "Accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "Hm_lvt_20f814af61b79c7337034b078fad5707=1724730665,1724737202; HMACCOUNT=F1D743A6D4A4E8F5; Hm_lpvt_20f814af61b79c7337034b078fad5707=1724737828",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "document"
    }
    return requests.get(url=url, headers=headers)


def get_numbers(td_i) -> str:
    """提取开奖号码"""
    number = ""
    all_i = td_i.find_all("i")
    for i in all_i:
        number += i.string
    return number


def get_winning_info(tds) -> ():
    """提取开奖信息"""
    issue = tds[0].string  # 期号
    date_time = tds[1].string  # 开奖时间
    number = get_numbers(tds[2])  # 开奖号码
    total_sale = tds[3].string.replace("\n", "").strip()  # 总销售额
    money_pool = tds[6].string  # 累计奖池
    return issue, {
        "期号": issue,
        "开奖时间": date_time,
        "开奖号码": number,
        "总销售额": total_sale,
        "累计奖池": money_pool
    }


def get_ticket_info():
    """获取500期彩票数据"""
    # 500期的彩票信息
    lottery_tiket_info = {}
    for i in range(1, 18):
        time.sleep(random.randint(1, 5))  # 随机休眠1 - 5秒
        response = get_html_info(i)
        soup = BeautifulSoup(response.text, "lxml")
        all_tr = soup.find("tbody").find_all("tr")  # 获取所有`tbody`下的`tr`标签
        # 遍历每个`tr`标签，获取彩票数据
        for tr in all_tr:
            tds = tr.find_all("td")
            issue, info = get_winning_info(tds)
            lottery_tiket_info[issue] = info
    with open("./lottery_ticket_data.json", "w", encoding="utf-8") as f:
        json.dump(lottery_tiket_info, f, ensure_ascii=False)


if __name__ == '__main__':
    get_ticket_info()

# -*- coding: UTF-8 -*-
"""正则表达式"""

import re

s = "ad2024-08-19aa"
# res = re.search(r"(\d{4})-(\d{2})-(\d{2})", s)
res = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", s)
print("匹配对象：", res)
# print("group()分组0：", res.group())
# print("group(1)分组1：", res.group(1))
# print("group(2)分组2：", res.group(2))
# print("group(3)分组3：", res.group(3))
# print("groups()全部分组：", res.groups())


print("group()分组0：", res.group())
print("group('name')分组1：", res.group("year"))
print("group('month')分组2：", res.group("month"))
print("group('day')分组3：", res.group("day"))

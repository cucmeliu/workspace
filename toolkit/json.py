#!/usr/bin/python
# -*- coding: UTF-8 -*-


import json

# 将一个Python数据结构转换为JSON
data = {
'name' : 'ACME',
'shares' : 100,
'price' : 542.23
}

json_str = json.dumps(data)

# 将一个JSON编码的字符串转换回一个Python数据结构
data = json.loads(json_str)

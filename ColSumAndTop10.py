#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: zhuzhipeng
# @Time: 2020/3/10|10:44 下午
# @Motto： Knowledge comes from decomposition

import json
"""
输出Hello world
计算 /tcdata/num_list.csv中一列数字的总和。
在/tcdata/num_list.csv文件中寻找最大的10个数，从大到小生成一个ListList.
"""
data = []
with open("./tcdata/num_list.csv") as f:
    for line in f:
        data.append(int(line.strip()))


q1 = "Hello world"
q2 = sum(data)
q3 = data.sort(reverse=True)[:10]
line = json.loads({
    'Q1': q1,
    'Q2': q2,
    'Q3': q3,
})

json.dump(line, open('result.json', 'w'))




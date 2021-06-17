#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/5 20:27
# @Author  : 周卫东
# @File    : generate_cross_item.py
# @Software: PyCharm

import pandas as pd
from sklearn import preprocessing
from sklearn_pandas import DataFrameMapper
import re

data = pd.DataFrame({'室外温度': [1, 2, 3], '室内湿度': [4, 5, 6], '室内温度': [2., 6, 9]})


# 生成交乘项
def generate_multi_term(data):
    """
    输入：原始数据集-DataFrame
    输出：包含所有变量的交乘项的数据集-DataFrame
    """
    mapper = DataFrameMapper([(list(data.columns),
                               [preprocessing.PolynomialFeatures(degree=2, interaction_only=True,
                                                                         include_bias=False)])])
    # 生成交乘项
    data_tr = mapper.fit_transform(data.copy())

    # 生成交乘项的列名
    names_tr = []

    for name in mapper.transformed_names_:
        names = map(int, re.findall(r'\d+', name))
        name_tr = ''
        for i in names:
            name_tr = name_tr + list(data.columns)[i] + '*'
        names_tr.append(name_tr[:-1])
    return pd.DataFrame(data_tr, columns=names_tr)


data = generate_multi_term(data)

print(data)
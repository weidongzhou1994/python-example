#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/17 11:21
# @Author  : Weidong Zhou
# @File    : dict_in_list_dup.py
# @Software: PyCharm

from functools import reduce


def list_in_dict_dup_rem(data: list):
    """
    :param data: dict in list
    :return:dict in list - no dup
    reduce(func, data)
    """
    rem_function = lambda x, y: x if y in x else x + [y]
    # 不加 [], python 会默认内部的元素为 dict
    return reduce(rem_function, [[], ] + data)


test_list = [
    {
        "name": "aaa",
        "phone": "123456"
    },
    {
        "name": "bbb",
        "phone": "123456"
    },
    {
        "name": "aaa",
        "phone": "123456"
    }]

rem_data = list_in_dict_dup_rem(test_list)
print(rem_data)
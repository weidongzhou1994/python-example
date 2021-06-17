"""
@创建日期 : 2021/6/17
@修改日期 : 2021/6/17   
@作者 : Weidong Zhou
@功能 :
"""


import numpy as np


def list_array_duplicate_removal(array_list: list):
    array_list_dp = []
    array_list_indexes = []
    for i in range(len(array_list)):
        nums = 0
        for j in range(len(array_list_dp)):
            if np.array_equal(array_list[i], array_list_dp[j]):
                nums += 1
                print(array_list[i])
        if nums == 0:
            array_list_dp.append(array_list[i])
            array_list_indexes.append(i)
    return [array_list[index] for index in array_list_indexes]

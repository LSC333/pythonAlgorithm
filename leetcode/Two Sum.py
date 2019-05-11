# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 19:45
# @Author  : ValarMorghulis
# @File    : Two Sum.py

from numpy import sort


def twoSum(nums, target):
    dic={}
    for i in range(len(nums)):
        dic[nums[i]]=i
    for i in range(len(nums)):
        if target-nums[i] in dic and dic[target-nums[i]]!=i:
            return [i, dic[target-nums[i]]]

arr = [3,2,4]

print(twoSum(arr, 6))
# print(dict.fromkeys(arr))
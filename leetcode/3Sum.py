# -*- coding: utf-8 -*-
# @Time    : 2019/4/25 22:43
# @Author  : ValarMorghulis
# @File    : 3Sum.py


def threeSum(nums):
    nums.sort()
    res = []
    dic = {}
    for i in range(len(nums)):
        dic[nums[i]] = i
    for i in range(len(nums)):
        t=-nums[i]
        for j in range(i+1,len(nums)):
            if t-nums[j] in dic and dic[t-nums[j]]>j:
                res.append([nums[i], nums[j], t-nums[j]])
    res = list(set([tuple(t) for t in res]))
    return res

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
# -*- coding: utf-8 -*- 
# @Time : 2019/6/29 11:31 
# @Author : ValarMorghulis 
# @File : 1071.py
import re


def solve():
    s = input()
    words = re.findall('[0-9|A-Z|a-z]+', s)
    words = [i.lower() for i in words]
    dic = dict()
    ans, num = "", 0
    for i in words:
        if i not in dic:
            dic[i] = 0
        dic[i] += 1
    ans = sorted([[dic[i], i] for i in dic], key=lambda x: (-x[0], x[1]))
    print(ans[0][1], ans[0][0])


if __name__ == "__main__":
    solve()

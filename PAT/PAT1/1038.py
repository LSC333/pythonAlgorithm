# -*- coding: utf-8 -*- 
# @Time : 2019/6/2 15:12 
# @Author : ValarMorghulis 
# @File : 1038.py
import functools


def cmp(a, b):
    x = a + b
    y = b + a
    return -1 if x < y else (0 if x == y else 1)


def solve():
    s = input().split()
    s.pop(0)
    s.sort(key=functools.cmp_to_key(cmp))
    print(int(''.join(s)))


if __name__ == "__main__":
    solve()

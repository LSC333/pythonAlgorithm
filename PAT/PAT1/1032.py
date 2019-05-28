# -*- coding: utf-8 -*-
# @Time : 2019/5/28 18:54
# @Author : ValarMorghulis
# @File : 1032.py


def solve():
    s, e, n = input().split()
    n = eval(n)
    tmp = dict()
    for i in range(n):
        address, data, nex = input().split()
        tmp[address] = nex
    posa, posb = s, e
    ans = list()
    while posa != '-1':
        ans.append(posa)
        posa = tmp[posa]
    while (posb not in ans) and posb != '-1':
        posb = tmp[posb]
    print(posb)


if __name__ == "__main__":
    solve()


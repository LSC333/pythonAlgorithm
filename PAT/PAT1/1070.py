# -*- coding: utf-8 -*- 
# @Time : 2019/6/28 14:36 
# @Author : ValarMorghulis 
# @File : 1070.py
import functools


class moonCake:
    def __init__(self, amounts, tot):
        self.amounts = amounts
        self.tot = tot
        self.price = tot / amounts


def cmp(a, b):
    return -1 if a.price < b.price else 1


def solve():
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(float, input().split()))
    cake = list()
    for i in range(n):
        cake.append(moonCake(a[i], b[i]))
    cake = sorted(cake, key=functools.cmp_to_key(cmp), reverse=True)
    ans = 0
    for i in range(n):
        if cake[i].amounts < d:
            ans += cake[i].tot
            d -= cake[i].amounts
        else:
            ans = ans + cake[i].price * d
            break
    print("%.2f" % ans)


if __name__ == "__main__":
    solve()

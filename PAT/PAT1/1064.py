# -*- coding: utf-8 -*- 
# @Time : 2019/6/25 10:48 
# @Author : ValarMorghulis 
# @File : 1064.py
from math import log

ans = list()
a=list()

def level(s, e, index):
    if s > e:
        return
    global ans
    tot = e - s + 1
    l = int(log(tot + 1) / log(2))
    leaves = tot - 2 ** l + 1
    root = s + min(leaves, 2 ** (l - 1)) + 2 ** (l - 1) - 1
    ans[index]=a[root]
    level(s, root - 1, index*2+1)
    level(root + 1, e, index*2+2)


def solve():
    global ans, a
    n = int(input())
    ans = [0 for i in range(n)]
    a = list(map(int, input().split()))
    a.sort()
    level(0, n - 1, 0)
    print(*ans)


if __name__ == "__main__":
    solve()

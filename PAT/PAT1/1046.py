# -*- coding: utf-8 -*- 
# @Time : 2019/6/6 11:15 
# @Author : ValarMorghulis 
# @File : 1046.py
def solve():
    a = list(map(int, input().split()))
    n = a[0]
    a[0] = 0
    for i in range(1, n + 1):
        a[i] += a[i - 1]
    m = int(input())
    for i in range(m):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        print(min(a[e - 1] - a[s - 1], a[n] - (a[e - 1] - a[s - 1])))


if __name__ == "__main__":
    solve()

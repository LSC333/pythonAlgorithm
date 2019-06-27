# -*- coding: utf-8 -*- 
# @Time : 2019/6/27 10:28 
# @Author : ValarMorghulis 
# @File : 1067.py
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    t = [0 for i in range(n)]
    for i in range(n):
        t[a[i]] = i
    cnt = 0
    for i in range(n):
        while t[0] != 0:
            t[t[0]], t[0] = t[0], t[t[0]]
            cnt += 1
        if t[i] != i:
            t[i], t[0] = t[0], t[i]
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    solve()

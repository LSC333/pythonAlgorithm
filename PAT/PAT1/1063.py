# -*- coding: utf-8 -*- 
# @Time : 2019/6/24 15:08 
# @Author : ValarMorghulis 
# @File : 1063.py
def solve():
    n = int(input())
    tot = list()
    for i in range(n):
        a = list(map(int, input().split()))
        t = list()
        for i in range(1, len(a)):
            if a[i] not in t:
                t.append(a[i])
        t.sort()
        tot.append(t)
    k = int(input())
    for i in range(k):
        a, b = map(int, input().split())
        posa, posb, cnt = 0, 0, 0
        while posa < len(tot[a - 1]) and posb < len(tot[b - 1]):
            if tot[a - 1][posa] == tot[b - 1][posb]:
                cnt += 1
                posa += 1
                posb += 1
            elif tot[a - 1][posa] < tot[b - 1][posb]:
                posa += 1
            else:
                posb += 1
        print("%.1f%%" % (cnt*100 / (len(tot[a - 1]) + len(tot[b - 1]) - cnt)))


if __name__ == "__main__":
    solve()

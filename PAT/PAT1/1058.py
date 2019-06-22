# -*- coding: utf-8 -*- 
# @Time : 2019/6/22 10:18 
# @Author : ValarMorghulis 
# @File : 1058.py
def solve():
    a, b = input().split()
    a = list(map(int, a.split('.')))
    b = list(map(int, b.split('.')))
    a[2] += b[2]
    a[1] = a[1] + b[1] + a[2] // 29
    a[2] %= 29
    a[0] = a[0] + b[0] + a[1] // 17
    a[1] %= 17
    print("%d.%d.%d" % (a[0], a[1], a[2]))


if __name__ == "__main__":
    solve()

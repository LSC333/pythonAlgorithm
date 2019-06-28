# -*- coding: utf-8 -*- 
# @Time : 2019/6/28 13:13 
# @Author : ValarMorghulis 
# @File : 1069.py
def solve():
    n = int(input())
    while n and n != 6174:
        n = "%04d" % n
        n = list(map(int, list(n)))
        n.sort()
        small = n[0] * 1000 + n[1] * 100 + n[2] * 10 + n[3]
        big = n[3] * 1000 + n[2] * 100 + n[1] * 10 + n[0]
        n = big - small
        print("%04d - %04d = %04d" % (big, small, n))


if __name__ == "__main__":
    solve()

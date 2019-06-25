# -*- coding: utf-8 -*- 
# @Time : 2019/6/25 11:28 
# @Author : ValarMorghulis 
# @File : 1065.py
def solve():
    n = int(input())
    for i in range(1, n + 1):
        print("Case #%d:" % i, end=' ')
        a, b, c = map(int, input().split())
        print("true" if a + b > c else "false")


if __name__ == "__main__":
    solve()

# -*- coding: utf-8 -*- 
# @Time : 2019/6/8 16:13 
# @Author : ValarMorghulis 
# @File : 1050.py
def solve():
    s1 = input()
    s2 = input()
    for i in s1:
        if i not in s2:
            print(i, end="")


if __name__ == "__main__":
    solve()

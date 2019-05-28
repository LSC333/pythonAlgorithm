# -*- coding: utf-8 -*- 
# @Time : 2019/5/28 18:17 
# @Author : ValarMorghulis 
# @File : 1031.py
def solve():
    s = input()
    left = (len(s) + 2) // 3
    bottom = left + (len(s) + 2) % 3
    for i in range(left):
        if i != left-1:
            print(s[i], end='')
            for j in range(bottom-2):
                print(' ', end='')
            print(s[len(s)-1-i])
        else:
            print(s[left-1:left+bottom-1])


if __name__ == "__main__":
    solve()

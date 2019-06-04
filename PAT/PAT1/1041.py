# -*- coding: utf-8 -*- 
# @Time : 2019/6/4 17:23 
# @Author : ValarMorghulis 
# @File : 1041.py
def solve():
    a = list(map(int, input().split()[1:]))
    ans = dict()
    for i in a:
        if i not in ans.keys():
            ans[i] = 0
        ans[i] += 1
    flag = True
    for i in a:
        if ans[i] == 1:
            flag = False
            print(i)
            break
    if flag:
        print("None")


if __name__ == "__main__":
    solve()

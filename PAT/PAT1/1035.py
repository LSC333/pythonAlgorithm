# -*- coding: utf-8 -*- 
# @Time : 2019/5/31 16:27 
# @Author : ValarMorghulis 
# @File : 1035.py
def solve():
    n = eval(input())
    res = list()
    for i in range(n):
        team, pwd = input().split()
        if '1' in pwd or '0' in pwd or 'l' in pwd or 'O' in pwd:
            if '1' in pwd:
                pwd=pwd.replace('1', '@')
            if '0' in pwd:
                pwd=pwd.replace('0', '%')
            if 'l' in pwd:
                pwd=pwd.replace('l', 'L')
            if 'O' in pwd:
                pwd=pwd.replace('O', 'o')
            res.append(team + ' ' + pwd)
    if len(res) == 0:
        if n == 1:
            print("There is 1 account and no account is modified")
        else:
            print("There are %d accounts and no account is modified" % n)
    else:
        print(len(res))
        for i in res:
            print(i)


if __name__ == "__main__":
    solve()

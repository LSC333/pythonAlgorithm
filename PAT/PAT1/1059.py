# -*- coding: utf-8 -*- 
# @Time : 2019/6/22 11:01 
# @Author : ValarMorghulis 
# @File : 1059.py
maxn = 2000
t = [True for i in range(maxn)]

def init():
    global t
    for i in range(2, maxn):
        if t[i]:
            # prime.append(i)
            j = 2
            while j * i < maxn:
                t[j * i] = False
                j += 1


def solve():
    n = eval(input())
    print("%d=" % n, end='')
    if n == 1:
        print(1, end='')
    i, cnt = 2, 0
    flag = False
    while n > 1:
        while not t[i] or n % i:
            i += 1
        while n % i == 0:
            n //= i
            cnt += 1
        if flag:
            print('*', end='')
        else:
            flag = True
        print("%d" % i, end='')
        if cnt > 1:
            print("^%d" % cnt, end='')
        cnt = 0
    print('')


if __name__ == "__main__":
    init()
    solve()

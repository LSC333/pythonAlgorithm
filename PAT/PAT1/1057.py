# -*- coding: utf-8 -*- 
# @Time : 2019/6/13 11:10 
# @Author : ValarMorghulis 
# @File : 1057.py
s = list()
c = [0 for i in range(100861)]


def lowBit(x):
    return x & (-x)


def update(x, v):
    i = x
    while i < 100861:
        c[i] += v
        i += lowBit(i)


def getSum(x):
    sum, i = 0, x
    while i >= 1:
        sum += c[i]
        i -= lowBit(i)
    return sum


def find():
    left, right, k = 1, 100861, (len(s) + 1) // 2
    while left < right:
        mid = (left + right) // 2
        if getSum(mid) >= k:
            right = mid
        else:
            left = mid + 1
    print(left)


def solve():
    global c, s
    n = int(input())
    for i in range(n):
        command = input().split()
        if command[0][1] == 'u':
            s.append(int(command[1]))
            update(int(command[1]), 1)
        elif command[0][1] == 'o':
            if len(s) == 0:
                print("Invalid")
            else:
                update(s[-1], -1)
                print(s[-1])
                s.pop()
        elif command[0][1] == 'e':
            if len(s) == 0:
                print("Invalid")
            else:
                find()


if __name__ == "__main__":
    solve()

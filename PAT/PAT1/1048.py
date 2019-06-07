# -*- coding: utf-8 -*- 
# @Time : 2019/6/7 17:22 
# @Author : ValarMorghulis 
# @File : 1048.py
def solve():
    n, m = map(int, input().split())
    money = [0 for i in range(1000)]
    a = list(map(int, input().split()))
    a = sorted(a, key=lambda x: x)
    for i in range(n):
        money[a[i]] += 1
    flag = False
    for i in range(n):
        if a[i] != m - a[i]:
            if money[m - a[i]]:
                print("%d %d" % (min(a[i], m - a[i]), max(a[i], m - a[i])))
                flag = True
                break
        elif money[a[i]] >= 2:
            print("%d %d" % (a[i], a[i]))
            flag = True
            break
    if not flag:
        print("No Solution")


if __name__ == "__main__":
    solve()

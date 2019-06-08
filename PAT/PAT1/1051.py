# -*- coding: utf-8 -*- 
# @Time : 2019/6/8 16:59 
# @Author : ValarMorghulis 
# @File : 1051.py
def solve():
    m, n, k = map(int, input().split())
    for i in range(k):
        stack=list()
        flag = True
        a = list(map(int, input().split()))
        pos = 0
        for j in range(1, n + 1):
            stack.append(j)
            if len(stack) > m:
                flag = False
                break
            while stack and stack[-1] == a[pos]:
                stack.pop()
                pos += 1
        if not flag:
            print("NO")
        elif pos == n:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()

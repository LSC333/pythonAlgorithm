# -*- coding: utf-8 -*- 
# @Time : 2019/6/27 16:51 
# @Author : ValarMorghulis 
# @File : 1068.py
def solve():
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    dp = [0 for i in range(m + 1)]
    flag = [[False for i in range(m + 1)] for j in range(n)]
    c.sort(key=lambda x: -x)
    for i in range(n):
        for j in range(m, 0, -1):
            if j >= c[i] and dp[j] <= dp[j - c[i]] + c[i]:
                dp[j] = dp[j - c[i]] + c[i]
                flag[i][j] = True
    if dp[m] != m:
        print("No Solution")
    else:
        i, j = n-1, m
        while i != -1 and j != 0:
            if flag[i][j]:
                j -= c[i]
                print(c[i], end=('\n' if j == 0 else ' '))
            i -= 1


if __name__ == "__main__":
    solve()

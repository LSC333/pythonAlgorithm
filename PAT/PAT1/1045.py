# -*- coding: utf-8 -*- 
# @Time : 2019/6/6 10:13 
# @Author : ValarMorghulis 
# @File : 1045.py
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = [[0 for i in range(b[0] + 5)] for j in range(a[0] + 5)]
    for i in range(1, a[0] + 1):
        for j in range(1, b[0] + 1):
            ans[i][j] = max(ans[i - 1][j], ans[i][j - 1]) if a[i] != b[j] else max(ans[i - 1][j], ans[i][j - 1]) + 1
    print(ans[a[0]][b[0]])


if __name__ == "__main__":
    solve()

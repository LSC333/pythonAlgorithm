# -*- coding: utf-8 -*- 
# @Time : 2019/6/4 19:19 
# @Author : ValarMorghulis 
# @File : 1042.py
def solve():
    t = ['S', 'H', 'C', 'D', 'J']
    n = int(input())
    a = list(map(int, input().split()))
    ans = list()
    for i in range(54):
        tmp = "%c%d" % (t[i // 13], i % 13 + 1)
        ans.append(tmp)
    for j in range(n):
        tans = ans.copy()
        for i in range(54):
            tans[a[i]-1] = ans[i]
        ans = tans
    print(*ans)


if __name__ == "__main__":
    solve()

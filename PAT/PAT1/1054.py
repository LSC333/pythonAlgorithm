# -*- coding: utf-8 -*- 
# @Time : 2019/6/10 18:46 
# @Author : ValarMorghulis 
# @File : 1054.py
def solve():
    m, n = map(int, input().split())
    ans, cnt = -1, 0
    for i in range(n):
        t = list(map(int, input().split()))
        for j in range(m):
            if ans != t[j]:
                if cnt == 0:
                    ans = t[j]
                else:
                    cnt -= 1
            else:
                cnt += 1
    print(ans)


if __name__ == "__main__":
    solve()

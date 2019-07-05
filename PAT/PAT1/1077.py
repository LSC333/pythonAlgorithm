# -*- coding: utf-8 -*- 
# @Time : 2019/7/5 12:16 
# @Author : ValarMorghulis 
# @File : 1077.py
def solve():
    n = int(input())
    ans = input()[::-1]
    for i in range(n - 1):
        t = input()[::-1]
        x = 0
        while x < len(ans) and x < len(t) and ans[x] == t[x]:
            x += 1
        ans = ans[:x]
    print("%s" % (ans[::-1] if len(ans) != 0 else "nai"))


if __name__ == "__main__":
    solve()

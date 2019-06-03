# -*- coding: utf-8 -*- 
# @Time : 2019/6/3 18:56 
# @Author : ValarMorghulis 
# @File : 1040.py
def init(s):
    ns = "?#"
    for i in range(len(s)):
        ns = ns + s[i]
        ns = ns + '#'
    ns = ns + "!"
    return ns


def manacher(s):
    res = [1 for i in range(len(s))]
    mx, po = 0, 0
    for i in range(1, len(s)-1):
        if mx > i:
            res[i] = min(mx - i, res[2 * po - i])
        while s[i + res[i]] == s[i - res[i]]:
            res[i] += 1
        if res[i]+i > mx:
            mx, po = i + res[i], i
    return res


def solve():
    s = input()
    s = init(s)
    ls = manacher(s)
    print(max(ls)-1)


if __name__ == "__main__":
    solve()

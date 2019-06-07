# -*- coding: utf-8 -*- 
# @Time : 2019/6/6 18:09 
# @Author : ValarMorghulis 
# @File : 1047.py
def solve():
    n, k = map(int, input().split())
    ans = [[] for i in range(k)]
    for i in range(n):
        line = input().split()
        name, courses = line[0], list(map(int, line[1:]))
        for j in range(1, courses[0] + 1):
            ans[courses[j] - 1].append(name)
    for i in range(k):
        print("%d %d" % (i+1, len(ans[i])))
        ans[i] = sorted(ans[i], key=lambda x: x)
        for j in ans[i]:
            print(j)


if __name__ == "__main__":
    solve()

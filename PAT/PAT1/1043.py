# -*- coding: utf-8 -*- 
# @Time : 2019/6/5 16:06 
# @Author : ValarMorghulis 
# @File : 1043.py
import sys
sys.setrecursionlimit(10000)

tree = list()
flag = True
ans = list()


def find(root, tail):
    global ans
    if root > tail:
        return
    i, j = root + 1, tail
    if flag:
        while i <= tail and tree[i] < tree[root]:
            i += 1
        while j > root and tree[j] >= tree[root]:
            j -= 1
    else:
        while i <= tail and tree[i] >= tree[root]:
            i += 1
        while j > root and tree[j] < tree[root]:
            j -= 1
    if i - j != 1:
        return
    find(root + 1, j)
    find(i, tail)
    ans.append(tree[root])


def solve():
    global tree, flag, ans
    n = int(input())
    tree = list(map(int, input().split()))
    find(0, n - 1)
    if len(ans) != n:
        flag = False
        ans.clear()
        find(0, n - 1)
    if len(ans) == n:
        print("YES")
        print(*ans)
    else:
        print("NO")


if __name__ == "__main__":
    solve()

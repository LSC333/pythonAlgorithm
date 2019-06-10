# -*- coding: utf-8 -*- 
# @Time : 2019/6/10 11:23 
# @Author : ValarMorghulis 
# @File : 1053.py
class node:
    def __init__(self, weight):
        self.weight = weight
        self.child = list()

    def toString(self):
        return "weight:%d\n" % self.weight + str(self.child)


tree = list()
n, m, s = 0, 0, 0
path = list()


def dfs(root, sum):
    global path
    if sum > s:
        return
    if sum == s:
        if tree[root].child:
            return
        for i in range(len(path)):
            print("%d" % path[i], end=('\n' if i == len(path) - 1 else ' '))
        return
    for i in range(len(tree[root].child)):
        path.append(tree[tree[root].child[i]].weight)
        dfs(tree[root].child[i], sum+tree[tree[root].child[i]].weight)
        path.pop()


def solve():
    global n, m, s, tree, path
    n, m, s = map(int, input().split())
    w = list(map(int, input().split()))
    for i in range(n):
        t = node(w[i])
        tree.append(t)
    for i in range(m):
        line = list(map(int, input().split()))
        id = line[0]
        tree[id].child = line[2:]
        tree[id].child = sorted(tree[id].child, key=lambda x: tree[x].weight, reverse=True)
    path.append(tree[0].weight)
    dfs(0, tree[0].weight)


if __name__ == "__main__":
    solve()

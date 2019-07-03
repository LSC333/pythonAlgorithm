# -*- coding: utf-8 -*- 
# @Time : 2019/7/3 15:00 
# @Author : ValarMorghulis 
# @File : 1076.py
class node:
    def __init__(self, id, level):
        self.id = id
        self.level = level


n, l = 0, 0
edge = list()


def bfs(start):
    vis = [False for i in range(n)]
    que = list()
    que.append(start)
    vis[start.id] = True
    cnt = 0
    while que:
        tmp = que.pop(0)
        for i in range(len(edge[tmp.id])):
            if not vis[edge[tmp.id][i]] and tmp.level < l:
                que.append(node(edge[tmp.id][i], tmp.level + 1))
                vis[edge[tmp.id][i]] = True
                cnt += 1
    return cnt


def solve():
    global n, l, edge
    n, l = map(int, input().split())
    edge = [[] for i in range(n)]
    for i in range(n):
        a = list(map(int, input().split()))
        for j in range(1, a[0] + 1):
            edge[a[j] - 1].append(i)
    t = list(map(int, input().split()))
    for i in range(1, t[0] + 1):
        print("%d" % bfs(node(t[i]-1, 0)))


if __name__ == "__main__":
    solve()

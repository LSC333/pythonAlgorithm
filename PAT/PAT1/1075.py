# -*- coding: utf-8 -*- 
# @Time : 2019/7/3 13:33 
# @Author : ValarMorghulis 
# @File : 1075.py
import functools


class node:
    def __init__(self):
        self.id = 100861
        self.rank = -1
        self.tot = 0
        self.score = [-1 for i in range(5)]
        self.show = False
        self.acNum = 0

    def toString(self):
        s = "%d %05d %d" % (self.rank, self.id, self.tot)
        return s


def cmp(a, b):
    if a.tot != b.tot:
        return -1 if a.tot > b.tot else 1
    if a.acNum != b.acNum:
        return -1 if a.acNum > b.acNum else 1
    return -1 if a.id < b.id else 1


def solve():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    users = [node() for i in range(n + 1)]
    for i in range(m):
        userId, problemId, s = map(int, input().split())
        users[userId].id = userId
        users[userId].score[problemId-1] = max(users[userId].score[problemId-1], s)
        if s != -1:
            users[userId].show = True
        elif users[userId].score[problemId-1] == -1:
            users[userId].score[problemId-1] = -2
    for i in range(1, n + 1):
        for j in range(k):
            if users[i].score[j] != -1 and users[i].score[j] != -2:
                users[i].tot += users[i].score[j]
            if users[i].score[j] == a[j]:
                users[i].acNum += 1
    users = sorted(users[1:], key=functools.cmp_to_key(cmp))
    for i in range(n):
        users[i].rank = i + 1
        if i != 0 and users[i].tot == users[i - 1].tot:
            users[i].rank = users[i - 1].rank

    for i in range(n):
        if users[i].show:
            ans = users[i].toString()
            for j in range(k):
                if users[i].score[j] == -1:
                    ans += " -"
                elif users[i].score[j] == -2:
                    ans += " 0"
                else:
                    ans += " %d" % users[i].score[j]
            print(ans)


if __name__ == "__main__":
    solve()

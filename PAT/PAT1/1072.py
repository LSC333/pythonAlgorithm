# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 14:11 
# @Author : ValarMorghulis 
# @File : 1072.py
INF = 0x3f3f3f3f


def solve():
    n, m, k, ds = map(int, input().split())
    edge = [[INF for i in range(n + m + 5)] for j in range(n + m + 5)]
    for i in range(k):
        a, b, c = input().split()
        c = int(c)
        if a[0] == 'G':
            a = n + int(a[1])
        else:
            a = int(a)
        if b[0] == 'G':
            b = n + int(b[1])
        else:
            b = int(b)
        edge[a][b] = edge[b][a] = c
    ansId, ansDis, ansAvg = -1, -1, INF
    for i in range(n + 1, n + m + 1):
        minDis, avg = INF, 0
        dis = [INF for i in range(n + m + 5)]
        vis = [False for i in range(n + m + 5)]
        dis[i] = 0
        for j in range(n + m):
            mark, md = -1, INF
            for x in range(1, n + m + 1):
                if not vis[x] and dis[x] < md:
                    mark, md = x, dis[x]
            if mark == -1:
                break
            vis[mark] = True
            for x in range(1, n + m + 1):
                if not vis[x] and dis[x] > dis[mark] + edge[mark][x]:
                    dis[x] = dis[mark] + edge[mark][x]
        for j in range(1, n + 1):
            if dis[j] > ds:
                minDis = -1
                break
            if dis[j] < minDis:
                minDis = dis[j]
            avg += dis[j]
        if minDis == -1:
            continue
        avg /= n
        if minDis > ansDis:
            ansId, ansDis, ansAvg = i, minDis, avg
        elif minDis == ansDis and ansAvg > avg:
            ansId, ansAvg = i, avg
    if ansId == -1:
        print("No Solution")
    else:
        print("G%d\n%.1f %.1f" % (ansId-n, ansDis, ansAvg))


if __name__ == "__main__":
    solve()

INF = 0xffffffff
n, m, c1, c2 = map(int, input().split())
weight = list(map(int, input().split()))
value = [INF for i in range(n)]
value[c1] = weight[c1]
dis = [INF for i in range(n)]
dis[c1] = 0
num = [0] * n
num[c1] = 1
vis = [False for i in range(n)]
edge = [[INF for i in range(n)] for j in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    edge[a][b] = edge[b][a] = c
for i in range(n):
    mark = -1
    minn = INF
    for j in range(n):
        if vis[j] == False and dis[j] < minn:
            mark = j
            minn = dis[j]
    if mark == -1 or mark == c2:
        break
    vis[mark] = True
    for j in range(n):
        if vis[j] == False and edge[mark][j] != INF:
            if dis[mark] + edge[mark][j] < dis[j]:
                dis[j] = dis[mark] + edge[mark][j]
                num[j] = num[mark]
                value[j] = value[mark] + weight[j]
            elif dis[mark] + edge[mark][j] == dis[j]:
                num[j] = num[j] + num[mark]
                if value[mark] + weight[j] > value[j]:
                    value[j] = value[mark] + weight[j]
print("%d %d" % (num[c2], value[c2]))

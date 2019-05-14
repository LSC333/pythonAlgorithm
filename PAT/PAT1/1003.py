INF = 0xffffffff    #无穷大
n, m, c1, c2 = map(int, input().split())
weight = list(map(int, input().split()))
value = [INF for i in range(n)]
value[c1] = weight[c1]
dis = [INF for i in range(n)]
dis[c1] = 0    #将起点与起点的距离设为0
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
    for j in range(n):   #找出当前距离起点最近的点
        if vis[j] == False and dis[j] < minn:
            mark = j
            minn = dis[j]
    if mark == -1 or mark == c2:   #如果没找到或者找到的点是终点
        break
    vis[mark] = True    #将找到的点标记为已访问
    for j in range(n):
        if vis[j] == False and edge[mark][j] != INF:   #如果点没有访问过并且标记的点和这个点之间有边
            if dis[mark] + edge[mark][j] < dis[j]:
                dis[j] = dis[mark] + edge[mark][j]
                num[j] = num[mark]
                value[j] = value[mark] + weight[j]
            elif dis[mark] + edge[mark][j] == dis[j]:
                num[j] = num[j] + num[mark]
                if value[mark] + weight[j] > value[j]:
                    value[j] = value[mark] + weight[j]
print("%d %d" % (num[c2], value[c2]))

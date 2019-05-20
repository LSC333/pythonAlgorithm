INF = 0xffffffff
cmax, n, sp, m = 0, 0, 0, 0
edge = list()   #存放边
minneed, minback = INF, INF #最小的携带量和拿走量
pre = list()    #存放每个点的前驱
dis = list()    #存放每个点到PBMC的距离
weight = list() #存放每个点的车的数量-cmax//2
ans, temp = list(), list()  #符合要求的路径，临时路径


def dfs(node):
    global temp, weight, pre, minneed, minback, ans
    temp.append(node)
    if node == 0:   #表示已经找到一条最短路径
        need, back = 0, 0
        for i in range(len(temp) - 2, -1, -1):
            if weight[temp[i] - 1] > 0:
                back += weight[temp[i] - 1]
            else:
                if weight[temp[i] - 1] + back >= 0:
                    back += weight[temp[i] - 1]
                else:
                    need = need - (back + weight[temp[i] - 1])
                    back = 0
        if need < minneed:  #更新要求的路径
            minneed = need
            minback = back
            ans = list(temp)
        elif need == minneed and back < minback:
            minback = back
            ans = list(temp)
        temp.pop()
        return
    else:
        for i in range(len(pre[node])):
            dfs(pre[node][i])
    temp.pop()
    return


def solve():
    global cmax, n, sp, m, weight, dis, pre, minneed, minback, ans
    cmax, n, sp, m = map(int, input().split())
    vis = [False for i in range(n + 1)]
    edge = [[INF for i in range(n + 1)] for j in range(n + 1)]
    weight = list(map(int, input().split()))
    for i in range(n):
        weight[i] = weight[i] - cmax // 2   #方便计算和判断
    for i in range(m):
        a, b, c = map(int, input().split())
        edge[a][b] = edge[b][a] = c
    dis = [INF for i in range(n + 1)]
    dis[0] = 0
    pre = [[] for i in range(n + 1)]
    for i in range(n + 1):  #dijkstra找最短路径和路径的前驱
        mark, mindis = -1, INF
        for j in range(n + 1):
            if (not vis[j]) and dis[j] < mindis:
                mark = j
                mindis = dis[j]
        if mark == -1:
            break
        vis[mark] = True
        for j in range(n + 1):
            if not vis[j]:
                if dis[mark] + edge[mark][j] < dis[j]:
                    dis[j] = dis[mark] + edge[mark][j]
                    pre[j].clear()
                    pre[j].append(mark)
                elif dis[mark] + edge[mark][j] == dis[j]:
                    pre[j].append(mark)
    dfs(sp)
    print("%d 0" % minneed, end="")
    for i in range(len(ans) - 2, -1, -1):
        print("->%d" % ans[i], end="")
    print(" %d" % minback)


if __name__ == "__main__":
    solve()

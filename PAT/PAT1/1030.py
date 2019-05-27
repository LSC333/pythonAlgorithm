def solve():
    INF = 0x7fffffff
    n, m, s, d = map(int, input().split())
    cost = [INF for i in range(n)]
    vis = [False for i in range(n)]
    edge = [[[-1, -1] for i in range(n)] for j in range(n)]
    dis = [INF for i in range(n)]
    path = [[] for i in range(n)]
    for i in range(m):
        a, b, D, c = map(int, input().split())
        edge[a][b], edge[b][a] = [D, c], [D, c]
    path[s] = [s]
    vis[s] = True
    dis[s], cost[s] = 0, 0
    mark = s
    while mark != -1:
        indexOfEdge = [i for i in range(n) if edge[mark][i] != [-1, -1] and not vis[i]]
        for i in indexOfEdge:
            if dis[mark] + edge[mark][i][0] < dis[i]:
                dis[i] = dis[mark] + edge[mark][i][0]
                cost[i] = cost[mark] + edge[mark][i][1]
                path[i] = path[mark]+[i]
            elif dis[mark] + edge[mark][i][0] == dis[i]:
                if cost[i] > cost[mark] + edge[mark][i][1]:
                    path[i] = path[mark]+[i]
                    cost[i] = cost[mark] + edge[mark][i][1]
        tmp = [i for i in range(n) if dis[i] != INF and not vis[i]]
        if len(tmp) == 0:
            mark = -1
        else:
            mark = sorted(tmp, key=lambda x: dis[x])[0]
            vis[mark] = True
    print(*path[d], dis[d], cost[d])


if __name__ == "__main__":
    solve()

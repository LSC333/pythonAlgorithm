def dfs(node):
    global n, m, k, edge, city
    city[node] = True
    for i in range(n):
        if edge[node][i] and (not city[i]):
            dfs(i)


n, m, k = 0, 0, 0
edge = list()  #城市之间是否连通
city = list()  #城市是否访问过


def solve():
    global n, m, k, edge, city
    n, m, k = map(int, input().split())
    edge = [[False for i in range(n)] for j in range(n)]
    for i in range(m):
        c1, c2 = map(int, input().split())
        edge[c1 - 1][c2 - 1] = edge[c2 - 1][c1 - 1] = True
    check = list(map(int, input().split()))
    for i in range(k):
        cnt = 0  #连通分量
        city = [False for j in range(n)]
        city[check[i] - 1] = True  #将自己排除
        for j in range(n):
            if not city[j]:
                dfs(j)   #dfs将连通的城市都访问一遍
                cnt += 1
        print(cnt - 1)


if __name__ == "__main__":
    solve()

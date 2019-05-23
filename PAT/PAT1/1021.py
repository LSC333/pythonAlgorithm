n = 0
edge = list()  # 邻接表存放图
vis = list()  # 判断节点是否访问过
maxDepth = 0  # 最大深度
root = list()  # 暂存的根节点


def dfs(node, d):
    global maxDepth, root, vis
    if d > maxDepth:  # 判断当前深度是否大于最大深度
        maxDepth = d
        root.clear()
        root.append(node)
    elif d == maxDepth:  # 如果当前深度等于最大深度
        root.append(node)
    vis[node] = True
    for i in edge[node]:
        if not vis[i]:
            dfs(i, d + 1)


def solve():
    global n, edge, root, vis
    n = eval(input())
    edge = [[] for i in range(n + 1)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)
    vis = [False for i in range(n + 1)]
    k = 0  # 连通分量
    s = 0
    ans = [False for i in range(n + 1)]  # 桶排序
    for i in range(1, n + 1):
        if not vis[i]:
            k += 1
            dfs(i, 1)
            if i == 1:
                if len(root):
                    s = root[0]
                for j in root:
                    ans[j] = True
    if k >= 2:
        print("Error: %d components" % k)
    else:
        vis = [False for i in range(n + 1)]
        dfs(s, 1)
        for i in root:
            ans[i] = True
        for i in range(1, len(ans)):
            if ans[i]:
                print(i)


if __name__ == "__main__":
    solve()

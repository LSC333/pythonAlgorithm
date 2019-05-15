def dfs(cnt, node):
    if num[cnt] == -1:  #这层还没到达过
        num[cnt] = 0
    if grep[node][node] != -2:  #当前node节点没有孩子
        num[cnt] += 1
        return
    for i in range(n + 1):  #遍历node节点的每个孩子
        if grep[node][i] == 1:
            dfs(cnt + 1, i)
    return


line = input()
if line == '' or len(line.split()) == 1:
    exit(0)
n, m = map(int, line.split())
if n == 0:
    exit(0)
num = [-1 for i in range(101)]  #存放每层的叶子节点数量
grep = [[-1 for i in range(n + 2)] for j in range(n + 2)]   #存放这棵树
for i in range(m):
    tmp = [int(x) for x in input().split()]
    fa = tmp[0]
    grep[fa][fa] = -2   #如果是非叶子节点将其标记为-2
    for j in range(tmp[1]):
        grep[fa][tmp[j + 2]] = 1
dfs(0, 1)
for i in range(101):
    if num[i] == -1:
        break
    print(num[i], end=('\n' if num[i + 1] == -1 else ' '))
exit(0)

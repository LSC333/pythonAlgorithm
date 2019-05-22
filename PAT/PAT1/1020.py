class node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None


n = 0
postOrder = list()
inOrder = list()


def findFather(a, b, c, d):
    root = node(-1)
    if a == b:  #找到叶子节点了
        root.num = inOrder[a]
        return root
    marki = -1  #标记根节点在后序中的下标
    markj = -1  #标记根节点在中序中的下标
    for i in range(d, c - 1, -1):
        if marki != -1:
            break
        for j in range(a, b + 1):
            if inOrder[j] == postOrder[i]:
                marki = i
                markj = j
                root.num = inOrder[j]
                break
    if markj == a:  #如果根节点没有左子树
        root.right = findFather(markj + 1, b, c, marki - 1)
        return root
    if markj == b:  #如果根节点没有右子树
        root.left = findFather(a, markj - 1, c, marki - 1)
        return root
    root.left = findFather(a, markj - 1, c, marki - 1)
    root.right = findFather(markj + 1, b, c, marki - 1)
    return root


def levelOrder(root):   #层次遍历保存结果
    que = list()
    ans = list()
    que.append(root)
    while que:
        a = que[0]
        que.pop(0)
        ans.append(a.num)
        if a.left:
            que.append(a.left)
        if a.right:
            que.append(a.right)
    return ans


def solve():
    global n, postOrder, inOrder
    n = map(int, input().split())
    postOrder = list(map(int, input().split()))
    inOrder = list(map(int, input().split()))
    root = findFather(0, len(inOrder) - 1, 0, len(postOrder) - 1)
    res = levelOrder(root)
    for i in range(len(res)):
        print("%d" % res[i], end=('\n' if i == len(res) - 1 else ' '))


if __name__ == "__main__":
    solve()

# -*- coding: utf-8 -*- 
# @Time : 2019/6/26 14:45 
# @Author : ValarMorghulis 
# @File : 1066.py
class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def getHeight(root):
    if root is None:
        return 0
    return max(getHeight(root.left), getHeight(root.right)) + 1


def leftRotate(root):
    t = root.right
    root.right = t.left
    t.left = root
    return t


def rightRotate(root):
    t = root.left
    root.left = t.right
    t.right = root
    return t


def leftRightRotate(root):
    root.left = leftRotate(root.left)
    return rightRotate(root)


def rightLeftRotate(root):
    root.right = rightRotate(root.right)
    return leftRotate(root)


def insert(root, val):
    if root is None:
        root = node(val)
    elif val < root.val:
        root.left = insert(root.left, val)
        if getHeight(root.left) - getHeight(root.right) == 2:
            root = rightRotate(root) if val < root.left.val else leftRightRotate(root)
    else:
        root.right = insert(root.right, val)
        if getHeight(root.right) - getHeight(root.left) == 2:
            root = leftRotate(root) if val > root.right.val else rightLeftRotate(root)
    return root


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    root = None
    for i in range(n):
        root = insert(root, a[i])
    print(root.val)


if __name__ == "__main__":
    solve()

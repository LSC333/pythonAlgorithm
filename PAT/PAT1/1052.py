# -*- coding: utf-8 -*- 
# @Time : 2019/6/9 18:01 
# @Author : ValarMorghulis 
# @File : 1052.py
def solve():
    nodes = list()
    dic = dict()
    n, head = map(int, input().split())
    for i in range(n):
        address, key, nex = map(int, input().split())
        dic[address] = [key, nex]
    while head != -1:
        nodes.append([head, dic[head][0]])
        head = dic[head][1]
    nodes = sorted(nodes, key=lambda x: x[1])
    if len(nodes)==0:
        print("0 -1")
    else:
        print("%d %05d" % (len(nodes), nodes[0][0]))
        for i in range(len(nodes)):
            print("%05d %d" % (nodes[i][0], nodes[i][1]), end=' ')
            if i == len(nodes) - 1:
                print("-1")
            else:
                print("%05d" % nodes[i + 1][0])

        nodes = sorted(nodes, key=lambda x: x[1])


if __name__ == "__main__":
    solve()

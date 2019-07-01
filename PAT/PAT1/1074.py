# -*- coding: utf-8 -*- 
# @Time : 2019/7/1 10:01 
# @Author : ValarMorghulis 
# @File : 1074.py
def solve():
    firstAddress, n, k = map(int, input().split())
    data = [-1 for i in range(100861)]
    next = [-1 for i in range(100861)]
    for i in range(n):
        address, d, ne = map(int, input().split())
        data[address] = d
        next[address] = ne
    tmpNext = list()
    ansNext = list()
    cnt = 0
    while firstAddress != -1:
        tmpNext.append(firstAddress)
        ansNext.append(firstAddress)
        cnt += 1
        firstAddress = next[firstAddress]
    for i in range(cnt - cnt % k):
        ansNext[i] = tmpNext[i // k * k + k - i % k - 1]
    for i in range(cnt - 1):
        print("%05d %d %05d" % (ansNext[i], data[ansNext[i]], ansNext[i + 1]))
    print("%05d %d -1" % (ansNext[cnt - 1], data[ansNext[cnt - 1]]))


if __name__ == "__main__":
    solve()

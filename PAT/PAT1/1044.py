# -*- coding: utf-8 -*- 
# @Time : 2019/6/5 18:56 
# @Author : ValarMorghulis 
# @File : 1044.py
n, m = 0, 0
sum = list()


def search(i):
    left, right = i, n
    while left < right:
        mid = (left + right) // 2
        if sum[mid]-sum[i-1] >= m:
            right = mid
        else:
            left = mid + 1
    return right, sum[right] - sum[i - 1]


def solve():
    global n, m, sum
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a
    sum = [0 for i in range(n + 5)]
    for i in range(1, n + 1):
        sum[i] = a[i]
        sum[i] += sum[i - 1]
    ans = list()
    minsum = sum[n]
    for i in range(1, n + 1):
        t, tmpsum = search(i)
        if tmpsum > minsum:
            continue
        if tmpsum >= m:
            if tmpsum < minsum:
                ans.clear()
                minsum = tmpsum
            ans.append([i, t])
    for i in range(0, len(ans)):
        print("%d-%d" % (ans[i][0], ans[i][1]))


if __name__ == "__main__":
    solve()

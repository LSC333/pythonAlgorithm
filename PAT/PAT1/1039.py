# -*- coding: utf-8 -*- 
# @Time : 2019/6/2 16:20 
# @Author : ValarMorghulis 
# @File : 1039.py
def solve():
    n, k = map(int, input().split())
    dic = dict()
    for i in range(k):
        course, num = map(int, input().split())
        if num > 0:
            names = input().split()
            for name in names:
                if name not in dic.keys():
                    dic[name] = list()
                dic[name].append(course)
    query = input().split()
    for i in range(n):
        if query[i] not in dic:
            print(query[i] + ' 0')
            continue
        tmp = sorted(dic[query[i]])
        print("%s %d" % (query[i], len(tmp)), end=' ')
        for j in range(len(tmp)):
            print(tmp[j], end=('\n' if j == len(tmp) - 1 else ' '))


if __name__ == "__main__":
    solve()

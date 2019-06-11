# -*- coding: utf-8 -*- 
# @Time : 2019/6/11 19:31 
# @Author : ValarMorghulis 
# @File : 1056.py
def solve():
    np, ng = map(int, input().split())
    mice = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = [0 for i in range(np)]
    while len(a) > 1:
        rank = len(a) // ng + 1
        if len(a) % ng:
            rank += 1
        tmp = list()
        num = 0
        while num < len(a):
            m, index, i = -1, 0, 0
            while num < len(a):
                if i < ng:
                    i += 1
                    ans[a[num]] = rank
                    if mice[a[num]] > m:
                        m = mice[a[num]]
                        index = a[num]
                else:
                    break
                num += 1
            tmp.append(index)
        a = tmp
    ans[a[0]] = 1
    print(*ans)


if __name__ == "__main__":
    solve()

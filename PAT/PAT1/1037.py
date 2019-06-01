# -*- coding: utf-8 -*- 
# @Time : 2019/6/1 10:05 
# @Author : ValarMorghulis 
# @File : 1037.py
def solve():
    n1 = eval(input())
    a = list(map(int, input().split()))
    pa = list()
    na = list()
    for i in a:
        if i < 0:
            na.append(i)
        if i > 0:
            pa.append(i)
    n2 = eval(input())
    b = list(map(int, input().split()))
    pb = list()
    nb = list()
    for i in b:
        if i < 0:
            nb.append(i)
        if i > 0:
            pb.append(i)
    ans = 0
    pa = sorted(pa, reverse=True)
    na = sorted(na)
    pb = sorted(pb, reverse=True)
    nb = sorted(nb)
    for i in range(min(len(pa), len(pb))):
        ans = ans + pa[i] * pb[i]
    for i in range(min(len(na), len(nb))):
        ans = ans + na[i] * nb[i]

    print(ans)


if __name__ == "__main__":
    solve()

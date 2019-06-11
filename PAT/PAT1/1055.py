# -*- coding: utf-8 -*- 
# @Time : 2019/6/11 10:32 
# @Author : ValarMorghulis 
# @File : 1055.py
import functools


class node:
    def __init__(self, name, age, worth):
        self.name = name
        self.age = age
        self.worth = worth

    def toString(self):
        return "%s %d %d" % (self.name, self.age, self.worth)


def cmp(a, b):
    if a.worth != b.worth:
        return -1 if a.worth > b.worth else 1
    elif a.age != b.age:
        return -1 if a.age < b.age else 1
    else:
        return -1 if a.name < b.name else 1


def solve():
    n, k = map(int, input().split())
    tot = list()
    for i in range(n):
        name, age, worth = input().split()
        tot.append(node(name, int(age), int(worth)))
    tot.sort(key=functools.cmp_to_key(cmp))
    person = list()
    ageOfAll = [0 for i in range(211)]
    for i in range(n):
        if ageOfAll[tot[i].age] < 100:
            person.append(tot[i])
            ageOfAll[tot[i].age] += 1
    for i in range(k):
        m, aMin, aMax = map(int, input().split())
        ans = list()
        for j in person:
            if aMin <= j.age <= aMax:
                ans.append(j)
        ans=ans[0:m]
        print("Case #%d:" % (i + 1))
        if ans:
            for j in ans:
                print(j.toString())
        else:
            print("None")


if __name__ == "__main__":
    solve()

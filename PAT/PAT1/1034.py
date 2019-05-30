# -*- coding: utf-8 -*- 
# @Time : 2019/5/30 16:13 
# @Author : ValarMorghulis 
# @File : 1034.py
class person:
    def __init__(self, name, total):
        self.name = name
        self.total = total
        self.link = []


def bfs(persons):
    global result
    while len(persons) > 0:
        temp, t = [], []
        start = [list(persons.keys())[0]]
        temp += start
        while len(start) > 0:
            for x in start:
                for i in persons[x].link:
                    if i not in temp and i not in t:
                        t.append(i)
            start, t = t, []
            temp += start
        a = max([[persons[x].total, x] for x in temp])
        sums = 0
        for x in temp:
            sums += persons[x].total
        result.append([a[1], len(temp), sums / 2])
        for x in temp:
            persons.pop(x)


result = list()


def solve():
    global result
    result = list()
    line = input().split(" ")
    n, limit = int(line[0]), int(line[1])
    persons = {}
    for x in range(n):
        line = input().split(" ")
        first, second = line[0], line[1]
        m = int(line[2])
        try:
            persons[first].total += m
            if second not in persons[first].link:
                persons[first].link.append(second)
        except:
            p = person(first, m)
            persons[first] = p
            persons[first].link.append(second)
        try:
            persons[second].total += m
            if first not in persons[second].link:
                persons[second].link.append(first)
        except:
            p = person(second, m)
            persons[second] = p
            persons[second].link.append(first)
    bfs(persons)
    result = sorted([x for x in result if x[1] > 2 and x[2] > limit])
    print(len(result))
    for x in result:
        print(x[0], x[1])


if __name__ == "__main__":
    solve()

# -*- coding: utf-8 -*- 
# @Time : 2019/6/24 13:57 
# @Author : ValarMorghulis 
# @File : 1062.py
import functools


class node:
    def __init__(self, id, virtue, talent, tot, category):
        self.id = id
        self.virtue = virtue
        self.talent = talent
        self.tot = tot
        self.category = category

    def toString(self):
        return "%s %d %d" % (self.id, self.virtue, self.talent)


def cmp(a, b):
    if a.category != b.category:
        return -1 if a.category < b.category else 1
    if a.tot != b.tot:
        return -1 if a.tot > b.tot else 1
    if a.virtue != b.virtue:
        return -1 if a.virtue > b.virtue else 1
    return -1 if a.id < b.id else 1


def solve():
    n, low, high = map(int, input().split())
    a = list()
    for i in range(n):
        id, virtue, talent = input().split()
        virtue, talent = int(virtue), int(talent)
        if virtue >= low and talent >= low:
            if virtue >= high and talent >= high:
                a.append(node(id, virtue, talent, virtue + talent, 1))
            elif virtue >= high > talent:
                a.append(node(id, virtue, talent, virtue + talent, 2))
            elif high > virtue >= talent and talent < high:
                a.append(node(id, virtue, talent, virtue + talent, 3))
            else:
                a.append(node(id, virtue, talent, virtue + talent, 4))
    a=sorted(a, key=functools.cmp_to_key(cmp))
    print(len(a))
    for i in a:
        print(i.toString())


if __name__ == "__main__":
    solve()

# -*- coding: utf-8 -*- 
# @Time : 2019/5/29 18:52 
# @Author : ValarMorghulis 
# @File : 1033.py
def solve():
    capacity, distance, per, total = map(float, input().split())
    total = int(total)
    stations = list()
    flag = False  # 表示起点是否有加油站
    for i in range(total):
        price, length = map(float, input().split())
        if length == 0.0:
            flag = True
        stations.append([length, price])
    if not flag:
        print("The maximum travel distance = 0.00")
        return
    stations = sorted(stations, key=lambda x: x[0])
    finalPrice = stations[-1][1]
    stations.append([distance, finalPrice])  # 将终点设一个加油站，油价就为它前一个的油价
    pos, cost, now = 0, 0.0, 0.0  # 当前站，花费，当前油量
    while pos < len(stations) - 1:  # 如果当前不是终点
        maxDis = capacity * per + stations[pos][0]  # 计算当前能走的最大距离
        arr = [x for x in range(pos + 1, len(stations)) if stations[pos][0] < stations[x][0] <= maxDis]  # 找出可达的站
        if len(arr) == 0:  # 如果都不可达说明终点不可达
            print("The maximum travel distance = %.2f" % maxDis)
            return
        mark = pos  # 标记下一个应去的站
        nearTheEnd = False  # 终点是否可达
        for i in arr:
            if stations[i][0] == distance:
                nearTheEnd = True
            if stations[i][1] <= stations[mark][1]:
                mark = i
                break
        if mark != pos:
            cost = cost + ((stations[mark][0] - stations[pos][0]) / per - now) * stations[pos][1]
            now = 0
            pos = mark
        else:
            if nearTheEnd:
                cost = cost + ((distance - stations[pos][0]) / per - now) * stations[pos][1]
                pos = len(stations) - 1
                now = 0
            else:
                cost = cost + (capacity - now) * stations[pos][1]
                mark += 1
                for i in arr:
                    if stations[i][1] <= stations[mark][1]:
                        mark = i
                now = capacity - (stations[mark][0] - stations[pos][0]) / per
                pos = mark
    print("%.2f" % cost)


if __name__ == "__main__":
    solve()

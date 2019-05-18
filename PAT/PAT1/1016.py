import functools


class phoneCall:    #保存通话记录
    def __init__(self, name, month, day, hour, minute, stat):
        self.name = name
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.stat = stat
        self.time = day * 24 * 60 + hour * 60 + minute

    def getDate(self):  #为了输出方便，就定义了一个获取日期的函数
        return "%02d:%02d:%02d" % (self.day, self.hour, self.minute)


def myCmp(pa, pb):  #自定义的排序规则
    if pa.name != pb.name:  #先按照姓名排序
        if pa.name < pb.name:
            return -1
        if pa.name > pb.name:
            return 1
    else:   #如果姓名相同就按照时间先后排序
        if pa.time < pb.time:
            return -1
        if pa.time > pb.time:
            return 1
        return 0


def bill(pC, rate): #计算账单（以00:00:00为开始时间）
    res = rate[pC.hour] * pC.minute + rate[24] * 60 * pC.day
    for i in range(pC.hour):
        res += rate[i] * 60
    return res / 100    #换成美元


def solve():
    rate = list(map(int, input().split()))  #存储每小时的费率
    rate.append(sum(rate))
    n = int(input())
    phoneCalls = list()
    for i in range(n):
        name, date, stat = input().split()
        month, day, hour, minute = list(map(int, date.split(':')))
        phoneCalls.append(phoneCall(name, month, day, hour, minute, stat == "on-line"))
    phoneCalls.sort(key=functools.cmp_to_key(myCmp))    #排序使用key=functools.cmp_to_key(myCmp)
    tpC = dict()    #存放配对成功的通话记录
    for i in range(1, n):
        if phoneCalls[i].name == phoneCalls[i - 1].name and phoneCalls[i - 1].stat and not phoneCalls[i].stat:
            if phoneCalls[i - 1].name in tpC:
                tpC[phoneCalls[i - 1].name].append(phoneCalls[i - 1])
                tpC[phoneCalls[i].name].append(phoneCalls[i])
            else:
                tpC[phoneCalls[i - 1].name] = list()
                tpC[phoneCalls[i - 1].name].append(phoneCalls[i - 1])
                tpC[phoneCalls[i].name].append(phoneCalls[i])
    for key, value in tpC.items():
        print("%s %02d" % (key, value[0].month))
        tot = 0.0   #本月总费用
        for i in range(1, len(value), 2):
            t = bill(value[i], rate) - bill(value[i - 1], rate)
            print("%s %s %d $%.2f" % (value[i - 1].getDate(), value[i].getDate(),
                                      value[i].time - value[i - 1].time, t))
            tot += t
        print("Total amount: $%.2f" % tot)


if __name__ == "__main__":
    solve()

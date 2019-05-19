import functools


class customer:
    def __init__(self, arr, pro):
        self.arr = arr  #顾客的到达时间
        self.pro = pro  #顾客的处理业务时间

    def toString(self):
        return "%d %d" % (self.arr, self.pro)


def cmp(a, b):  #自定义的比较函数
    if a.arr < b.arr:
        return -1
    if a.arr > b.arr:
        return 1
    return 0


def solve():
    n, k = map(int, input().split())
    customers = list()
    for i in range(n):
        time, pro = input().split()
        pro = int(pro)
        hour, minute, second = map(int, time.split(':'))
        arr = hour * 3600 + minute * 60 + second
        if arr > 61200: #晚于17:00就剔除
            continue
        customers.append(customer(arr, pro*60))
    customers.sort(key=functools.cmp_to_key(cmp))   #排序
    windows = [28800 for i in range(k)] #窗口开始的时间是8:00
    ans = 0.0
    for i in range(len(customers)):
        t = 0
        for j in range(k):  #找出最先空闲的窗口
            if windows[t] > windows[j]:
                t = j
        if windows[t] <= customers[i].arr:  #窗口在顾客来之前就空闲了
            windows[t] = customers[i].arr + customers[i].pro
        else:
            ans = ans + windows[t] - customers[i].arr
            windows[t] += customers[i].pro
    if len(customers) == 0: #如果没有可被服务的顾客输出0.0
        print("0.0")
    else:
        print("%.1f" % (ans / 60 / len(customers)))


if __name__ == "__main__":
    solve()

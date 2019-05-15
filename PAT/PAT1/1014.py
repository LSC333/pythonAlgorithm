class window:
    def __init__(self):
        self.firstTime = 0  #窗口第一个人处理完的时间
        self.lastTime = 0   #窗口最后一个人处理完的时间
        self.que = list()   #窗口前的队列


def solve():
    n, m, k, q = map(int, input().split())
    time = list(map(int, input().split()))
    windows = [window() for i in range(k)]
    ans = [0 for i in range(k)]
    pos = 0 #处理的顾客的编号
    for i in range(m):       #处理前M*N个顾客
        for j in range(n):
            if pos < k:   #判断是否已经处理完所有顾客
                windows[j].que.append(time[pos])
                ans[pos] = (-1 if windows[j].lastTime >= 540 else windows[j].lastTime + time[pos])
                #求这个顾客处理完的时间，如果他开始处理的时候就已经在17:00之后就设为-1
                windows[j].lastTime += time[pos]
                if i == 0:
                    windows[j].firstTime = windows[j].lastTime
                pos += 1
    while pos < k:
        minWindow = 0
        minTime = windows[minWindow].firstTime
        for i in range(n):  #找出所有窗口中最先处理完的那个
            if minTime > windows[i].firstTime:
                minTime = windows[i].firstTime
                minWindow = i
        windows[minWindow].que.pop(0)
        windows[minWindow].firstTime += windows[minWindow].que[0]
        windows[minWindow].que.append(time[pos])
        ans[pos] = (-1 if windows[minWindow].lastTime >= 540 else windows[minWindow].lastTime + time[pos])
        windows[minWindow].lastTime += time[pos]
        pos += 1
    lq = list(map(int, input().split()))
    for i in range(q):
        if ans[lq[i] - 1] == -1:    #如果是-1则表示要输出Sorry
            print("Sorry")
        else:
            print("%02d:%02d" % ((8 + ans[lq[i] - 1] // 60), ans[lq[i] - 1] % 60))


if __name__ == "__main__":
    solve()

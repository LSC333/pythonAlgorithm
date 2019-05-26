import functools
import decimal

decimal.getcontext().rounding = "ROUND_HALF_UP"


class player:
    def __init__(self, arrive, time, isVIP):
        self.arrive = arrive
        self.time = time
        self.isVIP = isVIP
        self.start = -1

    def toString(self):
        a=decimal.Decimal(str(self.start))
        b=decimal.Decimal(str(self.arrive))
        t = decimal.Decimal((a-b)/60)
        rt = decimal.Decimal(str(t)).quantize(decimal.Decimal("0"))
        return '%02d:%02d:%02d %02d:%02d:%02d %.0f' % \
               (self.arrive // 3600, self.arrive % 3600 // 60, self.arrive % 60,
                self.start // 3500, self.start % 3600 // 60, self.start % 60,
                rt)


class table:
    def __init__(self):
        self.end = 8 * 3600
        self.num = 0
        self.isVIP = False

    def toString(self):
        return '%d %d %s' % (self.end, self.num, str(self.isVIP))


players = list()
tables = list()


def playerToTable(playerId, tableId):
    global players, tables
    players[playerId].start = max(players[playerId].arrive, tables[tableId].end)
    tables[tableId].end = players[playerId].start + players[playerId].time
    tables[tableId].num += 1


def findVip(VIPId):
    VIPId += 1
    while VIPId < len(players) and not players[VIPId].isVIP:
        VIPId += 1
    return VIPId


def cmpArrive(a, b):
    return -1 if a.arrive < b.arrive else (1 if a.arrive != b.arrive else 0)


def cmpStart(a, b):
    return -1 if a.start < b.start else (1 if a.start != b.start else 0)


def solve():
    global players, tables
    n = eval(input())
    for i in range(n):
        t, time, isVIP = input().split()
        hour, minute, second = t.split(':')
        time = int(time)
        time = min(time * 60, 2 * 3600)
        isVIP = int(isVIP)
        arrive = int(hour) * 3600 + int(minute) * 60 + int(second)
        if arrive >= 21 * 3600:
            continue
        tmpPlayer = player(arrive, time, True if isVIP == 1 else False)
        tmpPlayer.start = 21 * 3600
        players.append(tmpPlayer)
    k, m = map(int, input().split())
    for i in range(k + 1):
        tables.append(table())
    for i in range(m):
        VIPTable = eval(input())
        tables[VIPTable].isVIP = True
    players.sort(key=functools.cmp_to_key(cmpArrive))
    mark, VIPId = 0, -1
    VIPId = findVip(VIPId)
    while mark < len(players):
        index, minEnd = -1, 999999999
        for i in range(1, k + 1):
            if tables[i].end < minEnd:
                minEnd = tables[i].end
                index = i
        if tables[index].end >= 21 * 3600:
            break
        if players[mark].isVIP and mark < VIPId:
            mark += 1
            continue
        if tables[index].isVIP:
            if players[mark].isVIP:
                playerToTable(mark, index)
                if VIPId == mark:
                    VIPId = findVip(VIPId)
                mark += 1
            else:
                if VIPId < len(players) and players[VIPId].arrive <= tables[index].end:
                    playerToTable(VIPId, index)
                    VIPId = findVip(VIPId)
                else:
                    playerToTable(mark, index)
                    mark += 1
        else:
            if not players[mark].isVIP:
                playerToTable(mark, index)
                mark += 1
            else:
                VIPIndex, minVIPEnd = -1, 999999999
                for i in range(1, k + 1):
                    if tables[i].isVIP and tables[i].end < minVIPEnd:
                        minVIPEnd = tables[i].end
                        VIPIndex = i
                if VIPIndex != -1 and players[mark].arrive >= tables[VIPIndex].end:
                    playerToTable(mark, VIPIndex)
                    if VIPId == mark:
                        VIPId = findVip(VIPId)
                    mark += 1
                else:
                    playerToTable(mark, index)
                    if VIPId == mark:
                        VIPId = findVip(VIPId)
                    mark += 1
    players.sort(key=functools.cmp_to_key(cmpStart))
    for i in players:
        if i.start >= 21 * 3600:
            continue
        print(i.toString())
    for i in range(1, k + 1):
        print("%d" % tables[i].num, end=('\n' if i == k else ' '))


if __name__ == "__main__":
    solve()

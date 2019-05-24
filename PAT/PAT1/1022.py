def solve():
    n = eval(input())
    dictTitle = dict()
    dictAuthor = dict()
    dictKey = dict()
    dictPublisher = dict()
    dictYear = dict()
    for i in range(n):
        id = input()
        title = input()
        author = input()
        keys = input().split()
        publisher = input()
        year = input()
        if title not in dictTitle:
            dictTitle[title] = list()
        dictTitle[title].append(id)
        if author not in dictAuthor:
            dictAuthor[author] = list()
        dictAuthor[author].append(id)
        for key in keys:
            if key not in dictKey:
                dictKey[key] = list()
            dictKey[key].append(id)
        if publisher not in dictPublisher:
            dictPublisher[publisher] = list()
        dictPublisher[publisher].append(id)
        if year not in dictYear:
            dictYear[year] = list()
        dictYear[year].append(id)
    m = eval(input())
    for i in range(m):
        t, ts = input().split(':')
        ts=ts[1:]
        # print(ts)
        if t == "1":
            print("%s: %s" % (t, ts))
            if ts in dictTitle:
                dictTitle[ts].sort()
                for s in dictTitle[ts]:
                    print(s)
            else:
                print("Not Found")
        if t == "2":
            print("%s: %s" % (t, ts))
            if ts in dictAuthor:
                dictAuthor[ts].sort()
                for s in dictAuthor[ts]:
                    print(s)
            else:
                print("Not Found")
        if t == "3":
            print("%s: %s" % (t, ts))
            if ts in dictKey:
                dictKey[ts].sort()
                for s in dictKey[ts]:
                    print(s)
            else:
                print("Not Found")
        if t == "4":
            print("%s: %s" % (t, ts))
            if ts in dictPublisher:
                dictPublisher[ts].sort()
                for s in dictPublisher[ts]:
                    print(s)
            else:
                print("Not Found")
        if t == "5":
            print("%s: %s" % (t, ts))
            if ts in dictYear:
                dictYear[ts].sort()
                for s in dictYear[ts]:
                    print(s)
            else:
                print("Not Found")


if __name__ == "__main__":
    solve()

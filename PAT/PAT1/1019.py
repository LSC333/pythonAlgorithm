def tran(n, d):
    res = list()
    while n:
        res.append(n % d)
        n //= d
    return res[::-1]


def solve():
    n, d = map(int, input().split())
    res = tran(n, d)
    flag = True
    for i in range(len(res)):
        if len(res) - i - 1 >= i:
            if res[i] != res[len(res) - 1 - i]:
                flag = False
                break
    print("Yes" if flag else "No")
    for i in range(len(res)):
        print(res[i], end=("\n" if i == len(res) - 1 else " "))


if __name__ == "__main__":
    solve()

def solve():
    n, c = map(int, input().split())
    ans = list()
    for i in range(n):
        tot = input()
        ans.append(tot)
    if c == 1:
        ans = sorted(ans)
    elif c == 2:
        ans = sorted(ans, key=lambda x: (x[7:-3], x[:6]))
    elif c == 3:
        ans = sorted(ans, key=lambda x: (x[-2:], x[:6]))
    for i in ans:
        print(i)


if __name__ == "__main__":
    solve()

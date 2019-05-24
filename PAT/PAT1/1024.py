def check(s):   #判断回文
    if s == s[::-1]:
        return True
    else:
        return False


def solve():
    n, k = map(int, input().split())
    cnt = 0
    for i in range(k):
        if check(str(n)):
            break
        n = n + int(str(n)[::-1])
        cnt += 1
    print(n)
    print(cnt)


if __name__ == "__main__":
    solve()

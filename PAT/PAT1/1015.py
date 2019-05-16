n, d = 0, 0


def trans(n, d):    #进制转换
    res = list()
    while n > 0:
        res.append(n % d)
        n //= d
    tmp = 0
    for i in range(len(res)):
        tmp *= d
        tmp += res[i]
    return tmp


def quickPow(a, i, n):  #快速幂
    if i == 0:
        return 1 % n
    temp = quickPow(a, i >> 1, n)
    temp = temp * temp % n
    if i & 1:
        temp = temp * a % n
    return temp


def test(n, a, d):  #Miller-Rabin测试
    if n == 2 or n == a:
        return True
    if (n & 1) == 0:
        return False
    while not (d & 1):
        d >>= 1
    t = quickPow(a, d, n)
    while d != n - 1 and t != 1 and t != n - 1:
        t = t * t % n
        d <<= 1
    return t == n - 1 or d & 1


def isPrime(n):
    if n < 2:
        return False
    a = [2, 3, 17, 23, 73, 19, 11, 61]  #多次进行测试以保证正确率
    for i in range(len(a)):
        if not test(n, a[i], n - 1):
            return False
    return True


def solve():
    global n, d
    while True:
        s = list(map(int, input().split()))
        if s[0] < 0:
            return
        n, d = s[0], s[1]
        if isPrime(n) and isPrime(trans(n, d)):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    solve()

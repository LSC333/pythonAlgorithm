def tran(s, n):
    res = 0
    for i in range(len(s) - 1, -1, -1):
        res += (ord(s[i]) - ord('0') if s[i].isdigit() else
                ord(s[i]) - ord('a') + 10) * pow(n, len(s) - 1 - i)
    return res


def findRadix(n, s):
    c = max(s)
    low = ord(c) - ord('0') if c.isdigit() else ord(c) - ord('a') + 10
    low += 1
    hight = max(low, n)
    while low <= hight:
        mid = (low + hight) // 2
        tmp = tran(s, mid)
        if tmp > n:
            hight = mid - 1
        elif tmp < n:
            low = mid + 1
        else:
            return mid
    return -1


n1, n2, tag, radix = input().split()
tag, radix = int(tag), int(radix)
ans = findRadix(tran(n1, radix), n2) if tag == 1 else findRadix(tran(n2, radix), n1)
print("Impossible" if ans == -1 else ans)
exit(0)
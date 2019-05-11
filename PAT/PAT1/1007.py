k = int(input())
num = list(map(int, input().split()))
sum, ts, left, right, tl = -1, 0, 0, k - 1, 0
for i in range(k):
    ts += num[i]
    if ts > sum:
        sum = ts
        left = tl
        right = i
    if ts < 0:
        ts = 0
        tl = i + 1
sum=max(sum, 0)
print('%d %d %d' % (sum, num[left], num[right]))
exit(0)

a = list(map(float, input().split()))
b = list(map(float, input().split()))
c = [0.0 for i in range(2019)]
for i in range(1, len(a), 2):
    for j in range(1, len(b), 2):
        x = int(a[i] + b[j])
        y = a[i + 1] * b[j + 1]
        c[x] += y
cnt = 0
for i in range(len(c)):
    if c[i] != 0.0:
        cnt += 1
print(cnt, end='')
for i in range(len(c) - 1, -1, -1):
    if c[i] != 0.0:
        print(' %d %.1f' % (i, c[i]), end=('\n' if i == 0 else ''))
exit(0)

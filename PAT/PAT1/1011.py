a = list(map(float, input().split()))
b = list(map(float, input().split()))
c = list(map(float, input().split()))
ma, mb, mc = 0, 0, 0
for i in range(3):
    if a[ma] < a[i]:
        ma = i
    if b[mb] < b[i]:
        mb = i
    if c[mc] < c[i]:
        mc = i

print("%c %c %c %.2f" % (('W' if ma == 0 else ('T' if ma == 1 else 'L')),
                         ('W' if mb == 0 else ('T' if mb == 1 else 'L')),
                         ('W' if mc == 0 else ('T' if mc == 1 else 'L')),
                         (a[ma] * b[mb] * c[mc] * 0.65 - 1) * 2))
exit(0)
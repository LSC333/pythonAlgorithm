a, b = map(int, input().split())
sum = a + b
tmp = sum
sum=abs(sum)
res = []
i = 0
if sum==0:
    res.append('0')
while sum != 0:
    if i == 3:
        i = 0
        res.append(',')
    t = sum % 10
    res.append(str(t))
    i += 1
    sum //= 10
if tmp < 0:
    res.append('-')

while res:
    print(res[-1], end="")
    res.pop()
exit(0)
floor = list(map(int, input().split()))
sum = 0
now = 0
for i in range(1, len(floor)):
    sum += (4 if floor[i] - now < 0 else 6) * abs(floor[i] - now) + 5
    now = floor[i]
print(sum)
exit(0)
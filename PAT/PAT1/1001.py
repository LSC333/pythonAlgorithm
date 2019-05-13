a, b = map(int, input().split())
sum = a + b
tmp = sum
sum=abs(sum)
res = []  #结果字符串
i = 0
if sum==0:
    res.append('0')
while sum != 0:
    if i == 3:
        i = 0
        res.append(',')  #每三位添加,
    t = sum % 10
    res.append(str(t))
    i += 1
    sum //= 10
if tmp < 0:   #小于0的时候添加负号
    res.append('-')

while res:
    print(res[-1], end="")  #逆序输出
    res.pop()
exit(0)
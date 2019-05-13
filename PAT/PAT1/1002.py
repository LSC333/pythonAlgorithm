a=list(map(float, input().split()))
b=list(map(float, input().split()))
res=list()
res.append(0)
posA=1
posB=1
while True:
    if posA>=len(a):  #判断a是否加完
        if posB>=len(b):  #判断b是否加完
            break
        else:
            res[0]+=1
            res.append(b[posB])
            res.append(b[posB+1])
            posB+=2
    else:
        if posB>=len(b):
            res[0]+=1
            res.append(a[posA])
            res.append(a[posA+1])
            posA+=2
        else:
            if a[posA]==b[posB]:    #如果ab指数相等
                if a[posA+1]+b[posB+1]!=0:   #系数和不为0
                    res[0]+=1
                    res.append(a[posA])
                    res.append(a[posA+1]+b[posB+1])
                    posA+=2
                    posB+=2
                else:
                    posA+=2
                    posB+=2
            else:
                if a[posA]<b[posB]:
                    res[0]+=1
                    res.append(b[posB])
                    res.append(b[posB+1])
                    posB+=2
                else:
                    res[0]+=1
                    res.append(a[posA])
                    res.append(a[posA+1])
                    posA+=2
print(res[0], end="")
for i in range(1, len(res), 2):
    print(' %d %.1f' % (res[i], res[i+1]), end=('\n' if i==len(res)-1 else ''))
n = int(input())
id = ['' for i in range(n)]
inTime = ['' for i in range(n)]
outTime = ['' for i in range(n)]
for i in range(n):
    id[i], inTime[i], outTime[i] = input().split()

maxTime=0
minTime=0

for i in range(n):
    if inTime[minTime]>inTime[i]:
        minTime=i
    if outTime[maxTime]<outTime[i]:
        maxTime=i
print(id[minTime]+' '+id[maxTime])
exit(0)
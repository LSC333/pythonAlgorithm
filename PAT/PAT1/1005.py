num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

line = input()
sum = 0
for i in line:
    sum += int(i)
sum=str(sum)
for i in range(len(sum)):
    print(num[int(sum[i])], end=('\n' if i == len(sum) - 1 else ' '))
exit(0)
def main():
    n = int(input())
    tests = []
    count = 0
    for x in range(n):
        k = int(input())
        count += k
        temp = []
        for i in range(k):
            line = input().split(" ")
            unit = [line[0], -1, str(x + 1), -1, int(line[1])]
            temp.append(unit)
        temp = sorted(temp, key=lambda i: (-i[4], i[0]))
        temp[0][3] = '1'
        for i in range(1, k):
            if temp[i][4] != temp[i - 1][4]:
                temp[i][3] = str(i + 1)
            else:
                temp[i][3] = temp[i - 1][3]
        tests += temp
    tests = sorted(tests, key=lambda x: (-x[4], x[0]))
    tests[0][1] = '1'
    print(count)
    print(' '.join(tests[0][:-1]))
    for i in range(1, count):
        if tests[i][4] != tests[i - 1][4]:
            tests[i][1] = str(i + 1)
        else:
            tests[i][1] = tests[i - 1][1]

        print(' '.join(tests[i][:-1]))


if __name__ == "__main__":
    main()
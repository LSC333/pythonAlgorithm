# -*- coding: utf-8 -*- 
# @Time : 2019/6/23 14:23 
# @Author : ValarMorghulis 
# @File : 1060.py
def trans(num, n):
    if float(num) < 1:
        if float(num) == 0:
            return "0." + '0' * n + "*10^0"
        else:
            tmp = str(int(num[2:]))
            return ("0." + tmp + '0' * n)[0:n + 2] + "*10^" + str(len(tmp) - len(num) + 2)
    else:
        if '.' not in num:
            num += '.0'
        for i in range(len(num)):
            if num[i + 1] == '.' or int(num[i]) > 0:
                break
        num = num[i:]
        t = num.find('.')
        num = num.replace('.', '')
        return ("0." + num + '0' * n)[0:n + 2] + "*10^" + str(t)


def solve():
    n, a, b = input().split()
    a = trans(a, int(n))
    b = trans(b, int(n))
    if a == b:
        print("YES " + a)
    else:
        print("NO " + a + ' ' + b)


if __name__ == "__main__":
    solve()

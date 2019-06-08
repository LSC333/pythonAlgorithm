# -*- coding: utf-8 -*- 
# @Time : 2019/6/8 11:46 
# @Author : ValarMorghulis 
# @File : 1049.py
def solve():
    n = int(input())
    pos, right, left, a, ans = 0, 0, 0, 1, 0
    while n / a:
        pos, right, left = n // a % 10, n % a, n // a // 10
        if pos == 0:
            ans = ans + left * a
        elif pos == 1:
            ans = ans + left * a + right + 1
        else:
            ans = ans + (left + 1) * a
        a *= 10
    print(ans)


if __name__ == "__main__":
    solve()

# -*- coding: utf-8 -*- 
# @Time : 2019/7/1 9:24 
# @Author : ValarMorghulis 
# @File : 1073.py
def solve():
    s = input()
    posE = s.find('E')
    if s[0] == '-':
        print('-', end='')
    cnt = int(s[posE + 2:])
    if s[posE + 1] == '-':
        print('0.', end='')
        print('0' * (cnt - 1), end='')
        for i in range(posE):
            if '0' <= s[i] <= '9':
                print(s[i], end='')
        print('')
    else:
        cnt += 1
        for i in range(posE):
            if cnt == 0:
                print('.', end='')
            if '0' <= s[i] <= '9':
                print(s[i], end='')
                cnt -= 1
        print('0' * cnt)


if __name__ == "__main__":
    solve()

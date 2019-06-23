# -*- coding: utf-8 -*- 
# @Time : 2019/6/23 15:53 
# @Author : ValarMorghulis 
# @File : 1061.py
def solve():
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    t = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    cnt = 0
    d, h, m = 0, 0, 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            if cnt == 0:
                if 'A' <= s1[i] <= 'G':
                    d = s1[i]
                    cnt += 1
                    continue
            if cnt == 1:
                if 'A' <= s1[i] <= 'N' or '0' <= s1[i] <= '9':
                    h = s1[i]
                    cnt += 1
                    break
    for i in range(min(len(s3), len(s4))):
        if s3[i] == s4[i]:
            if 'a' <= s3[i] <= 'z' or 'A' <= s3[i] <= 'Z':
                m = i
                break
    d = t[int(ord(d) - ord('A'))]
    if '0' <= h <= '9':
        h = ord(h) - ord('0')
    else:
        h = 10 + ord(h) - ord('A')
    print("%s %02d:%02d" % (d, h, m))


if __name__ == "__main__":
    solve()

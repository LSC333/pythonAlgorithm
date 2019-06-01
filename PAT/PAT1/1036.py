# -*- coding: utf-8 -*- 
# @Time : 2019/6/1 9:24 
# @Author : ValarMorghulis 
# @File : 1036.py
def solve():
    n = eval(input())
    male = list()
    female = list()
    for i in range(n):
        name, gender, id, grade = input().split()
        grade = int(grade)
        if gender == 'M':
            male.append([name, id, grade])
        elif gender == 'F':
            female.append([name, id, grade])
    male = sorted(male, key=lambda x: x[2])
    female = sorted(female, key=lambda x: x[2], reverse=True)
    if len(male) == 0:
        print("%s %s" % (female[0][0], female[0][1]))
        print("Absent")
        print("NA")
    elif len(female) == 0:
        print("Absent")
        print("%s %s" % (male[0][0], male[0][1]))
        print("NA")
    else:
        print("%s %s" % (female[0][0], female[0][1]))
        print("%s %s" % (male[0][0], male[0][1]))
        print(female[0][2] - male[0][2])


if __name__ == "__main__":
    solve()

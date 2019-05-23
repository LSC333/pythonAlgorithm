class student:
    def __init__(self, C, M, E, ID):
        self.grade = [round((C + M + E) / 3), C, M, E]
        self.id = ID
        self.rank = [-1, -1, -1, -1]


def solve():
    line = input().split(" ")
    n = int(line[0])
    m = int(line[1])
    students = {}
    for i in range(n):
        line = input().split(" ")
        ID = line[0]
        C = int(line[1])
        M = int(line[2])
        E = int(line[3])
        s = student(C, M, E, ID)
        students[ID] = s
    for x in range(4):
        p = sorted(students.values(), key=lambda i: -i.grade[x])
        p[0].rank[x] = 1
        for i in range(1, n):
            p[i].rank[x] = i + 1
            if p[i].grade[x] == p[i - 1].grade[x]:
                p[i].rank[x] = p[i - 1].rank[x]
    for i in range(m):
        line = input()
        try:
            unit = students[line]
            temp = zip(unit.rank, ['0A', '1C', '2M', '3E'])
            temp = sorted(temp)
            print(str(min(unit.rank)), temp[0][1][1])
        except:
            print('N/A')


if __name__ == "__main__":
    solve()

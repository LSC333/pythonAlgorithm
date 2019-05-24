def solve():
    n = eval(input())
    m = n * 2
    if ''.join(sorted(str(n))) == ''.join(sorted(str(m))):
        print("Yes")
    else:
        print("No")
    print(m)


if __name__ == "__main__":
    solve()

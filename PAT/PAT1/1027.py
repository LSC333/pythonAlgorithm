def solve():
    ans = [chr(ord('0') + i) if i <= 9 else chr(ord('A') + i - 10) for i in range(13)]
    red, green, blue = map(int, input().split())
    print('#%c%c%c%c%c%c' % (ans[red // 13], ans[red % 13],
                             ans[green // 13], ans[green % 13],
                             ans[blue // 13], ans[blue % 13]))


if __name__ == "__main__":
    solve()

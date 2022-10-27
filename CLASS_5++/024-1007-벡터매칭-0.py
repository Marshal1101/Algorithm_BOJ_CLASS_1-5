## https://www.acmicpc.net/source/41970874

"""
Probliem Link: https://www.acmicpc.net/problem/1007
Solution Link: https://jintak0401.github.io/posts/boj-1007
"""

from sys import stdin

input = stdin.readline


def solve():
    TC = int(input())
    inf = float('inf')
    x, y = [0] * 20, [0] * 20
    ans, tx, ty = inf, 0, 0

    def combi(cnt, idx, sx, sy):
        nonlocal ans
        if cnt == 0:
            tmp = ((tx - 2 * sx) ** 2 + (ty - 2 * sy) ** 2) ** 0.5
            if tmp < ans:
                ans = tmp

        else:
            for i in range(idx, N - cnt + 1):
                combi(cnt-1, i+1, sx+x[i], sy+y[i])

    for _ in range(TC):
        N = int(input())
        ans, tx, ty = inf, 0, 0
        for i in range(N):
            x[i], y[i] = map(int, input().split())
            tx += x[i]
            ty += y[i]
        combi(N//2 - 1, 1, x[0], y[0])
        print(ans)


if __name__ == '__main__':
    solve()

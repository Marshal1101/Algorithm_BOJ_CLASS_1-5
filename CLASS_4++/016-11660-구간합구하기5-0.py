## https://www.acmicpc.net/source/43272734

def solution():
    import sys

    input = iter(sys.stdin.read().split("\n")).__next__
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    dp = [before := [0] * (n + 1)] + [
        (before := [b := 0] + [
                (b := b + l) + m
                for l, m in zip(line, before[1:])
        ])
        for line in table
    ]
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        x1 -= 1
        y1 -= 1
        print(dp[x2][y2] - dp[x1][y2] - dp[x2][y1] + dp[x1][y1])


solution()
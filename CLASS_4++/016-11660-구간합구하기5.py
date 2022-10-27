## pypy

import sys; input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
pre_line_sum = 0

for _ in range(N) :
    line = list(map(int, input().split()))
    line = [pre_line_sum] + line
    for i in range(1, N+1) :
        line[i] = line[i-1] + line[i]
    pre_line_sum = line[N]
    graph.append(line)

for _ in range(M) :
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    res = 0
    for i in range(x1-1, x2) :
        res += graph[i][y2] - graph[i][y1-1]

    print(res)
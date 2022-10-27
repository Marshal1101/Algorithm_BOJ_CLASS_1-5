## https://www.acmicpc.net/source/13769331

import sys
from heapq import *
input = sys.stdin.readline
n, m, x = map(int, input().split())
home = [[] for _ in range(n+1)]
home2 = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    home[s].append((e, t))
    home2[e].append((s, t))

def dijkstra(g, start):
    d=[9876543210]*(n+1)
    d[start] = 0
    heap = [(0,start)]
    while heap:
        total, node = heappop(heap)
        if d[node]<total:continue
        for nxt, cost in g[node]:
            if d[nxt]>d[node]+cost:
                d[nxt] = d[node]+cost
                heappush(heap, (d[nxt],nxt))
    return d[1:]

print(max([a+b for a, b in zip(dijkstra(home, x), dijkstra(home2,x))]))
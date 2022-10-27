## 데이크스트라

import sys; input = sys.stdin.readline
from heapq import heappop, heappush

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
items.insert(0, 0)
graph = [[] for _ in range(n+1)]
for _ in range(r) :
    a, b, l =  map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

def dijkstra(start, min_dist) :
    min_dist[start] = 0
    hq = [(0, start)]
    while hq :
        dist, node = heappop(hq)
        if dist > min_dist[node] :
            continue
        for adj, l in graph[node] :
            new_dist = dist + l
            if new_dist < min_dist[adj] :
                min_dist[adj] = new_dist
                heappush(hq, (new_dist, adj))

    return min_dist

INF = sys.maxsize
max_cnt = 0
for i in range(1, n+1) :
    dist = dijkstra(i, [INF] * (n+1))
    cnt = 0
    for k in range(1, n+1) :
        if dist[k] <= m :
            cnt += items[k]
    if cnt > max_cnt :
        max_cnt = cnt

print(max_cnt)
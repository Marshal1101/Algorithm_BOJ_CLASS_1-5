import sys; input = sys.stdin.readline
from heapq import heappop, heappush

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E) :
    v1, v2, d = map(int, input().split())
    graph[v1].append([v2, d])
    graph[v2].append([v1, d])

s1, s2 = map(int, input().split())
inf = sys.maxsize

def dijkstra(start, end) :
    min_dist = [inf for _ in range(N+1)]
    min_dist[start] = 0
    hq = [(0, start)]

    while hq :
        d, node = heappop(hq)
        for adj, dist in graph[node] :
            exp_dist = d + dist
            if exp_dist < min_dist[adj] :
                min_dist[adj] = exp_dist
                heappush(hq, (exp_dist, adj))

    return min_dist[end]

m1s1 = dijkstra(1, s1)
m1s2 = dijkstra(1, s2)
ms1N = dijkstra(s1, N)
ms2N = dijkstra(s2, N)
s1s2 = dijkstra(s1, s2)
s2s1 = dijkstra(s2, s1)

a = m1s1 + s1s2 + ms2N
b = m1s2 + s2s1 + ms1N

cnt = min(a, b)
print(cnt if cnt < inf else -1)
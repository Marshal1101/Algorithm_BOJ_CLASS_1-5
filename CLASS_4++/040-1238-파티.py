import sys; input = sys.stdin.readline
from heapq import heappop, heappush

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))

def dijkstra(start) :
    INF = sys.maxsize
    min_w = [INF] * (N+1)
    min_w[start] = 0
    hq = [(0, start)]
    while hq :
        past, node = heappop(hq)
        if past > min_w[node] :
            continue
        for adj, w in graph[node] :
            nw = past + w
            if nw < min_w[adj] :
                min_w[adj] = nw
                heappush(hq, (nw, adj))
    return min_w

res = [ 0 for _ in range(N+1) ]
for i in range(1, N+1) :
    res[i] += dijkstra(i)[X]
from_X = dijkstra(X)
for i in range(1, N+1) :
    res[i] += from_X[i]
print(max(res))
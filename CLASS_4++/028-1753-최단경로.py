import sys; input = sys.stdin.readline
from heapq import heappush, heappop

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E) :
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start) :
    INF = sys.maxsize
    min_w = [INF] * (V+1)
    min_w[start] = 0
    hq = [(0, start)]
    while hq :
        pre_w, node = heappop(hq)
        if pre_w > min_w[node] :
            continue
        for adj, w in graph[node] :
            exp_w = pre_w + w
            if exp_w < min_w[adj] :
                min_w[adj] = exp_w
                heappush(hq, (exp_w, adj))             
    
    for i in range(1, V+1) :
        print(min_w[i] if min_w[i] < INF else 'INF')

dijkstra(K)
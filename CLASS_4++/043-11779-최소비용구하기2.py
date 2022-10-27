import sys
from heapq import heappop, heappush

def dijkstra(n, start, end, graph) :
    INF = float('inf')
    min_dist = [INF] * (n+1)
    min_dist[start] = 0
    path = [start]
    heapq = [(0, start, path)]
    while heapq :
        dist, node, path = heappop(heapq)
        if dist > min_dist[node] :
            continue
        if node == end :
            ret_path = path[:]
        for adj, d in graph[node] :
            if (new_d := dist + d) < min_dist[adj] :
                min_dist[adj] = new_d
                path.append(adj)
                heappush(heapq, (new_d, adj, path[:]))
                path.pop()

    return [min_dist[end], ret_path]

def main() :
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(m) :
        v1, v2, w = map(int, input().split())
        graph[v1].append((v2, w))
    
    start, end = map(int, input().split())
    dist, path = dijkstra(n, start, end, graph)
    print(dist)
    print(len(path))
    print(*path)

if __name__ == '__main__' :
    main()
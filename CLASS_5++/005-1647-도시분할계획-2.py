## 프림 알고리즘

import sys
from heapq import heappop, heappush

def prim(s_node, N, graph) :
    total_dist = 0
    max_dist = 0

    INF = sys.maxsize
    min_dist =[INF] * (N+1)
    min_dist[s_node] = 0
    
    spanning_tree = set()
    adj_heapq = [(0, s_node)]
    while len(spanning_tree) < N :
        cur_d, cur_node = heappop(adj_heapq)
        if cur_d > min_dist[cur_node] :
            continue
        if cur_d > max_dist : max_dist = cur_d
        total_dist += cur_d
        spanning_tree.add(cur_node)
        for dist, adj in graph[cur_node]:
            if dist < min_dist[adj] and not adj in spanning_tree :
                min_dist[adj] = dist
                heappush(adj_heapq, (dist, adj))

    return (total_dist, max_dist)


def main() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M) :
        A, B, C = map(int, input().split())
        graph[A].append((C, B))
        graph[B].append((C, A))
    
    total_dist, max_dist = prim(1, N, graph)
    print(total_dist - max_dist)
    

if __name__ == '__main__' :
    main()
## 프림 알고리즘

import sys, math
from heapq import heappop, heappush

def prim(start, N, graph) :
    visited = [False] * N
    adj_heapq = [(0, start)]
    cnt = 0
    total = 0
    while cnt < N :
        cur_d, cur_node = heappop(adj_heapq)
        if not visited[cur_node] :
            visited[cur_node] = True
            total += cur_d
            cnt += 1
            for dist, adj in graph[cur_node] :
                if not visited[adj] :
                    heappush(adj_heapq, (dist, adj))
    
    return round(total, 2)


def distance_xy(x1, y1, x2, y2) :
    return math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)


def main() :
    input = sys.stdin.readline
    N = int(input())
    node_list = []
    for _ in range(N) :
        node_list.append(list(map(float, input().split())))
    
    graph = [[] for _ in range(N)]
    for i in range(N-1) :
        x1, y1 = node_list[i]
        for j in range(i+1, N) :
            x2, y2 = node_list[j]
            dist = distance_xy(x1, y1, x2, y2)
            graph[i].append((dist, j))
            graph[j].append((dist, i))

    print(prim(0, N, graph))


if __name__ == '__main__' :
    main()
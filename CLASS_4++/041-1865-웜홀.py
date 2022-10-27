import sys; input = sys.stdin.readline

def bellmanFord(graph) :
    INF = sys.maxsize
    min_dist = [INF for _ in range(N+1)]
    
    for i in range(1, N+1) :
        for node in range(1, N+1) :
            for adj, dist in graph[node] :
                if (next_d := min_dist[node] + dist) < min_dist[adj] :
                    min_dist[adj] = next_d
                    if i == N :
                        return False
    return True


TC = int(input())
for _ in range(TC) :
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M) :
        S, E, T = map(int, input().split())
        graph[S].append((E, T))
        graph[E].append((S, T))
    for _ in range(W) :
        S, E, T = map(int, input().split())
        graph[S].append((E, -T))
    
    if bellmanFord(graph) :
        print('NO')
    else : print('YES')
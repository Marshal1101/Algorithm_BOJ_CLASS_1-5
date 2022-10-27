import sys
from collections import deque

def topological_sort(N, P, time, indegree, graph) :
    que = deque([])
    max_time = [0] * (N+1)
    for i in range(1, N+1) :
        if not indegree[i] :
            max_time[i] = time[i]
            que.append(i)
    while que :
        node = que.popleft()
        if node == P : return max_time[node]
        for adj in graph[node] :
            indegree[adj] -= 1
            if (n_cost := max_time[node] + time[adj]) > max_time[adj] :
                max_time[adj] = n_cost
            if not indegree[adj] :
                que.append(adj)

def main() :
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T) :
        N, K = map(int, input().split())
        time = [0, *map(int, input().split())]
        graph = [[] for _ in range(N+1)]
        indegree = [0] * (N+1)
        for _ in range(K) :
            bf, af = map(int, input().split())
            graph[bf].append(af)
            indegree[af] += 1
        P = int(input())

        print(topological_sort(N, P, time, indegree, graph))


if __name__ == '__main__' :
    main()
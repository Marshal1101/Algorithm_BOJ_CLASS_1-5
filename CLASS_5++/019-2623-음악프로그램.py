import sys
from collections import deque

def topological_sort(N, indegree, graph) :
    que = deque([])
    for node in range(1, N+1):
        if not indegree[node] :
            que.append(node)
    # print('que0:', que)
    order = []
    while que :
        node = que.popleft()
        order.append(node)
        for adj in graph[node] :
            indegree[adj] -= 1
            if not indegree[adj] :
                que.append(adj)
    
    return order


def main() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    for _ in range(M) :
        sub_pd = list(map(int, input().split()))
        before = sub_pd[1]
        for k in range(2, sub_pd[0]+1) :
            graph[before].append(sub_pd[k])
            indegree[sub_pd[k]] += 1
            before = sub_pd[k]
    # print(indegree)

    order = topological_sort(N, indegree, graph)
    if len(order) != N :
        print(0)
    else :
        for singer in order :
            print(singer)


if __name__ == '__main__' :
    main()
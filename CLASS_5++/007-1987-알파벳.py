# PyPy

import sys

def main() :
    input = sys.stdin.readline
    R, C = map(int, input().split())
    graph = []
    for _ in range(R) :
        graph.append(list(input().rstrip()))
    
    global max_cnt
    max_cnt = 0

    visited = [0] * 26
    visited[ord(graph[0][0])-65] = 1
    max_cnt = dfs(0, 0, 1, graph, visited, R, C)
    print(max_cnt)

def dfs(si, sj, cnt, graph, visited, R, C) :
    global max_cnt
    if cnt > max_cnt : max_cnt = cnt

    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for di, dj in delta :
        if 0 <= (ni := si + di) < R and 0 <= (nj := sj + dj) < C :
            alphabet = ord(graph[ni][nj]) - 65
            if not visited[alphabet] :
                visited[alphabet] = 1
                dfs(ni, nj, cnt+1, graph, visited, R, C)
                visited[alphabet] = 0


if __name__ == '__main__' :
    main()
import sys; input = sys.stdin.readline
from itertools import combinations
from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N) :
    graph.append(input().split())

total = N * M
wall = 0
virus = 0
virus_pos = []
zero_pos = []
for i in range(N) :
    for j in range(M) :
        if graph[i][j] == '1' :
            wall += 1
        elif graph[i][j] == '2' :
            virus_pos.append((i, j))
            virus += 1
        else :
            zero_pos.append((i, j))

def bfs(set_wall_yx, new_graph) :
    for sy, sx in set_wall_yx :
        new_graph[sy][sx] = '1'
    safe_cnt = total - virus - wall - 3
    que = deque(virus_pos)
    while que :
        length = len(que)
        infected_cnt = 0
        for _ in range(length) :
            vi, vj = que.popleft()
            if 0 <= vi - 1 and new_graph[vi-1][vj] == '0' :
                new_graph[vi-1][vj] = '2'
                que.append((vi-1, vj))
                infected_cnt += 1
            if vi + 1 < N and new_graph[vi+1][vj] == '0' :
                new_graph[vi+1][vj] = '2'
                que.append((vi+1, vj))
                infected_cnt += 1
            if 0 <= vj - 1 and new_graph[vi][vj-1] == '0' :
                new_graph[vi][vj-1] = '2'
                que.append((vi, vj-1))
                infected_cnt += 1
            if vj + 1 < M and new_graph[vi][vj+1] == '0' :
                new_graph[vi][vj+1] = '2'
                que.append((vi, vj+1))
                infected_cnt += 1
        safe_cnt -= infected_cnt
        if not infected_cnt :
            return safe_cnt

max_safe_cnt = 0
for set_wall_yx in combinations(zero_pos, 3) :
    copy_graph = [graph[i][:] for i in range(N)]
    each_safe_cnt = bfs(set_wall_yx, copy_graph)
    if each_safe_cnt > max_safe_cnt :
        max_safe_cnt = each_safe_cnt
print(max_safe_cnt)
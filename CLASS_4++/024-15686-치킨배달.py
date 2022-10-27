import sys; input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
graph = []
for _ in range(N) :
    graph.append(input().split())

h_pos = []
c_pos = []

for i in range(N) :
    for j in range(N) :
        if graph[i][j] == '1' :
            h_pos.append((i, j))        
        elif graph[i][j] == '2' :
            c_pos.append((i, j))

def bfs(sel_c_pos: list) :    
    total_dist = 0
    for hy, hx in h_pos :
        min_dist = N*2
        for cy, cx in sel_c_pos :
            dist = abs(hy - cy) + abs(hx - cx)
            if dist < min_dist : min_dist = dist
        total_dist += min_dist
            
    return total_dist

min_total_dist = sys.maxsize
for set_c_pos in combinations(c_pos, M) :
    total_dist = bfs(list(set_c_pos))
    if min_total_dist > total_dist :
        min_total_dist = total_dist

print(min_total_dist)
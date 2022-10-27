## pypy

import sys; input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N) :
    graph.append(list(map(int, input().split())))

for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 1 :
            graph[i][j] = -1

def pipe(i, j, state: str) :
    if j + 1 < N and state == "hor" :
        if graph[i][j+1] != -1 :
            graph[i][j+1] += 1
            pipe(i, j+1, "hor")

    elif i + 1 < N and state == "ver" :
        if graph[i+1][j] != -1 :
            graph[i+1][j] += 1
            pipe(i+1, j, "ver")
        
    elif state == "cro" :
        if j + 1 < N and graph[i][j+1] != -1 :
            graph[i][j+1] += 1
            pipe(i, j+1, "hor")
        if i + 1 < N and graph[i+1][j] != -1 :
            graph[i+1][j] += 1
            pipe(i+1, j, "ver")

    if j + 1 < N and i + 1 < N and graph[i][j+1] != -1 and graph[i+1][j] != -1 and graph[i+1][j+1] != -1 :
        graph[i+1][j+1] += 1
        pipe(i+1, j+1, "cro")

if graph[N-1][N-1] == -1 :
    print(0)
else :
    pipe(0, 1, "hor")
    print(graph[N-1][N-1])
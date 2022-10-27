import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N) :
    graph.append(input().strip())

def dfs_nor(y, x) :
    color = graph[y][x]
    visited[y][x] = 1
    stack = [(y, x)]
    while stack :
        i, j = stack.pop()
        if i + 1 < N and visited[i+1][j] == 0 and graph[i+1][j] == color :
            visited[i+1][j] = 1
            stack.append((i+1, j))
        if i - 1 >= 0 and visited[i-1][j] == 0 and graph[i-1][j] == color :
            visited[i-1][j] = 1
            stack.append((i-1, j))
        if j + 1 < N and visited[i][j+1] == 0 and graph[i][j+1] == color :
            visited[i][j+1] = 1
            stack.append((i, j+1))
        if j - 1 >= 0 and visited[i][j-1] == 0 and graph[i][j-1] == color :
            visited[i][j-1] = 1
            stack.append((i, j-1))
    return 1

def dfs_abn(y, x) :
    color = graph[y][x]
    visited[y][x] = 1
    stack = [(y, x)]
    if color == 'B' :
        while stack :
            i, j = stack.pop()
            if i + 1 < N and visited[i+1][j] == 0 and graph[i+1][j] == color :
                visited[i+1][j] = 1
                stack.append((i+1, j))
            if i - 1 >= 0 and visited[i-1][j] == 0 and graph[i-1][j] == color :
                visited[i-1][j] = 1
                stack.append((i-1, j))
            if j + 1 < N and visited[i][j+1] == 0 and graph[i][j+1] == color :
                visited[i][j+1] = 1
                stack.append((i, j+1))
            if j - 1 >= 0 and visited[i][j-1] == 0 and graph[i][j-1] == color :
                visited[i][j-1] = 1
                stack.append((i, j-1))
    else :
        while stack :
            i, j = stack.pop()
            if i + 1 < N and visited[i+1][j] == 0 and graph[i+1][j] != 'B' :
                visited[i+1][j] = 1
                stack.append((i+1, j))
            if i - 1 >= 0 and visited[i-1][j] == 0 and graph[i-1][j] != 'B' :
                visited[i-1][j] = 1
                stack.append((i-1, j))
            if j + 1 < N and visited[i][j+1] == 0 and graph[i][j+1] != 'B' :
                visited[i][j+1] = 1
                stack.append((i, j+1))
            if j - 1 >= 0 and visited[i][j-1] == 0 and graph[i][j-1] != 'B' :
                visited[i][j-1] = 1
                stack.append((i, j-1))        
    return 1

visited = [[0 for _ in range(N)] for _ in range(N)]
abnormal_cnt = 0
for i in range(N) :
    for j in range(N) :
        if visited[i][j] != 1 :
            abnormal_cnt += dfs_abn(i, j)

visited = [[0 for _ in range(N)] for _ in range(N)]
normal_cnt = 0
for i in range(N) :
    for j in range(N) :
        if visited[i][j] != 1 :
            normal_cnt += dfs_nor(i, j)

print(normal_cnt, abnormal_cnt)
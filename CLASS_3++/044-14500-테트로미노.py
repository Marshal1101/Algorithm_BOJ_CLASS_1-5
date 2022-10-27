import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []

for i in range(N) :
    graph.append(list(map(int, input().split())))
max_val = max(map(max, graph)) # 모든 좌표 중 최댓값

def dfs(y: int, x: int, level: int, total: int, banned: int) :
    global max_total

    if total + max_val*(4-level) <= max_total:
        return

    if level == 4 :
        max_total = max(max_total, total)
        return

    total += graph[y][x]
    if y - 1 >= 0 and banned != 0 :
        dfs(y-1, x, level+1, total, 1)
    if y + 1 < N and banned != 1 :
        dfs(y+1, x, level+1, total, 0)
    if x - 1 >= 0 and banned != 2 :
        dfs(y, x-1, level+1, total, 3)
    if x + 1 < M and banned != 3 :
        dfs(y, x+1, level+1, total, 2)

    if level == 0 :
        max_clksum = 0
        yi = [-1, 1, 0, 0]
        xi = [0, 0, -1, 1]
        for l in range(4) :
            clksum = 0
            for k in range(4) :
                if l == k : continue
                ny = y + yi[k]
                nx = x + xi[k]
                if 0 <= ny < N and 0 <= nx < M :
                    clksum += graph[ny][nx]
            max_clksum = max(max_clksum, clksum)
        max_total = max(max_total, total + max_clksum)
    
    if level == 1 :
        max_clksum = 0
        yi = [-1, 1, 0, 0]
        xi = [0, 0, -1, 1]
        for l in range(4) :
            if l == banned : continue
            clksum = 0
            for k in range(4) :
                if k == l or k == banned : continue
                ny = y + yi[k]
                nx = x + xi[k]
                if 0 <= ny < N and 0 <= nx < M :
                    clksum += graph[ny][nx]
            max_clksum = max(max_clksum, clksum)
        max_total = max(max_total, total + max_clksum)                    

max_total = 0
for i in range(0, N) :
    for j in range(0, M) :
        dfs(i, j, 0, 0, 'C')

print(max_total)
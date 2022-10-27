import sys; input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
graph.append([0 for _ in range(N+1)])
pre_line_sum = 0
for i in range(1, N+1) :
    line = list(map(int, input().split()))
    line = [0] + line
    for j in range(1, N+1) :
        line[j] = line[j] + line[j-1] + graph[i-1][j] - graph[i-1][j-1]
    graph.append(line)

for _ in range(M) :
    x1, y1, x2, y2 = map(int, input().split())
    print(graph[x2][y2] - graph[x2][y1-1] - graph[x1-1][y2] + graph[x1-1][y1-1])
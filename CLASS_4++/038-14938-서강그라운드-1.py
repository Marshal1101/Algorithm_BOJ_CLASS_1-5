## 플로이드워셜

import sys; input = sys.stdin.readline

n, m, r = map(int, input().split())
item_list = list(map(int, input().split()))
INF = sys.maxsize
graph = [[INF for _ in range(n)] for _ in range(n)]
for _ in range(r) :
    a, b, l = map(int, input().split())
    graph[a-1][b-1] = l
    graph[b-1][a-1] = l

for i in range(n) :
    graph[i][i] = 0

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            temp = graph[i][k] + graph[k][j]
            if temp < graph[i][j] :
                graph[i][j] = temp

max_items = 0
for i in range(n) :
    item = 0
    for j in range(n) :
        if graph[i][j] <= m :
            item += item_list[j]
    if item > max_items :
        max_items = item 

print(max_items)
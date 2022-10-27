import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M) :
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def check(start) :
    visited = [False] * (N+1)
    visited[start] = True
    que = [(start, 0)]
    min_cnt = 0
    ptr = 0
    while len(que) > ptr :
        node, level = que[ptr]
        for edge in graph[node] :
            if visited[edge] != True :
                visited[edge] = True
                min_cnt += (level + 1)
                que.append((edge, level+1))
        ptr += 1
    return min_cnt

min_kbnum = (sys.maxsize, 0)
for i in range(1, N+1) :
    cnt = check(i)
    if cnt < min_kbnum[0] :
        min_kbnum = (cnt, i)

print(min_kbnum[1])
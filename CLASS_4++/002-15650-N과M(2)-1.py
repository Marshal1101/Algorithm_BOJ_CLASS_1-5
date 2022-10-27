## 조합

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

visited = [False] * (N+1)
finished = [False] * (N+1)
path = [0] * (N+1)
res = set()
def dfs(n, m, cnt) :
    # if finished[i] : return
    if cnt == m :
        res.add(''.join(map(str, path)))
        return

    for i in range(1, n+1) :
        if not visited[i] :
            visited[i] = True
            path[i] = 1
            dfs(n, m, cnt+1)
            path[i] = 0
            visited[i] = False

dfs(N, M, 0)
# result = list(res)
# print(result)
result = []
for r in res :
    temp = []
    for i in range(N+1) :
        if r[i] == '1' :
            temp.append(i)
    result.append(temp)
result.sort()
for k in result :
    print(*k)
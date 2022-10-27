## 조합

import sys; input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
visited = [False] * (N+1)
def dfs(length, cnt, res) :

    if cnt == 0 :
        print(*res)
        return
    
    for i in range(length) :
        if not visited[i] :
            res.append(arr[i])
            visited[i] = True
            dfs(length, cnt-1, res)
            visited[i] = False
            res.pop()

dfs(N, M, [])
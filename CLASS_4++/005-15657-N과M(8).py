import sys; input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
visited = [False] * (N+1)
def dfs(start, cnt, res) :

    if cnt == 0 :
        print(*res)
        return
    
    for i in range(start, N) :
        res.append(arr[i])
        dfs(i, cnt-1, res)
        res.pop()

dfs(0, M, [])
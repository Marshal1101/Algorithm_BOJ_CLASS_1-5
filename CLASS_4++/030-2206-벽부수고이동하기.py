import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N) :
    graph.append(input().strip())

INF = sys.maxsize

def bfs(si, sj) :
    dp = [[ [INF, INF] for _ in range(M) ] for _ in range(N)]
    dp[si][sj] = [1, 1]
    que = deque([(si, sj, 0)])
    while que :
        i, j, b = que.popleft()
        for ni, nj in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)] :
            if 0 <= ni < N and 0 <= nj < M :
                if graph[ni][nj] == '0' :
                    if dp[i][j][b] + 1 < dp[ni][nj][b] :
                        dp[ni][nj][b] = dp[i][j][b] + 1
                        que.append((ni, nj, b))
                    
                elif graph[ni][nj] == '1' and b < 1:
                    if dp[i][j][b] + 1 < dp[ni][nj][b+1] :    
                        dp[ni][nj][b+1] = dp[i][j][b] + 1
                        que.append((ni, nj, b + 1))

    return dp[N-1][M-1]

cnt1, cnt2 = bfs(0, 0)
# print(cnt1, cnt2)
if cnt1 < INF or cnt2 < INF : print(cnt1 if cnt1 < cnt2 else cnt2)
else : print(-1)
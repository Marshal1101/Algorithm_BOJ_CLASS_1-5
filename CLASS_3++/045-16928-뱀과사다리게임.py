## pypy
## DFS : 단계를 깊이우선하여 증가하므로 조건 만족하더라도 최소값 보장 못함
## 실시간으로 현재 최소값 반영하여 최소값 보다 크면 바로바로 종료하여 시간 단축해야함


import sys; input = sys.stdin.readline


N, M = map(int, input().split())
board = [0] * 101
for _ in range(N) :
    x, y = map(int, input().split())
    board[x] = y
for _ in range(M) :
    u, v = map(int, input().split())
    board[u] = v
visited = [False] * 101
past_path = [30] * 101
min_move = 17
def dfs(start, cnt) :
    global min_move
    if cnt > min_move : return
    if cnt > past_path[start] : return
    if start > 93 : 
        min_move = min(min_move, cnt + 1)
        return

    for i in range(1, 7) :
        nex = start + i
        if not visited[nex] :
            past_path[nex] = min(past_path[nex], cnt+1)
            visited[nex] = True
            if board[nex] :
                past_path[board[nex]] = min(past_path[board[nex]], cnt+1)
                visited[board[nex]] = True
                dfs(board[nex], cnt + 1)
                visited[board[nex]] = False
            else :
                dfs(nex, cnt + 1)
            visited[nex] = False

dfs(1, 0)
print(min_move)
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

def N_to_the_K(N, K, visited, cnt) :
    if visited[N] != 0 : return
    res = []
    visited[N] = 1
    que = deque([(N, cnt)])
    while que :
        cur, cnt = que.popleft()
        if cur == K :
            res.append(cnt)
            continue
        if (cur*2 <= 2*(K-1)) :
            if visited[cur*2] != 1 :
                visited[cur*2] = 1
                que.append((cur*2, cnt+1))
        if (cur + 1 <= K) :
            if visited[cur+1] != 1 :
                visited[cur+1] = 1
                que.append((cur+1, cnt+1))
        if (0 <= cur - 1 <= K) :
            if visited[cur-1] != 1 :
                visited[cur-1] = 1
                que.append((cur-1, cnt+1))
    return min(res)

if N > K : print(N-K)
elif N == K : print(0)
else :
    visited = [0] * (2*K)
    print(N_to_the_K(N, K, visited, 0))
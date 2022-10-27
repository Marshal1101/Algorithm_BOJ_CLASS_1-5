## 숨바꼭질 문제에서 cur*2 경우 가중치가 0 으로 우선되어지므로 appendleft 한다.
## 근데 cur*2를 앞에 넣어서 우선해야할 경우가 1->2 때 말고 더 있을까?

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
            return cnt

        if (cur == 1) :
            if visited[cur+1] != 1 :
                visited[cur*2] = 1
                que.append((cur*2, cnt+1))
            if visited[cur+1] != 1 :
                visited[cur+1] = 1
                que.append((cur+1, cnt+1))
        else :
            if (cur*2 <= 2*(K-1)) :
                if visited[cur*2] != 1 :
                    visited[cur*2] = 1
                    que.appendleft((cur*2, cnt))
            if (cur + 1 <= K) :
                if visited[cur+1] != 1 :
                    visited[cur+1] = 1
                    que.append((cur+1, cnt+1))
            if (0 <= cur - 1 <= K) :
                if visited[cur-1] != 1 :
                    visited[cur-1] = 1
                    que.append((cur-1, cnt+1))

if N > K : print(N-K)
elif N == K : print(0)
else :
    visited = [0] * (2*K)
    print(N_to_the_K(N, K, visited, 0))
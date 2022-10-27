## 조합

## 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
## 고른 수열은 오름차순이어야 한다

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
# print(N, M)
def dfs(start, count, res) :
    if count == 0 :
        print(res)
    
    for i in range(start, N+1) :
        next_res = res + str(i) + ' '
        dfs(i + 1, count - 1, next_res)

dfs(1, M, '')
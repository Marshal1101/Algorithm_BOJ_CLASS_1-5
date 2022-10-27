## 중복순열

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * (N+1)

def dfs(start, cnt, res) :
    if cnt == 0 :
        print(res)
        return

    for i in range(start, N+1) :
        new_res = res + str(i) + ' '
        dfs(i, cnt-1, new_res)
dfs(1, M, '')
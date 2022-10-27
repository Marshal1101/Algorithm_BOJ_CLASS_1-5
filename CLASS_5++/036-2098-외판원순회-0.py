import sys

input = sys.stdin.readline
N = int(input())
city = []
for i in range(N) : 
    city.append(list(map(int, input().split())))
INF = sys.maxsize
dp = [[-1 for _ in range(1 << N)] for _ in range(N)]

def recursion(cur, visited):
    # all node visit
    if visited == (1 << N)-1:
        if city[cur][0] == 0:
            return INF
        dp[cur][visited] = city[cur][0]
        return city[cur][0]

    # memoization
    if dp[cur][visited] != -1:
        return dp[cur][visited]

    # even if i to i is impossible, change dp[i][i] = -1 => INF
    # it can ban new recursions of 'i to i case' before all node visited
    min_dist = INF
    for i in range(N):
        # if not visited i-node yet + city not zero
        if not visited & (1 << i) and city[cur][i] != 0:
            min_dist = min(min_dist, city[cur][i] + recursion(i, visited | (1 << i)))

    dp[cur][visited] = min_dist
    return dp[cur][visited]

print(recursion(0, 1))
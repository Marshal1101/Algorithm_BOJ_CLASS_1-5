import sys

input = sys.stdin.readline

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4
T = int(input())
for i in range(T) :
    N = int(input())
    if (dp[N] == 0) :
        for i in range(4, N+1) :
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[N])
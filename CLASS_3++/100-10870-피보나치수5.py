import sys

N = int(sys.stdin.readline())

def fibonacci(N) :
    dp = [0, 1, 1, 2]
    if N < 4 : return dp[N]
    for _ in range(4, N+1) :
        dp[1] = dp[2]
        dp[2] = dp[3]
        dp[3] = dp[2] + dp[1]
    return dp[3]

print(fibonacci(N))
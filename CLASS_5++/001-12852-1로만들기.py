## https://developmentdiary.tistory.com/428

import sys; input = sys.stdin.readline

N = int(input())
dp = [[1, []] for _ in range(N+1)]

# 초기화
dp[1][0] = 0
dp[1][1] = [1]

for i in range(2, N+1) :

        
    # 1을 뺄 때
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + [i]

    # 2로 나누어 떨어질 때
    if i % 2 == 0 and dp[i//2][0] + 1 < dp[i][0] :
        dp[i][0] = dp[i//2][0] + 1
        dp[i][1] = dp[i//2][1] + [i]
        mod2 = True

    if i % 3 == 0 and dp[i//3][0] + 1 < dp[i][0] :
        dp[i][0] = dp[i//3][0] + 1
        dp[i][1] = dp[i//3][1] + [i]
        mod3 = True

# 연산 최소 회수 출력
print(dp[N][0])

# 과정 뒤집기 및 출력
dp[N][1].reverse()
for i in dp[N][1] :
    print(i, end=" ")
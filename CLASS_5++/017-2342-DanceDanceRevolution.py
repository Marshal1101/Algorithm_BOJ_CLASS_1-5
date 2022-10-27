import sys


def move(a, b) :
    if a == b :
        return 1
    elif a == 0 :
        return 2
    elif abs(a - b) == 2 :
        return 4
    else :
        return 3    


def main() :
    INF = sys.maxsize
    arr = list(map(int, sys.stdin.readline().split()))
    N = len(arr)
    dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(N+1)]
    dp[0][0][0] = 0

    for i in range(1, N+1) :
        target = arr[i-1]
        for left in range(5) :
            for right in range(5) : 
                dp[i][left][target] = temp1 if (temp1 := dp[i][left][target]) < (temp2 := dp[i-1][left][right] + move(right, target)) else temp2
                dp[i][target][right] = temp1 if (temp1 := dp[i][target][right]) < (temp2 := dp[i-1][left][right] + move(left, target)) else temp2

    result = INF
    for i in range(5) :
        for j in range(5) :
            result = result if result < (temp := dp[N-1][i][j]) else temp

    print(result) 


if __name__ == '__main__' :
    main()
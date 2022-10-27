import sys
sys.setrecursionlimit(10**9)

def palindrome(s, e, arr, dp) :
    if s == e :
        return 1
    elif s + 1 == e :
        if arr[s] == arr[e] :
            return 1
        else :
            return 0

    if dp[s][e] != -1 :
        return dp[s][e]

    if arr[s] != arr[e] :
        dp[s][e] = 0
    else :
        dp[s][e] = palindrome(s+1, e-1, arr, dp)
    return dp[s][e]
            

def main() :
    input = sys.stdin.readline
    N = int(input())
    arr = input().split()
    M = int(input())
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N) :
        dp[i][i] = 1
    for _ in range(M) :
        s_idx, e_idx = map(lambda x: int(x)-1, input().split())
        print(palindrome(s_idx, e_idx, arr, dp))

if __name__ == '__main__' :
    main()
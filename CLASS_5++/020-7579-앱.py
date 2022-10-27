import sys


def main() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    m = list(map(int, input().split()))
    c = list(map(int, input().split()))

    c_tot = sum(c)

    dp = [[ 0 for _ in range(c_tot+1)] for _ in range(N)]
    for i in range(N) :
        mem, cost = m[i], c[i]
        if cost == 0 : dp[i][0] = mem
        for j in range(1, c_tot+1) :
            a = dp[i-1][j]
            b = dp[i-1][j-cost] + mem
            if j >= cost :
                dp[i][j] = b if (b := dp[i-1][j-cost] + mem) > (a := dp[i-1][j]) else a
            else :
                dp[i][j] = dp[i-1][j]

    # for p in dp :
    #     print(p)
    for j in range(c_tot+1) :
        for i in range(N) :
            if dp[i][j] >= M :
                print(j)
                exit()


if __name__ == '__main__' :
    main()
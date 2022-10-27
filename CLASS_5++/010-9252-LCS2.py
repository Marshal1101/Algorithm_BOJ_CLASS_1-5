import sys


def main() :
    input = sys.stdin.readline
    str1 = list(input().rstrip())
    str2 = list(input().rstrip())
    leng1 = len(str1)
    leng2 = len(str2)

    dp = [[[0, ""] for _ in range(leng1+1)] for _ in range(leng2+1)]

    for i in range(1, leng2 + 1) :
        for j in range(1, leng1 + 1) :
            if str2[i-1] == str1[j-1] :
                dp[i][j][0] = dp[i-1][j-1][0] + 1
                dp[i][j][1] += dp[i-1][j-1][1] + str2[i-1]
            else :
                # dp[i][j][0] = max(dp[i-1][j-1][0], dp[i-1][j][0], dp[i][j-1][0])
                leftup = dp[i-1][j-1][0]
                left = dp[i][j-1][0]
                up = dp[i-1][j][0]
                if leftup >= up and leftup > left :
                    dp[i][j][0] = leftup
                    dp[i][j][1] = dp[i-1][j-1][1]
                
                elif (up > leftup and up > left) :
                    dp[i][j][0] = up
                    dp[i][j][1] = dp[i-1][j][1]

                else :
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i][j-1][1]

    # for line in dp :
    #     print(line)

    print(dp[leng2][leng1][0])
    print(dp[leng2][leng1][1])


if __name__ == '__main__' :
    main()
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    k = int(input())
    n = int(input())

    floor = [[i for i in range(n+1)] for _ in range(k+1)]
    # print(floor)
    for i in range(1, k+1) :
        floor[i][0] = 0
        for j in range(1, n+1) :
            floor[i][j] = floor[i][j-1] + floor[i-1][j]

    print(floor[k][n])
N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
result = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
result[0][1][0] = 1
for i in range(N):
    for j in range(2, N):
        if data[i][j] == 0:
            result[i][j][0] = result[i][j - 1][0] + result[i][j - 1][2]
            if i > 0:
                result[i][j][1] = result[i - 1][j][1] + result[i - 1][j][2]
                if data[i - 1][j] == 0 and data[i][j - 1] == 0:
                    result[i][j][2] = result[i - 1][j - 1][0] + result[i - 1][j - 1][1] + result[i - 1][j - 1][2]
print(sum(result[N - 1][N - 1]))

import sys

input = sys.stdin.readline


N = int(input())
house = []
for _ in range(N) :
    house.append(list(input().strip()))

result = []
def bfs(y, x) :
    house[y][x] = '0'
    que = [(y, x)]
    ptr = 0
    cnt = 0
    while len(que) > ptr :
        i, j = que[ptr]
        ptr += 1
        if i + 1 < N and house[i+1][j] == '1' :
            house[i+1][j] = '0'
            que.append((i+1, j))
        if i - 1 >= 0 and house[i-1][j] == '1' :
            house[i-1][j] = '0'
            que.append((i-1, j))
        if j + 1 < N and house[i][j+1] == '1' :
            house[i][j+1] = '0'
            que.append((i, j+1))
        if j - 1 >= 0 and house[i][j-1] == '1' :
            house[i][j-1] = '0'
            que.append((i, j-1))
    
    result.append(ptr)

for i in range(N) :
    for j in range(N) :
        if house[i][j] != '0' :
            bfs(i, j)

result.sort()
print(len(result))
for num in result :
    print(num)
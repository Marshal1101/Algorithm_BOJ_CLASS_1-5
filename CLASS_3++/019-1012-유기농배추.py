import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_x, start_y, ground) :
    ground[start_y][start_x] = 0
    que = [[start_x, start_y]]
    ptr = 0
    while len(que) > ptr :
        x, y = que[ptr]
        ptr += 1
        i = [-1, 1, 0, 0]
        j = [0, 0, -1, 1]
        for k in range(4) :
            ny = y + i[k]
            nx = x + j[k]
            if 0 <= ny < N and 0 <= nx < M :
                if ground[ny][nx] == 1 :
                    ground[ny][nx] = 0
                    que.append([nx, ny])
    return 1

T = int(input())
res = []
for _ in range(T) :
    M, N, K = map(int, input().split())
    ground = [ [ 0 for _ in range(M)] for _ in range(N) ]
    cab_pos = deque([])
    for _ in range(K) :
        x, y = map(int, input().split())
        ground[y][x] = 1
        cab_pos.append([x, y])

    warm = 0
    while cab_pos :
        x, y = cab_pos.popleft()
        if ground[y][x] != 0 :
            warm += bfs(x, y, ground)
    res.append(str(warm))

print('\n'.join(res))
import sys
from heapq import heappush, heappop
input = sys.stdin.readline


N = int(input())
sea = []
fish = [0] * 20
for i in range(N) :
    row_i = list(map(int, input().split()))
    sea.append(row_i)
    for fish_size in row_i :
        if fish_size :
            fish[fish_size] += 1
fish[9] = 0
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def find_shark(list) :
    for i in range(N) :
        for j in range(N) :
            if list[i][j] == 9 :
                return (i, j)

def bfs(y, x, ate, size, time) :
    if sum(fish[1:size]) == 0 :
        print(time)
        return

    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[y][x] = True
    sea[y][x] = 0
    new_t = time
    que = [(y, x)]
    while que :
        length = len(que)
        next_q = []
        eat_q = []
        # print('time:', time, 'que:', que)
        for _ in range(length) :
            i, j = heappop(que)
            for dy, dx in d :
                ni = i + dy
                nj = j + dx
                if 0 <= ni < N and 0 <= nj < N :
                    if not visited[ni][nj] and sea[ni][nj] <= size :
                        visited[ni][nj] = True
                        if 0 < sea[ni][nj] < size :
                            if ate + 1 == size :
                                heappush(eat_q, (ni, nj, 0, size+1, new_t+1))
                            else :
                                heappush(eat_q, (ni, nj, ate+1, size, new_t+1))
                            # print('time:', time, 'eat+ fish:', sea[ni][nj], 'at:(', ni, ',', nj, ') ate:', ate+1, 'size:', size)
                        else : heappush(next_q, (ni, nj))
        
        if eat_q :
            # print('time:', time, 'eat_q:', eat_q)
            ny, nx, eat, level, t = heappop(eat_q)
            fish[sea[ny][nx]] -= 1
            bfs(ny, nx, eat, level, t)
            return
        if not next_q :
            print(time)
        que = next_q
        new_t += 1

sy, sx = find_shark(sea)
bfs(sy, sx, 0, 2, 0)
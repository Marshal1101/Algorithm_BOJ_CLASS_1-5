import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
box = []
for _ in range(N) :
    box.append(list(map(int, input().split())))

def tomato(M, N) :
    total = M * N
    empty = 0
    red = 0
    que = deque([])
    for i in range(N) :
        for j in range(M) :
            if box[i][j] == 1 :
                red += 1
                que.append((i, j))
            elif box[i][j] == -1 :
                empty += 1
                box[i][j] == 1

    green = total - empty - red
    if green == 0 : return 0

    day = 0
    while que :
        new_que = deque([])
        green_to_red = 0
        while que :
            y, x = que.popleft()
            if y - 1 >= 0 and box[y-1][x] == 0 :
                box[y-1][x] = 1
                new_que.append((y-1, x))
                green_to_red += 1
            if y + 1 < N and box[y+1][x] == 0 :
                box[y+1][x] = 1
                new_que.append((y+1, x))
                green_to_red += 1
            if x - 1 >= 0 and box[y][x-1] == 0 :
                box[y][x-1] = 1
                new_que.append((y, x-1))
                green_to_red += 1
            if x + 1 < M and box[y][x+1] == 0 :
                box[y][x+1] = 1
                new_que.append((y, x+1))
                green_to_red += 1
        
        day += 1
        red += green_to_red
        green -= green_to_red
        
        if green == 0 : return day
        else : que = new_que

    return -1

print(tomato(M, N))
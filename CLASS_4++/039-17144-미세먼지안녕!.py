## pypy

import sys; input = sys.stdin.readline

R, C, T = map(int, input().split())
graph = []
for _ in range(R) :
    graph.append(list(map(int, input().split())))

def count_dirt(graph) :
    dirt_pos = []
    filter_i = []
    for i in range(R) :
        for j in range(C) :
            if graph[i][j] :
                if graph[i][j] != -1 :
                    dirt_pos.append((i, j))
                else :
                    filter_i.append(i)
    return [dirt_pos, filter_i]

def move_on_graph(new_graph, filter_pos) :
    up, down = filter_pos
    
    # 상단 흡기
    for i in range(up-1, 0, -1) :
        new_graph[i][0] = new_graph[i-1][0]
    
    # 0행 서풍
    for j in range(C-1) :
        new_graph[0][j] = new_graph[0][j+1]

    # C-1열 북풍
    for i in range(up) :
        new_graph[i][C-1] = new_graph[i+1][C-1]

    # 상단 나오는 바람
    for j in range(C-1, 1, -1) :
        new_graph[up][j] = new_graph[up][j-1]
    new_graph[up][1] = 0
    
    # 하단 흡기
    for i in range(down+1, R-1) :
        new_graph[i][0] = new_graph[i+1][0]

    # R-1행 동풍
    for j in range(C-1) :
        new_graph[R-1][j] = new_graph[R-1][j+1]
    
    # C-1열 남풍
    for i in range(R-1, down, -1) :
        new_graph[i][C-1] = new_graph[i-1][C-1]

    # 하단 나오는 바람
    for j in range(C-1, 1, -1) :
        new_graph[down][j] = new_graph[down][j-1]
    new_graph[down][1] = 0

    return new_graph

dirt_pos, filter_i = count_dirt(graph)
up, down = filter_i
time = 0
while dirt_pos :
    length = len(dirt_pos)
    new_graph = [line[:] for line in graph]
    for _ in range(length) :
        y, x = dirt_pos.pop()
        if graph[y][x] == -1 : continue

        cnt = 0
        amount = graph[y][x] // 5
        if amount == 0 : continue

        if y - 1 >= 0 and graph[y-1][x] != -1 :
            cnt += 1
            new_graph[y-1][x] += amount

        if y + 1 < R and graph[y+1][x] != -1 :
            cnt += 1
            new_graph[y+1][x] += amount

        if x - 1 >= 0 and graph[y][x-1] != -1 :
            cnt += 1
            new_graph[y][x-1] += amount

        if x + 1 < C and graph[y][x+1] != -1 :
            cnt += 1
            new_graph[y][x+1] += amount

        if cnt :
            new_graph[y][x] -= amount * cnt

    graph = move_on_graph(new_graph, filter_i)
    time += 1
    
    if time == T :
        total = 2
        for line in graph :
            total += sum(line)
        print(total)
        break

    dirt_pos, _ = count_dirt(graph)
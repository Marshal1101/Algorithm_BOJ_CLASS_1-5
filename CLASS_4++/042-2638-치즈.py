import sys, collections; 

def air_check(N, M, graph) :
    visited = [[False] * M for _ in range(N)]
    que = collections.deque([(0, 0)])
    visited[0][0] = True
    deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while que :
        y, x = que.popleft()
        for di, dj in deltas :
            if (0 <= (ny := y + di) < N
                and 0 <= (nx := x + dj) < M
                and not visited[ny][nx]
                and graph[ny][nx] == "0") :
                visited[ny][nx] = True
                que.append((ny, nx))
    return visited

def main() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    graph = []
    for _ in range(N) :
        graph.append(input().split())

    cheese_q = collections.deque([])
    for i in range(N) :
        for j in range(M) :
            if graph[i][j] == "1" :
                cheese_q.append((i, j))
    
    hours = 0
    deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while cheese_q :
        length = len(cheese_q)
        is_insulted = air_check(N, M, graph)
        new_graph = [row[:] for row in graph]
        for _ in range(length) :
            expo_cnt = 0
            y, x = cheese_q.popleft()
            for di, dj in deltas :
                if (0 <= (ny := y + di) < N
                    and 0 <= (nx := x + dj) < M
                    and graph[ny][nx] == "0"
                    and is_insulted[ny][nx]) :
                    expo_cnt += 1
            if expo_cnt > 1 : new_graph[y][x] = "0"
            else : cheese_q.append((y, x))
        graph = new_graph
        hours += 1
        # print('time:', time)
        # for i in new_graph :
        #     print(i)
        
    print(hours)

if __name__ == '__main__':
    main()
## DFS

import sys
sys.setrecursionlimit(10**9)

def circle(graph, cur, start, cnt) :
    # print(cur, start, cnt)
    if graph[cur] != start :
        cnt = circle(graph, graph[cur], start, cnt + 1)
    return cnt

def find(graph, i, visited, path) :
    # print('stu:', i)
    if not visited[i] :
        if graph[i] != i :
            visited[i] = True
            path.add(i)
            cnt = find(graph, graph[i], visited, path)
        else :
            if i in path :
                return 1
            else :
                return 0
    else :
        if i in path :
            # 사이클
            cnt = circle(graph, i, i, 1)
        else :
            return 0
    return cnt

def main() :
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T) :
        N = int(input())

        graph = [0] * (N+1)
        visited = [False] * (N+1)
        for i, sel in zip(range(1, N+1), map(int, input().split())) :
            graph[i] = sel
        
        circled_cnt = 0
        for i in range(1, N+1) :
            if not visited[i] :
                path = set([i])
                cnt = find(graph, i, visited, path)
                circled_cnt += cnt
        print(N - circled_cnt)


if __name__ == '__main__' :
    main()
import sys; input = sys.stdin.readline

def main() :
    V = int(input())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    global max_dist
    max_dist = 0
    for _ in range(V) :
        line = list(map(int, input().split()))
        length = len(line)
        for i in range(1, length, 2) :
            if line[i] != -1 :
                graph[line[0]].append((line[i], line[i+1]))
    visited[1] = True
    dfs(1, graph, visited)
    print(max_dist)

def dfs(s_node, graph, visited) :
    global max_dist
    max1, max2 = 0, 0
    for adj, d in graph[s_node] :
        if not visited[adj] :
            visited[adj] = True
            ret = dfs(adj, graph, visited)
            if (temp := ret + d) > max1 :
                max2 = max1
                max1 = temp
            elif temp > max2 :
                max2 = temp
    if (temp := max1 + max2) > max_dist :
        max_dist = temp
    return max1

if __name__ == '__main__' :
    main()
import sys

all = sys.stdin.readlines()

N = int(all.pop(0))
graph = [[] for _ in range(N+1)]

for input in all :
    v1, v2 = map(int, input.split())
    graph[v1].append(v2)
    graph[v2].append(v1)

parent = [ '-1' for _ in range(N+1) ]

def bfs(start) :
    parent[start] = '0'
    que = [start]
    ptr = 0
    while len(que) > ptr:
        node = que[ptr]
        for adj in graph[node] :
            if parent[adj] == '-1' :
                parent[adj] = str(node)
                que.append(adj)
        ptr += 1
    
    print('\n'.join(parent[2:]))

bfs(1)
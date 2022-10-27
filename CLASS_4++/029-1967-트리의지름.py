import sys; input = sys.stdin.readline
from collections import deque
from heapq import heappush, heappushpop

N = int(input())
graph = [ [] for _ in range(N+1) ]
indegree = [ 0 for _ in range(N+1) ]
for _ in range(N-1) :
    p, c, w = map(int, input().split())
    graph[c].append((p, w))
    indegree[p] += 1

w_max = [ 0 for _ in range(N+1) ]
w_total = [ [] for _ in range(N+1) ]
w_total_max = 0

def topology() :
    global w_total_max
    que = deque([])
    half = []
    for i in range(1, N+1) :
        if not indegree[i] :
            que.append(i)
        elif indegree[i] == 1 :
            half.append(i)

    while que :
        c = que.popleft()
        for p, w in graph[c] :
            indegree[p] -= 1
            nw = w + w_max[c]
            if nw > w_max[p] :
                w_max[p] = nw
            if len(w_total[p]) < 2 :
                heappush(w_total[p], nw)
            else : 
                heappushpop(w_total[p], nw)
            if not indegree[p] :
                temp = sum(w_total[p])
                if temp > w_total_max and (not p in half or p == 1) :
                    w_total_max = temp
                que.append(p)

topology()
print(w_total_max)
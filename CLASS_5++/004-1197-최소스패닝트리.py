## 03 1197 최소 스패닝 트리
# 프림 알고리즘


import sys, heapq

V, E = map(int, sys.stdin.readline().strip().split())

# arr: 인접 리스트
# 정점1(v1) 정점2(v2) 인덱스에 [간선, 가중치] 값 추가
# 정점번호-1 = 인덱스
arr = [[] for _ in range(V)]
for _ in range(E):
    v1, v2, d = map(int, sys.stdin.readline().strip().split())
    arr[v1-1].append([v2-1, d])
    arr[v2-1].append([v1-1, d])

### Prim
# 큐, 가중치, 방문 회수
# 정점 방문 여부 리스트(인덱스i:정점i 방문되면 True)
# 힙 푸시: dist, start vertex
que, dist, cnt = [], 0, 0 
vi = [False for _ in range(V)] 
heapq.heappush(que, (0, 0)) 


# que 안에는 가중치(d) 기준 최소 힙 정렬됨
# way는 [간선 인접 정점, 간선 가중치]
while cnt < V:
    (d, v2) = heapq.heappop(que)
    if not vi[v2]:
        vi[v2] = True
        dist += d
        cnt += 1

        for way in arr[v2]:
            if not vi[way[0]]:
                heapq.heappush(que, [way[1], way[0]])

print(dist)
from heapq import heappop, heappush
import sys

input = sys.stdin.readline

k = int(input())
for i in range(k) :
    n = int(input())
    min_heap = []
    max_heap = []
    heap_cnt = 0
    visited = [False] * n
    for j in range(n) :
        order, num = input().split()
        if order == "I" :
            heappush(min_heap, [int(num), j])
            heappush(max_heap, [-int(num), j])
            visited[j] = True
            heap_cnt += 1
        elif order == "D" :
            if heap_cnt > 0 :
                if num == "-1" :
                    while min_heap and visited[min_heap[0][1]] == False :
                        heappop(min_heap)
                    visited[heappop(min_heap)[1]] = False
                elif num == "1" :
                    while max_heap and visited[max_heap[0][1]] == False :
                        heappop(max_heap)
                    visited[heappop(max_heap)[1]] = False
                heap_cnt -= 1
                    
    if heap_cnt > 0 :
        while min_heap and visited[min_heap[0][1]] == False :
            heappop(min_heap)
        while max_heap and visited[max_heap[0][1]] == False :
            heappop(max_heap)
        print(-heappop(max_heap)[0], heappop(min_heap)[0])
    else :
        print("EMPTY")
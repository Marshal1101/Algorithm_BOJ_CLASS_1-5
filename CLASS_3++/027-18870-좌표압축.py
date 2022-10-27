import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
heap_arr = []
for n in arr :
    heappush(heap_arr, n)
order = {}
i = 0
k = -1
ex_num = 10000000000
while i < N :
    num = heappop(heap_arr)
    if num != ex_num :
        k += 1
        order[num] = k
        ex_num = num
    else : order[num] = k
    i += 1

for num in arr :
    print(order[num], end=" ")
import sys
from heapq import heappop, heappush
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
heap = []
checklist = defaultdict(int)
length = 0
res = ''
for i in range(N) :
    num = int(input())
    if num == 0 :
        if length > 0 :
            mini = heappop(heap)
            if checklist[-mini] > 0 :
                checklist[-mini] -= 1
                res += str(-mini) + '\n'
            else :
                checklist[mini] -= 1
                res += str(mini) + '\n'
            length -= 1
            # print('heap', heap)
        else : res += '0\n'
    else :
        if num > 0 :
            heappush(heap, num)
        else :
            heappush(heap, -num)
        checklist[num] += 1
        length += 1
print(res)
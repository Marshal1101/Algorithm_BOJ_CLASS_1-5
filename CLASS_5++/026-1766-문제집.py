"""
problem url: https://www.acmicpc.net/problem/1766
"""

import sys
from heapq import heappop, heappush
from collections import defaultdict

def main() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    
    indegree = [0] * (N+1)
    order = defaultdict(list)
    for _ in range(M) :
        v1, v2 = map(int, input().split())
        order[v1].append(v2)
        indegree[v2] += 1
    hq = [i for i in range(1, N+1) if not indegree[i]]
    res = ""
    while hq :
        p = heappop(hq)
        for adj in order[p] :
            indegree[adj] -= 1
            if not indegree[adj] :
                heappush(hq, adj)
        res += str(p) + " "

    return res


if __name__ == '__main__' :
    print(main())
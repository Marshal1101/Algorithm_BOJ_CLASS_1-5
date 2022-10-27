from collections import deque
import sys

input = sys.stdin.readline

def solution() :
    res = []
    T = int(input())
    for _ in range(T) :
        N, M = map(int, input().split())
        que = deque([i for i in range(N)])
        arr = list(map(int, input().split()))
        priorities = {}
        for i in range(N) :
            priorities[i] = arr[i]
        arr.sort(reverse=True)
        def find(M) :
            order = 0
            for prio in arr :
                while True :
                    paper_num = que.popleft()
                    if priorities[paper_num] != prio :
                        que.append(paper_num)
                    else : 
                        order += 1
                        if paper_num == M : 
                            print(order)
                            return
                        break
        find(M)
solution()
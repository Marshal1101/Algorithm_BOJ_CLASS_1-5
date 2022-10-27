## https://www.acmicpc.net/source/40457581

import sys
from heapq import heappop as hpop, heappush as hpush
from collections import defaultdict
input = sys.stdin.readline

def solution(input):
    for _ in range(int(input())):
        minQ = []
        maxQ = []
        counter = defaultdict(int)
        length = 0
        for _ in range(int(input())):
            command, i = input().split()
            if command == "I":
                i = int(i)
                hpush(minQ, i)
                hpush(maxQ, -i)
                length += 1
                counter[i] += 1
            elif command == "D":
                if length:
                    if i == "1":
                        while maxQ and counter[-maxQ[0]] == 0: 
                            hpop(maxQ)
                        d = -hpop(maxQ)
                    elif i == "-1":
                        while minQ and counter[minQ[0]] == 0:
                            hpop(minQ)
                        d = hpop(minQ)
                    counter[d] -= 1
                    length -= 1
                    if length == 0:
                        minQ.clear()
                        maxQ.clear()
                        counter.clear()
    
        if length :
            while maxQ and counter[-maxQ[0]] == 0: 
                hpop(maxQ)
            while minQ and counter[minQ[0]] == 0:
                hpop(minQ)
            print(-maxQ[0], minQ[0])
        else: print("EMPTY")

solution(input)
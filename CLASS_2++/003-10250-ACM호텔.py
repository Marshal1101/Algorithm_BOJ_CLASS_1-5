import sys, math


input = sys.stdin.readline


T = int(input())
for _ in range(T) :
    H, W, N = map(int, input().split(' '))
    floor = N % H
    if (floor == 0) : floor = H
    room = math.ceil(N / H)
    if (room > 9) : print(str(floor) + str(room))
    else : print(str(floor) + '0' + str(room))
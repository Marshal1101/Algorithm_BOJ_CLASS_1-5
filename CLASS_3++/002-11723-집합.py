import sys

input = sys.stdin.readline


M = int(input())

S = [ 0 for _ in range(21) ]
i = 0
while i < M :
    line = input().split()
    if line[0] == 'add' :
        S[int(line[1])] = 1
    elif line[0] == 'remove' :
        S[int(line[1])] = 0
    elif line[0] == 'check' :
        if S[int(line[1])] : print(1)
        else : print(0)
    elif line[0] == 'toggle' :
        if S[int(line[1])] : S[int(line[1])] = 0
        else : S[int(line[1])] = 1
    if line[0] == 'all' :
        S = [ 1 for _ in range(21) ]
    elif line[0] == 'empty' :
        S = [ 0 for _ in range(21) ]

    i += 1
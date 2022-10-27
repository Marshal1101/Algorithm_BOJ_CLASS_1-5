import sys

input = sys.stdin.readline

N = int(input())
person = [0] * N
for i in range(N) :
    person[i] = list(map(int, input().split(' ')))

for i in person :
    rank = 1
    for j in person :
        if i[0] < j[0] and i[1] < j[1] :
            rank += 1        
    print(rank, end=" ")
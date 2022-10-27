import sys

input = sys.stdin.readline

N, M = map(int, input().split())
total = [0]
for num in map(int, input().split()) :
    total.append(total[-1] + num)

for _ in range(M) :
    i, j = map(int, input().split())
    print(total[j] - total[i-1])
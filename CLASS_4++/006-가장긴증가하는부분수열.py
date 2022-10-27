import sys

n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
cache = [0] * n

for i in range(n):
    for j in range(i):
        if data[i] > data[j] and cache[i] < cache[j]:
            cache[i] = cache[j]
    cache[i] += 1

print(max(cache))
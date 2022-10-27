import sys


input = sys.stdin.readline


n = int(input())
points = list(map(int, input().split(' ')))
total = 0
max_point = 0
for point in points :
    total += point
    if (max_point < point) :
        max_point = point

print(f'{(total/max_point/n*100)}')
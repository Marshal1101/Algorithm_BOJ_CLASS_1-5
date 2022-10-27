import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
waiting = 0
total = 0
for time in arr :
    waiting += time
    total += waiting

print(total)
import sys

input = sys.stdin.readline

k, n = map(int, input().split())
arr = list(int(input()) for _ in range(k))
arr.sort(reverse=True)
lp = 1
rp = arr[0]
cnt = 0
maxLen = 0
while (lp <= rp) :
    cnt = 0
    mid = (lp + rp) // 2
    for line in arr :
        cnt += line // mid
    if cnt < n :
        rp = mid - 1
    else :
        maxLen = max(maxLen, mid)
        lp = mid + 1

print(maxLen)
## https://www.acmicpc.net/source/25627611
## 정규식

import sys, re
input = sys.stdin.readline
N = int(input())
M = int(input())
s = input().strip()

s = re.sub('OO+', ' ', s)
s = re.sub('II+', 'I I', s)
print(s)
answer = 0
for x in map(lambda x : (len(x) -1)// 2, s.split(' ')):
    if x >= N : answer += x + 1 - N
print(answer)
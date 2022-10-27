## https://www.acmicpc.net/source/10832460

import sys
n, m = map(int, input().split())
nameList = sys.stdin.read().splitlines()
print(nameList)
hearset = set(nameList[:n])
seeset = set(nameList[n:])
ret = list(hearset & seeset)
ret.sort()
print(len(ret))
for i in ret:
    print(i)
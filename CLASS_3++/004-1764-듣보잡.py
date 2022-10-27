import sys

input = sys.stdin.readline

N, M = map(int, input().split())
listened = {}
cnt = 0
res = []
for i in range(N) :
    listened[input().rstrip()] = 1
for i in range(M) :
    ask = input().rstrip()
    try :
        if listened[ask] :
            res.append(ask)
            cnt += 1
    except : 
        continue
res.sort()
print(cnt)
print('\n'.join(res))
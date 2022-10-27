import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [False] * (N)
count = defaultdict(int) 
for num in arr :
    count[num] += 1

def dfs(start, cnt, res) :
    if cnt == 0 :
        print(res)
        return

    ## set으로 현재 자리수 숫자 방문 체크, 중복 방지
    visit_set = set(arr)
    for i in range(start, N) :
        if arr[i] in visit_set :
            ## 숫자 개수 소모로 전체 방문된 숫자 제어
            if count[arr[i]] :
                count[arr[i]] -= 1
                visit_set.remove(arr[i])
                new_res = res + str(arr[i]) + ' '
                dfs(start, cnt - 1, new_res)
                count[arr[i]] += 1

dfs(0, M, '')
## https://www.acmicpc.net/source/15218002

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
adj = [list() for i in range(n+1)]
bacon = [[sys.maxsize] * (n+1) for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


def dfs(x, visited, path, origin, cnt):
    bacon[origin][x] = min(cnt, bacon[origin][x])
    for a in adj[x]:
        if not visited[a]:
            visited[a] = True
            if bacon[origin][a] > cnt + 1:
                dfs(a, visited, path + [a], origin, cnt + 1)
            visited[a] = False
    return cnt


result = sys.maxsize
person = -1
for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i, visited, [], i, 0)
    s = sum(bacon[i][1:])
    if result > s:
        result = s
        person = i

print(person)
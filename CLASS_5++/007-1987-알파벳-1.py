## https://www.acmicpc.net/source/45361190

r, c = map(int, input().split())

b = []
for i in range(r):
    b.append(list(input()))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# lst = [] # 지나온 알파벳
answer = 1

def bfs(x, y):
    global answer
    q = set([(x, y, b[x][y])])
    while q:
        xx, yy, a = q.pop()

        for i in range(4):
            nx = dx[i] + xx
            ny = dy[i] + yy
            if (0 <= nx < r) and (0 <= ny < c) and (b[nx][ny] not in a):
                q.add((nx, ny, a+b[nx][ny]))
                answer = max(answer, len(a)+1)
# 최대길이
bfs(0,0)
print(answer)
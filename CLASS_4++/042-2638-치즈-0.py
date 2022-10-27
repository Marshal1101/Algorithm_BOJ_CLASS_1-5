## https://www.acmicpc.net/source/28964248


import sys

input = sys.stdin.readline

def solution(N, M, paper):
    cheese = []
    for i in range(N):
        for j in range(M):
            if paper[i][j] == 1: cheese.append((i, j))

    dx = [1, -1, 0, 0]; dy = [0, 0, 1, -1]
    num = len(cheese)
    answer = 0
    q = [(0, 0)]
    while num > 0:
        nextQ = []; qIdx = 0
        while len(q) != qIdx:
            c = q[qIdx]; qIdx += 1
            for i in range(4):
                nx = c[0] + dx[i]; ny = c[1] + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if paper[nx][ny] == 0:
                        paper[nx][ny] = -1
                        q.append((nx, ny))
                    elif paper[nx][ny] > 0:
                        paper[nx][ny] += 1
                        if paper[nx][ny] > 2:
                            nextQ.append((nx, ny))
                            paper[nx][ny] = -1
                            num -= 1
        
        answer += 1
        q = nextQ

    return answer

if __name__ == '__main__':
    N, M = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(N)]

    print(solution(N, M, paper))
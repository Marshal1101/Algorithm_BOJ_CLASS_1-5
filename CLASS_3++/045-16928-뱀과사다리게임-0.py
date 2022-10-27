## https://www.acmicpc.net/source/33025819
## BFS : 모두 공평하게 단계 +1씩 돌아가면서 찾으므로 조건 만족 시 최소값 충족가능


import sys

N, M = map(int, sys.stdin.readline().split())
teleport = [0 for _ in range(101)]

for _ in range(N+M):
    start, end = map(int, sys.stdin.readline().split())
    teleport[start] = end

visit = [False for _ in range(101)]
q = []

visit[1] = True
q.append(1)


def BOJ16928():
    cnt = 0
    while len(q) != 0:

        qSize = len(q)

        for _ in range(qSize):
            n = q.pop(0)

            for dice in range(6):
                move = n + dice + 1

                if move > 100:
                    continue

                if move == 100:
                    print(cnt+1)
                    return

                if teleport[move] != 0:
                    if not visit[teleport[move]]:
                        visit[teleport[move]] = True
                        q.append(teleport[move])
                else:
                    if not visit[move]:
                        visit[move] = True
                        q.append(move)

        cnt += 1


BOJ16928()

"""
https://www.acmicpc.net/source/40167809
https://jintak0401.github.io/
"""


from sys import stdin

input = stdin.readline


def solve():
    N, M = map(int, input().split())

    arr = ''
    for i in range(N):
        arr += input()[:-1]

    def adj(k):
        i, j = k // M, k % M
        # 상
        if i > 0:
            yield k - M
        # 하
        if i < N - 1:
            yield k + M
        # 좌
        if j > 0:
            yield k - 1
        # 우
        if j < M - 1:
            yield k + 1

    # 각 공간과 벽에 방문했는지 여부
    visited = [False] * (N * M)

    ans = [0 if arr[i] == '0' else 1 for i in range(len(arr))]

    def bfs(pos):
        visited[pos] = True
        que = [pos]
        wall = []
        count = 0
        while True:
            if not que:
                break
            new_que = []
            while que:
                cur_pos = que.pop()
                count += 1
                # 인접한 칸들에 대해서
                for around in adj(cur_pos):
                    # 방문하지 않았다면
                    if not visited[around]:
                        visited[around] = True
                        if arr[around] == '0':
                            new_que.append(around)
                        else:
                            wall.append(around)

            que = new_que

        for pos in wall:
            ans[pos] = (ans[pos] + count) % 10
            # 벽의 반대편 빈 칸에 대해서도 계산되어야 하므로 visited를 False로 해준다
            visited[pos] = False

    # 빈 칸일 경우 bfs 실행
    for i in range(N * M):
        if arr[i] == '0' and not visited[i]:
            bfs(i)

    # 답 출력
    for i in range(N):
        print(*ans[i*M:(i+1)*M], sep='')


if __name__ == '__main__':
    solve()

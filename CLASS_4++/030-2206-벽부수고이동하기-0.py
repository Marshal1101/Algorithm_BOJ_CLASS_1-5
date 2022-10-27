## https://www.acmicpc.net/source/30819840

import sys

input = sys.stdin.readline


def sol2206():
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    nw = {'0', '2'}
    q = [(0, 0, 2)]
    answer = 1
    while q:
        nq = []
        for r, c, w in q:
            if r == n - 1 and c == m - 1:
                return answer
            
            for nr, nc in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc]!='3':
                    if w == 1:
                        if board[nr][nc] == '0':
                            board[nr][nc] = '2'
                            nq.append((nr, nc, 1))
                    else:
                        if board[nr][nc] == '1':
                            nq.append((nr, nc, 1))
                        elif board[nr][nc] in nw:
                            nq.append((nr, nc, 2))
                        board[nr][nc] = '3'
        answer += 1
        q = nq
    return -1


if __name__ == '__main__':
    print(sol2206())
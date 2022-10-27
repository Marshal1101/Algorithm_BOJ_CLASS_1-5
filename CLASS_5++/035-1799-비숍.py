import sys


def dfs(cnt, N, k, diaonal_neg, board):
    global max_cnt 
    if cnt > max_cnt: max_cnt = cnt
    if k > 2*N-1: return
    if cnt + 2*(N-1) - k < max_cnt: return
    
    if k < N:
        s = 0
        e = k + 1
    else:
        s = k - N + 1
        e = N
    for i in range(s, e):
        j = k - i
        if board[i][j] and not diaonal_neg[N-1+i-j]:
            diaonal_neg[N-1+i-j] = True
            dfs(cnt+1, N, k+1, diaonal_neg, board)
            diaonal_neg[N-1+i-j] = False
    dfs(cnt, N, k+1, diaonal_neg, board)

        
def main():
    input = sys.stdin.readline
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    diaonal_neg = [False] * (2*N-1)
    global max_cnt
    max_cnt = 0
    dfs(0, N, 0, diaonal_neg, board)
    print(max_cnt)


if __name__ == '__main__':
    main()
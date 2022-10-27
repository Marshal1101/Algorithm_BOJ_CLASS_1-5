import sys


def move_dir(N, board, dir) :
    if dir == 0 :
        for i in range(N) :
            set_up(i, N, board, i)
        
    elif dir == 1 :
        for i in range(N*N-1, N*N-N-1, -1) :
            set_down(i, N, board, i)

    elif dir == 2 :
        for i in range(0, N*N, N) :
            set_left(i, i+N, N, board, i)

    else :
        for i in range(N-1, N*N, N) :
            set_right(i, i-N, N, board, i)

    # print('dir:', dir, "==================")
    # for i in range(N*N) :
    #     print(board[i], end=" ")
    #     if (i+1) % N == 0: print()

    return board


def set_up(i, N, board, ptr) :
    # print('i:', i, 'ptr:', ptr, 'bi:', board[i])

    ni = i + N
    while ni < N*N and board[ni] == 0 :
        ni += N

    if i >= N*(N-1) or ni >= N*N :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        # print("======i ni == N ======")
        return

    if board[i] == board[ni] :
        board[ptr] = 2 * board[i]
        if ptr != i : board[i] = 0
        board[ni] = 0
        ptr += N
    elif board[i] != 0 :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        ptr += N
            
    set_up(ni, N, board, ptr)


def set_down(i, N, board, ptr) :
    # print('i:', i, 'ptr:', ptr, 'bi:', board[i])

    ni = i - N
    while ni >= 0 and board[ni] == 0 :
        ni -= N

    if i < N or ni < 0 :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        # print("======i ni == N ======")
        return

    if board[i] == board[ni] :
        board[ptr] = 2 * board[i]
        if ptr != i : board[i] = 0
        board[ni] = 0
        ptr -= N
    elif board[i] != 0 :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        ptr -= N
            
    set_down(ni, N, board, ptr)


def set_left(i, end, N, board, ptr) :
    # print('i:', i, 'ptr:', ptr, 'bi:', board[i])

    ni = i + 1
    while ni < end and board[ni] == 0 :
        ni += 1

    if i >= end-1 or ni >= end :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        # print("======i ni == N ======")
        return

    if board[i] == board[ni] :
        board[ptr] = 2 * board[i]
        if ptr != i : board[i] = 0
        board[ni] = 0
        ptr += 1
    elif board[i] != 0 :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        ptr += 1
            
    set_left(ni, end, N, board, ptr)


def set_right(i, end, N, board, ptr) :
    # print('i:', i, 'ptr:', ptr, 'bi:', board[i])

    ni = i - 1
    while ni >= 0 and board[ni] == 0 :
        ni -= 1

    if i <= end+1 or ni <= end :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        # print("======i ni == N ======")
        return

    if board[i] == board[ni] :
        board[ptr] = 2 * board[i]
        if ptr != i : board[i] = 0
        board[ni] = 0
        ptr -= 1
    elif board[i] != 0 :
        board[ptr] = board[i]
        if ptr != i : board[i] = 0
        ptr -= 1
            
    set_right(ni, end, N, board, ptr)


def brute_force(N, board, n, U, D, L, R) :
    # print('n:', n, 'U:', U, 'D:', D, 'L:', L, 'R:', R)
    if n > 4 :
        global max_num
        if max_num < (temp := max(board)) :
            max_num = temp
        return

    if U < 4 :
        brute_force(N, move_dir(N, board[:], 0), n+1, U+1, D, L, R)

    if D < 4 :
        brute_force(N, move_dir(N, board[:], 1), n+1, U, D+1, L, R)

    if L < 4 :
        brute_force(N, move_dir(N, board[:], 2), n+1, U, D, L+1, R)

    if R < 4 :
        brute_force(N, move_dir(N, board[:], 3), n+1, U, D, L, R+1)


def main() :
    input = sys.stdin.readline
    N = int(input())
    T = N * N
    board = []
    for _ in range(N) :
        board += list(map(int, input().split()))

    global max_num
    max_num = 0

    brute_force(N, board, 0, 0, 0, 0, 0) 
    # print('max_num:', end=" ")
    print(max_num)

    # for i in range(N*N) :
    #     print(board[i], end=" ")
    #     if (i+1) % N == 0 :
    #         print()


if __name__ == '__main__' :
    main()
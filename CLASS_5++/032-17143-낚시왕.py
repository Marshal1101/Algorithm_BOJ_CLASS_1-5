import sys
from collections import deque


def arrange_dir(d, r, c, R, C) :
    if r == 0 and d == 4 : d = 3
    if r == R-1 and d == 3 : d = 4
    if c == 0 and d == 1 : d = 2
    if c == C-1 and d == 2 : d = 1
    return d


def get_shark_pos(shark, pos, deltas, R, C) :
    length = len(shark)
    n_pos = [[0 for _ in range(C)] for _ in range(R)]
    for _ in range(length) :
        r, c, s, d, z = shark.popleft()
        is_minus = False
        if pos[r][c] == z :
            if d > 2 :
                nc = c
                ns = r + (deltas[d] * s)
                if ns < 0 :
                    ns = abs(ns)
                    is_minus = True
                di = ns // (R - 1)
                k = ns % (R - 1)
                if di % 2 : nr = R-1 - k
                else : nr = k
            else :
                nr = r
                ns = c + (deltas[d] * s)
                if ns < 0 :
                    ns = abs(ns)
                    is_minus = True
                di = ns // (C - 1)
                k = ns % (C - 1)
                if di % 2 : nc = C-1 - k
                else: nc = k
                    
            if n_pos[nr][nc] < z :
                if is_minus : di += 1
                if di % 2 :
                    if d == 1 : d = 2
                    elif d == 2 : d = 1
                    elif d == 3 : d = 4
                    else : d = 3
                d = arrange_dir(d, nr, nc, R, C)
                n_pos[nr][nc] = z
                shark.append((nr, nc, s, d, z))
    return n_pos


def get_fish(step, C, pos) :
    for j in range(C) :
        if (fish := pos[step][j]) > 0 :
            pos[step][j] = 0
            return fish
    return 0


def main() :
    input = sys.stdin.readline
    C, R, M = map(int, input().split())
    pos = [[0 for _ in range(C)] for _ in range(R)]
    shark = deque([])
    for _ in range(M) :
        c, r, s, d, z = map(int, input().split())
        r -= 1
        c -= 1
        d = arrange_dir(d, r, c, R, C)
        pos[r][c] = z
        shark.append((r, c, s, d, z))


    deltas = [0, -1, 1, 1, -1]
    total = 0
    for i in range(R) :
        total += get_fish(i, C, pos)
        pos = get_shark_pos(shark, pos, deltas, R, C)
        
    print(total)


if __name__ == '__main__' :
    main()
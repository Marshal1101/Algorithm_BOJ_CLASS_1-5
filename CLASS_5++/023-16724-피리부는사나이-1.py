import sys


def set_pos(i, j, v, pos, N, M) :
    if v == 'U' :
        pos[i*M + j] = (i-1) * M + j
    elif v == 'D' :
        pos[i*M + j] = (i+1) * M + j
    elif v == 'L' :
        pos[i*M + j] = i * M + j - 1
    else :
        pos[i*M + j] = i * M + j + 1


def dfs(i, pos, visited) :
    start = i
    while visited[i] == -1 :
        visited[i] = start
        i = pos[i]
    else :
        if visited[i] == start :
            return 1
        else : return 0

def main() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    T = N * M
    pos = [0] * T
    for i in range(N) :
        for j, arrow in enumerate(list(input().rstrip())) :
            set_pos(i, j, arrow, pos, N, M)

    # print(pos)
    visited = [-1] * T
    shelter = 0
    for i in range(T) :
        if visited[i] == -1 :
            shelter += dfs(i, pos, visited)

    print(shelter)


if __name__ == '__main__' :
    main()
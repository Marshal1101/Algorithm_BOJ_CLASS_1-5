import sys


def dfs(i, pos, visited, dir) :
    start = i
    while visited[i] == -1 :
        visited[i] = start
        i = i + dir[pos[i]]
    else :
        if visited[i] == start :
            return 1
        else : return 0

def main() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    T = N * M
    pos = []
    for i in range(N) :
        pos += list(input().rstrip())

    # https://www.acmicpc.net/source/46395660
    dir = {'L': -1, 'R': 1, 'U': -M, 'D': M}
    
    visited = [-1] * T
    shelter = 0
    for i in range(T) :
        if visited[i] == -1 :
            shelter += dfs(i, pos, visited, dir)

    print(shelter)


if __name__ == '__main__' :
    main()
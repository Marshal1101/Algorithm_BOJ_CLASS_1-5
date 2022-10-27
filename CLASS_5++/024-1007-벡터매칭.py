"""
Probliem Link: https://www.acmicpc.net/problem/1007
"""


import sys, math

def distance(dx, dy) :
    return math.sqrt(dx**2 + dy**2)


def brute_force(N, pos, i, sum_x, sum_y, p, m) :
    global min_dist

    if i == N :
        if (dist := distance(sum_x, sum_y)) < min_dist :
            min_dist = dist
        return

    if p :
        brute_force(N, pos, i+1, sum_x + pos[i][0], sum_y + pos[i][1], p - 1, m)
    if m :
        brute_force(N, pos, i+1, sum_x - pos[i][0], sum_y - pos[i][1], p, m - 1)



def main() :
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T) :
        N = int(input())
        pos = []
        for _ in range(N) :
            pos.append(list(map(int, input().split())))
            
        global min_dist
        min_dist = sys.maxsize
        brute_force(N, pos, 0, 0, 0, N//2, N//2)
        
        print(min_dist)
        

if __name__ == '__main__' :
    main()
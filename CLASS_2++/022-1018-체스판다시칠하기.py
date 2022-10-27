import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
board = [[] for _ in range(N)]
for i in range(N) :
    board[i] = list(sys.stdin.readline().strip())

def checker(i, j) :
    count1 = 0
    even = 'B'
    odd = 'W'
    for y in range(i, i+8, 2) :
        for x in range(j, j+8, 2) :
            if board[y][x] != even :
                count1 += 1
        for x in range(j+1, j+8, 2) :
            if board[y][x] != odd :
                count1 += 1            
    for y in range(i+1, i+8, 2) :
        for x in range(j+1, j+8, 2) :
            if board[y][x] != even :
                count1 += 1
        for x in range(j, j+8, 2) :
            if board[y][x] != odd :
                count1 += 1

    even = 'W'
    odd = 'B'
    count2 = 0
    for y in range(i, i+8, 2) :
        for x in range(j, j+8, 2) :
            if board[y][x] != even :
                count2 += 1
        for x in range(j+1, j+8, 2) :
            if board[y][x] != odd :
                count2 += 1            
    for y in range(i+1, i+8, 2) :
        for x in range(j+1, j+8, 2) :
            if board[y][x] != even :
                count2 += 1
        for x in range(j, j+8, 2) :
            if board[y][x] != odd :
                count2 += 1
    
    return min(count1, count2)

result = 2500
for i in range(N-7) :
    for j in range(M-7) :
        res = checker(i, j)
        # print('i', i, 'j', j, 'res', res)
        if res < result :
            result = res
print(result)

import sys

input = sys.stdin.readline

N = int(input())
bw = []
for _ in range(N) :
    bw.append(input().strip())
def divide(y, x, N) :
    result = ''
    start_color = bw[y][x]
    all_same_color = True
    for i in range(y, y + N) :
        if all_same_color != True :
            break
        for j in range(x, x + N) :
            if start_color != bw[i][j] :
                all_same_color = False
                break
    
    if all_same_color :
        result += start_color
        return result
    else :
        result += '('
        if N > 2 :
            for i in range(y, y + N, N // 2) :
                for j in range(x, x + N, N // 2) :
                    result += divide(i, j, N//2)
        else :
            for i in range(y, y+2) :
                for j in range(x, x+2) :
                    result += bw[i][j]
        result += ')'
        return result

print(divide(0, 0, N))
import sys, math

input = sys.stdin.readline


N = int(input())
paper = []
for i in range(N) :
    paper.append(input().split())

def devide(y, x, N) :
    count = {'-1': 0, '0': 0, '1': 0}
    start = paper[y][x]
    is_the_same_color_in_this_level = True
    for i in range(y, y + N) :
        if is_the_same_color_in_this_level != True :
            break
        for j in range(x, x + N) :
            if start != paper[i][j] :
                is_the_same_color_in_this_level = False
                break
    if is_the_same_color_in_this_level == True:
        count[start] += 1
        return count
    if N > 3 :
        for i in range(y, y + N, N // 3) :
            for j in range(x, x + N, N // 3) :
                res = devide(i, j, N // 3)
                for key, value in res.items() :
                    count[key] += value
    else :
        for i in range(y, y+3) :
            for j in range(x, x+3) :
                count[paper[i][j]] += 1
    return count
    
for i in devide(0, 0, N).values() :
    print(i)
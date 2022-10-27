import sys
input = sys.stdin.readline

N = int(input())
paper = []
for i in range(N) :
    paper.append(input().split())

def checker(y, x, N) :
    start = paper[y][x]

    ## 현재 사각형이 전부 같은 숫자인지 체크
    for i in range(y, y + N) :
        for j in range(x, x + N) :
            if start != paper[i][j] :
                return False
    return True

def devide(y: int, x: int, N: int) :
    count = {'-1': 0, '0': 0, '1': 0}
    start = paper[y][x]


    # 같으면 첫 시작 숫자를 카운트 +1 하고 리턴
    if checker(y, x, N) :
        count[start] += 1
        return count
    
    ## 통일된 사각형이 아니면 9분할 시작 위치마다 재귀시작
    if N > 3 :
        for i in range(y, y + N, N // 3) :
            for j in range(x, x + N, N // 3) :
                res = devide(i, j, N // 3)
                for key, value in res.items() :
                    count[key] += value
    # k=1; 9칸짜리 사각형일 때는 그냥 카운트
    else :
        for i in range(y, y+3) :
            for j in range(x, x+3) :
                count[paper[i][j]] += 1
    return count
    
for i in devide(0, 0, N).values() :
    print(i)
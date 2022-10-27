import sys; input = sys.stdin.readline

N = int(input())
stars = [ list("*" * N) for _ in range(N) ]

# print(stars)
## 3, 9, 27, 81, ... , 3**k (1<=k<=8)

def recursion(si, sj, N) :
    if N == 3 :
        stars[si+1][sj+1] = " "
        return

    next_N = N // 3

    for i in range(si, si + N, next_N) :
        for j in range(sj, sj + N, next_N) :
            if i != si + next_N or j != sj + next_N :
                recursion(i, j, next_N)
            else :
                for v in range(i, i + next_N) :
                    for w in range(j, j + next_N) :
                        stars[v][w] = " "


recursion(0, 0, N)
for star in stars :
    print("".join(star))
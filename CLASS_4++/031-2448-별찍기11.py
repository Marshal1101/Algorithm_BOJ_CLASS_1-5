import sys; input = sys.stdin.readline

N = int(input())

stars = []
for i in range(1, N+1) :
    star = ""
    empty = ((2*N-1) - (2*i-1)) // 2
    star += " " * empty + "*" * (2*i-1) + " " * empty
    stars.append(list(star))

def recur(si, sj, N) :

    if N == 3 :
        stars[si+1][sj] = " "
        return

    next_N = N // 2

    for v in range(next_N) :
        for w in range(N-1-2*v) :
            stars[si+next_N+v][sj-N+next_N+1+v+w] = " "

    recur(si, sj, next_N)
    recur(si + next_N, sj - next_N, next_N)
    recur(si + next_N, sj + next_N, next_N)

recur(0, N-1, N)
for star in stars :
    print("".join(star))
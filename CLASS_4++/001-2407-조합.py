import sys

N, M = map(int, sys.stdin.readline().split())


def permutation(n, r) :
    res = 1
    while r > 0 :
        res *= n
        n -= 1
        r -= 1
    return res

def combination(n, r) :
    return permutation(n, r) // permutation(r, r)

print(combination(N, M))
## https://www.acmicpc.net/source/17964028

import sys
def euc(x, y):
    q = []
    while y:
        q.append(x // y)
        x, y = y, x % y
    q.pop()
    a, b = 0, 1
    for i in q[::-1]:
        a, b = b, a - i*b
    return x, a, b


def f():
    M, N, x, y = [int(i) for i in sys.stdin.readline().split()]
    d = x-y

    g, a, b = euc(M, N)
    if d % g:
        return -1
    k = d // g
    K = x - k*a*M
    return (K-1) % (M//g*N) + 1


for _ in range(int(sys.stdin.readline())):
    print(f())
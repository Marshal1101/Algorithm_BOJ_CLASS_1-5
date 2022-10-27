## https://www.acmicpc.net/source/26276950

matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]

mod = 10**9+7

def matmul(A, B):
    n = len(A)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[j][i] += A[j][k] * B[k][i]
            result[j][i] %= mod
    return result

def matpow(A, n):
    if n == 1: return A
    A2 = matpow(A, n//2)
    A2 = matmul(A2, A2)
    if n%2 == 1: A2 = matmul(A2, A)
    return A2

print(matpow(matrix, int(input()))[0][0])
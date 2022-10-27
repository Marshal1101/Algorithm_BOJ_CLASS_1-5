import sys; input = sys.stdin.readline


def main():
    N = 8
    MOD = 1000000007
    D = int(input())
    mem = dict()
    mem[1] = [
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        
    ]
    print(f(D, 0, 0, N, MOD, mem))


def f(d, start, end, N, MOD, mem):
    if d <= 1:
        return mem[d][start][end]

    mem.setdefault(d, [[0 for _ in range(N)] for _ in range(N)])
    if mem[d][start][end]:
        return mem[d][start][end]

    half1 = d // 2
    half2 = half1 + 1 if d % 2 else half1

    for k in range(N):
        mem[d][start][end] += f(half1, start, k, N, MOD, mem) * f(half2, k, end, N, MOD, mem)
        mem[d][start][end] %= MOD

    return mem[d][start][end]


if __name__ == '__main__':
    main()
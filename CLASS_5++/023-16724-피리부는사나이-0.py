## https://www.acmicpc.net/source/39958197


from sys import stdin

input = stdin.readline


def union_find(disjoint_set, a):
    if disjoint_set[a] <= 0:
        return a
    else:
        disjoint_set[a] = union_find(disjoint_set, disjoint_set[a])
        return disjoint_set[a]


def solve():
    N, M = map(int, input().split())
    d = {'D': M, 'L': -1, 'R': 1, 'U': -M}
    arr = '0'
    for _ in range(N):
        arr += input()[:-1]

    disjoint_set = [0] * (N * M + 1)
    ans = 0
    for i in range(1, len(arr)):
        root = union_find(disjoint_set, i + d[arr[i]])
        if root == i:
            ans += 1
            disjoint_set[i] = -1
        else:
            disjoint_set[i] = root

    return ans


if __name__ == '__main__':
    print(solve())

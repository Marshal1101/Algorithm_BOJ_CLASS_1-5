## https://www.acmicpc.net/source/39584312

from sys import stdin

input = stdin.readline


def solve():
    T = int(input())
    n = int(input())
    A = [0] + [*map(int, input().split())]
    m = int(input())
    B = [0] + [*map(int, input().split())]
    a_sum = [0] * (n + 1)
    b_sum = [0] * (m + 1)
    for i in range(1, n + 1):
        a_sum[i] = a_sum[i-1] + A[i]
    for i in range(1, m + 1):
        b_sum[i] = b_sum[i-1] + B[i]

    dic = {}
    for i in range(1, n + 1):
        for j in range(i):
            partial_sum = a_sum[i] - a_sum[j]
            if partial_sum not in dic:
                dic[partial_sum] = 0
            dic[partial_sum] += 1

    ans = 0
    for i in range(1, m + 1):
        for j in range(i):
            partial_sum = b_sum[i] - b_sum[j]
            diff = T - partial_sum
            if diff in dic:
                ans += dic[diff]

    return ans


if __name__ == '__main__':
    print(solve())

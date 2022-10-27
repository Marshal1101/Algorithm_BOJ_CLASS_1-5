from sys import stdin
from collections import deque

input = stdin.readline


def solve():
    N, M = map(int, input().split())
    length = N * M
    arr = [0] * length
    for i in range(0, length, N):
        arr[i:i+N] = input().split()

    que = deque(i for i in range(length) if arr[i] == '1')
    cnt = arr.count('0')
    ans = 0

    while cnt and que:
        ans += 1
        for _ in range(len(que)):
            cur = que.popleft()
            r, c = cur // N, cur % N
            if 0 < r and arr[cur - N] == '0':
                que.append(cur - N)
                arr[cur - N] = '1'
                cnt -= 1
            if r < M - 1 and arr[cur + N] == '0':
                que.append(cur + N)
                arr[cur + N] = '1'
                cnt -= 1
            if 0 < c and arr[cur - 1] == '0':
                que.append(cur - 1)
                arr[cur - 1] = '1'
                cnt -= 1
            if c < N - 1 and arr[cur + 1] == '0':
                que.append(cur + 1)
                arr[cur + 1] = '1'
                cnt -= 1

    return ans if cnt == 0 else -1


if __name__ == '__main__':
    print(solve())
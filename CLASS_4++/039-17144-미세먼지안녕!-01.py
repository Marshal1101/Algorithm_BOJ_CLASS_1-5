## https://www.acmicpc.net/source/43912881

from sys import stdin

input = stdin.readline


def solve():
    R, C, T = map(int, input().split())
    length = R * C
    arr = [0] * length
    for i in range(0, length, C):
        arr[i:i+C] = [*map(int, input().split())]

    print(arr)
    up = arr.index(-1)
    down = up + C

    for _ in range(T):
        # 확산
        newArr = arr.copy()
        for cur in range(length):
            if arr[cur] <= 0: continue
            spread_amount = arr[cur] // 5
            spread_count = 0
            r, c = cur // C, cur % C
            if 0 < r and (nxt := cur - C) != down:
                spread_count += 1
                newArr[nxt] += spread_amount
            if r < R - 1 and (nxt := cur + C) != up:
                spread_count += 1
                newArr[nxt] += spread_amount
            if 0 < c and (nxt := cur - 1) not in (up, down):
                spread_count += 1
                newArr[nxt] += spread_amount
            if c < C - 1:
                spread_count += 1
                newArr[cur + 1] += spread_amount

            newArr[cur] -= spread_amount * spread_count


        # 순환
        for i in range(up - C, 0, -C):
            newArr[i] = newArr[i-C]
        for i in range(0, C - 1):
            newArr[i] = newArr[i+1]
        for i in range(C - 1, up, C):
            newArr[i] = newArr[i+C]
        for i in range(up + C - 1, up + 1, -1):
            newArr[i] = newArr[i-1]
        for i in range(down + C, length - C, C):
            newArr[i] = newArr[i+C]
        for i in range(length - C, length - 1):
            newArr[i] = newArr[i+1]
        for i in range(length - 1, down + C, -C):
            newArr[i] = newArr[i-C]
        for i in range(down + C - 1, down + 1, -1):
            newArr[i] = newArr[i-1]

        newArr[up+1] = 0
        newArr[down+1] = 0
        arr = newArr

    print(sum(arr) + 2)


if __name__ == '__main__':
    solve()

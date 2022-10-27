## https://www.acmicpc.net/source/43100195

from sys import stdin

input = stdin.readline


def solve():
    R, C, M = map(int, input().split())
    length = R * C
    sharks = {}
    for i in range(M):
        r, c, s, d, z = map(int, input().split())
        pos = (r - 1) * C + (c - 1)
        s %= 2 * (R - 1 if d <= 2 else C - 1)
        sharks[pos] = [s, d, z]

    def move_sharks():
        nxtSharks = {}
        for pos in sharks.keys():
            s, d, z = sharks[pos]

            if d == 1:
                nxtPos = pos % C
                x = pos // C
                l = R
                _2l = 2 * l

                if s <= x: nxtPos += C * (x - s)
                elif s <= x + l - 1:
                    nxtPos += C * (s - x)
                    d = 2 if d == 1 else 3
                else: nxtPos += C * (_2l + x - 2 - s)

            elif d == 2:
                nxtPos = pos % C
                x = pos // C
                l = R
                _2l = 2 * l

                if s <= l - 1 - x: nxtPos += C * (x + s)
                elif s <= _2l - 2 - x:
                    nxtPos += C * (_2l - x - s - 2)
                    d = 1 if d == 2 else 4
                else: nxtPos += C * (s + x + 2 - _2l)

            elif d == 3:
                nxtPos = (pos // C) * C
                x = pos % C
                l = C
                _2l = 2 * l

                if s <= l - 1 - x: nxtPos += x + s
                elif s <= _2l - 2 - x:
                    nxtPos += _2l - x - s - 2
                    d = 1 if d == 2 else 4
                else: nxtPos += s + x + 2 - _2l

            else:
                nxtPos = (pos // C) * C
                x = pos % C
                l = C
                _2l = 2 * l

                if s <= x: nxtPos += x - s
                elif s <= x + l - 1:
                    nxtPos += s - x
                    d = 2 if d == 1 else 3
                else: nxtPos += _2l + x - 2 - s

            if nxtPos not in nxtSharks or nxtSharks[nxtPos][2] < sharks[pos][2]:
                sharks[pos][1] = d
                nxtSharks[nxtPos] = sharks[pos]

        return nxtSharks

    def get_sharks(line):
        for i in range(line, length, C):
            if i in sharks:
                return i
        return -1

    ans = 0
    for i in range(C):
        pos = get_sharks(i)
        if pos != -1:
            ans += sharks[pos][2]
            del sharks[pos]
        sharks = move_sharks()

    return ans


if __name__ == '__main__':
    print(solve())

import sys
from bisect import bisect_left

input = sys.stdin.readline


def sol12015():
    n = int(input())
    A = map(int, input().split())
    seq = [next(A)]
    # print(seq)
    # print(list(A))
    for a in A:
        if(a > seq[-1]):
            seq.append(a)
        else:
            seq[bisect_left(seq, a)] = a
    print(len(seq))

sol12015()
        
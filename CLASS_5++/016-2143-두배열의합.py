from collections import defaultdict
import sys


def main() :
    input = sys.stdin.readline
    T = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    sum_A = []
    sum_B = []

    for i in range(n) :
        total = 0
        for j in range(i, n) :
            total += A[j]
            sum_A.append(total)

    B_cnt = defaultdict(int)
    for i in range(m) :
        total = 0
        for j in range(i, m) :
            total += B[j]
            B_cnt[total] += 1
            sum_B.append(total)
    
    sum_A.sort()
    sum_B.sort()
    # print(sum_A)
    # print(sum_B)
    # C = Counter(sum_B)

    count = 0
    for num in sum_A :
        count += B_cnt[T-num]

    print(count)


if __name__ == '__main__' :
    main()
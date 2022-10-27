import sys


input = sys.stdin.readline
N = int(input())
memo = [0]
for a in map(int, input().split()) :
    if memo[-1] < a :
        memo.append(a)
    else :
        lp = 0
        rp = len(memo)-1

        while lp <= rp :
            mid = (lp + rp) // 2

            if memo[mid] < a :
                lp = mid + 1
            else :
                rp = mid - 1
        memo[lp] = a

print(len(memo)-1)
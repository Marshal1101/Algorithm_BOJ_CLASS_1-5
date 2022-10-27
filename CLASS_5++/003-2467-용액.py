import sys

def main() :
    input = sys.stdin.readline

    N = int(input())
    arr = list(map(int, input().split()))

    lp = 0
    rp = N - 1
    num1 = 0
    num2 = 0
    min_gap = sys.maxsize
    while lp < rp :
        if (abs(s := arr[lp] + arr[rp]) < min_gap) :
            min_gap = abs(s)
            num1 = arr[lp]
            num2 = arr[rp]
        # mid = (lp + rp) // 2
        if s > 0 :
            rp -= 1
        elif (s == 0) :
            return (arr[lp], arr[rp])
        else :
            lp += 1

    return (num1, num2)

if __name__ == '__main__' :
    print(*main())
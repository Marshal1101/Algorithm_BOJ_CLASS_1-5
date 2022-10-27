import sys


def main() :
    input = sys.stdin.readline

    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    left = 0 ; right = 0 ; mid = 0
    min_sum = sys.maxsize
    flag = False
    for i in range(N-2) :
        if flag : break
        fix = arr[i]
        lp = i + 1
        rp = N - 1
        while lp < rp :    
            cur_sum = fix + arr[lp] + arr[rp]
        
            if abs(cur_sum) < min_sum :
                min_sum = abs(cur_sum)
                left = fix
                mid = arr[lp]
                right = arr[rp]

            if cur_sum < 0 :
                lp += 1
            elif cur_sum > 0 :
                rp -= 1
            else :
                flag = True
                break

    return (left, mid, right)

if __name__ == '__main__' :
    print(*main())
import sys

def dp(arr, sel_idx, N) :
    INF = sys.maxsize
    for i in range(3) :
        if i != sel_idx :
            arr[0][i] = INF
    arr[N-1][sel_idx] = INF
    # print(sel_idx, arr)
    for i in range(1, N) :
        arr[i][0] = (arr[i-1][1] if arr[i-1][1] < arr[i-1][2] else arr[i-1][2]) + arr[i][0]
        arr[i][1] = (arr[i-1][0] if arr[i-1][0] < arr[i-1][2] else arr[i-1][2]) + arr[i][1]
        arr[i][2] = (arr[i-1][0] if arr[i-1][0] < arr[i-1][1] else arr[i-1][1]) + arr[i][2]
    
    return min(arr[N-1])


def main() :
    input = sys.stdin.readline
    N = int(input())
    house = []
    for _ in range(N) :
        house.append(list(map(int, input().split())))

    result = []
    for k in range(3) :
        result.append(dp([h[:] for h in house], k, N))

    print(min(result))


if __name__ == '__main__' :
    main()
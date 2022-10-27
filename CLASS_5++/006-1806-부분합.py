import sys

def main() :
    input = sys.stdin.readline
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    fp = 0
    bp = 0
    total = 0
    min_cnt = sys.maxsize
    while fp < N :
        total += arr[fp]
        if total >= S :
            while total - arr[bp] >= S :
                total -= arr[bp]
                bp += 1 
            if (cnt := fp+1 - bp) < min_cnt :
                min_cnt = cnt
        # print('bp:', bp, 'fp:', fp, 'total:', total)
        fp += 1

    if min_cnt < sys.maxsize :
        print(min_cnt)
    else : print(0)

if __name__ == '__main__' :
    main()
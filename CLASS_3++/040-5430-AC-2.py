from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    func = input()
    N = int(input())
    S = input().strip()
    if N > 0 :
        arr = S[1:-1].split(',')
    else : arr = []

    arr = deque(arr)
    # print(func, N, 'init', arr)
    ptr_switch_zeroLP_oneRP = 0
    for f in func :
        if f == 'R' :
            ptr_switch_zeroLP_oneRP = 1 - ptr_switch_zeroLP_oneRP
        elif f == 'D' :
            if len(arr) == 0:
                print('error')
                break
            else :
                if ptr_switch_zeroLP_oneRP :
                    arr.pop()
                else : 
                    arr.popleft()
    else :
        res = ""
        if ptr_switch_zeroLP_oneRP :
            arr.reverse()
        res += ",".join(arr)
        print('[' + res + ']')
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    func = input().strip()
    N = int(input())
    S = input().lstrip('[').rstrip(']\n')
    if N > 0 :
        arr = S.split(',')
    else : arr = []

    lp = 0
    rp = N - 1
    length = N
    ptr_switch_zeroLP_oneRP = 0
    for f in func :
        if f == 'R' :
            ptr_switch_zeroLP_oneRP = 1 - ptr_switch_zeroLP_oneRP
        elif f == 'D' :
            if length > 0:
                if ptr_switch_zeroLP_oneRP :
                    rp -= 1
                else : 
                    lp += 1
                length -= 1
            else :
                print('error')
                break
    else :
        res = ""
        if length > 0 :
            new = arr[lp:rp+1]
            if ptr_switch_zeroLP_oneRP :
                new.reverse()
            res += ",".join(new)
        print("[" + res + "]")
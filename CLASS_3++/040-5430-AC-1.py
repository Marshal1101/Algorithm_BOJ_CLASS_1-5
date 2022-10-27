import sys
from random import randint
input = sys.stdin.readline


## 테스트 하는 법을 알았다.

# T = int(input())
while True :
    # 랜덤 연산 생성
    func = ''
    for i in range(randint(2, 7)) :
        j = randint(0, 1)
        if j : func += 'R'
        else : func += 'D'
        # func = list(input().strip())
        print('===================')
        N = randint(0, 10)
        if N == 0 : _input = '[]'
        else :
            a = randint(1, 9)
            _input = f'[{a}'
            for i in range(N-1) :
                num = randint(1, 100)
                _input = _input + f',{num}'
            _input = _input + ']\n'
        
        print('연산:', func)
        print('리스트길이:', N)
        print('리스트:', _input)
        
        # 코드
        if N > 0 :
            arr = list(map(
                int,
                _input.strip()
                .replace('[', '')
                .replace(']', '')
                .split(',')
                ))
        else : arr = []

        print(func, N, 'init', arr)

        lp = 0
        rp = N - 1
        length = N
        ptr_switch_zeroLP_oneRP = 0
        # is_error = False
        for order in func :
            if order == 'R' :
                ptr_switch_zeroLP_oneRP = 1 - ptr_switch_zeroLP_oneRP
            elif order == 'D' :
                if length > 0:
                    if ptr_switch_zeroLP_oneRP :
                        rp -= 1
                    else : 
                        lp += 1
                    length -= 1
                else :
                    print('error')
                    # is_error = True
                    break
            print('lp:', lp, 'rp:', rp)
        else :
            res = '['
            while length > 0 :
                if ptr_switch_zeroLP_oneRP :
                    res += str(arr[rp])
                    rp -= 1
                else :
                    res += str(arr[lp])
                    lp += 1
                length -= 1
                if length > 0 : res += ","
            res += "]"
            print(res, '<-ans sort->', ptr_switch_zeroLP_oneRP)
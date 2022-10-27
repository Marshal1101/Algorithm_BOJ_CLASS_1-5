import sys

N = sys.stdin.readline()

def solution(input) :
    n = len(input)
    _n = int(input)
    if (_n <= 18) :
        temp = 0
    else :
        temp = _n - n*9
    # temp = 1
    while (temp >=0 and temp < _n) :
        str_temp = str(temp)
        total = 0
        res = 0
        for st in str_temp :
            total += int(st)
            print(st, total, temp)
        res = temp + total
        # print(res, temp, total)
        if (res == _n) :
            return temp
        else : temp += 1
    return 0

print(solution(N))
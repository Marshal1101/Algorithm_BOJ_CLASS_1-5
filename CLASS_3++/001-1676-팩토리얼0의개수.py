import sys


def factorial(num) :
    res = 1
    k = 1
    cnt = 0
    while ( num > 1 ) :
        res *= num
        num -= 1
        if res % (10**k) == 0 :
            cnt = k
            k += 1
    return cnt

N = int(sys.stdin.readline())
print(factorial(N))
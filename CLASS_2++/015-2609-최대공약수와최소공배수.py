## Least Common Multiple: LCM
## Greatest Common Divisor: GCD

import sys

a, b = map(int, sys.stdin.readline().split(' '))

def devide(num1, num2) :
    LCM = 1
    GCD = 1
    prime = 2
    while (num1 > 1 or num2 > 1) :
        if (num1 % prime == 0) :
            LCM *= prime
            num1 //= prime 
            if (num2 % prime == 0) :
                GCD *= prime
                num2 //= prime
        elif (num2 % prime == 0) :
            LCM *= prime
            num2 //= prime
        else :
            prime += 1
        # print('prime', prime, 'num1', num1, 'num2', num2)
    print(GCD)
    print(LCM)

devide(a, b)
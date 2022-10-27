import sys, math

M, N = map(int, sys.stdin.readline().split())

def primeCheck(num) :
    if num == 1 : return False
    if num == 2 : return True
    end = math.floor(math.sqrt(num))
    for i in range(2, end+1) :
        if num % i == 0 :
            return False
    return True

for i in range(M, N+1) :
    if primeCheck(i) :
        print(i)
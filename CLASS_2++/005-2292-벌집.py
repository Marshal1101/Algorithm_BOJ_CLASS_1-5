import sys

input = sys.stdin.readline()

def solution(N) :
    n = int(N)
    i = 1
    while True :
        address = 3*(i**2) - 3*i + 1
        if (n <= address) :
            return i
        i += 1

print(solution(input))
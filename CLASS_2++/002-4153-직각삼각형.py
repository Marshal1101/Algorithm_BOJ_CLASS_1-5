import sys

input = sys.stdin.readline

while (True) :
    a, b, c = map(int, input().split(' '))
    if (a == 0) : break
    if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a) :
        print("right")
    else : print("wrong")
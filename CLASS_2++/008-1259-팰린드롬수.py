from re import L
import sys

input = sys.stdin.readline

while True :
    _num = input()
    num = int(_num)
    if (num == 0) : break
    string = list(_num.strip())
    n = len(string)
    total = 0
    for i in range(n-1, -1, -1) :
        total += int(string[i]) * 10**i
    if num == total : print("yes")
    else : print("no")
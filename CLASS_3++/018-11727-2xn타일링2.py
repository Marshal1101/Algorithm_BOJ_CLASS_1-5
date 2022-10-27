import sys


input = sys.stdin.readline


n = int(input())
s = [0, 1, 3]
if n < 3 : print(s[n])
else : 
    for i in range(3, n+1):
        s.append(2*s[i - 2] + s[i - 1])
    print(s[n] % 10007)
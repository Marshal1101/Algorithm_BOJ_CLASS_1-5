import sys
input = sys.stdin.readline

N, M = map(int, input().split())

name_key = {}
num_key = {}
for i in range(1, N+1) : 
    pmon = input().rstrip()
    name_key[pmon] = i
    num_key[i] = pmon
for j in range(M) :
    ask = input().rstrip()
    if 65 <= ord(ask[0]) <= 90 or 97 <= ord(ask[0]) <= 122 :
        print(name_key[ask])
    else : print(num_key[int(ask)])
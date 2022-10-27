import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
for i in range(T) :
    N = int(input())
    clothes = defaultdict(int)
    for j in range(N) :
        cloth, part = input().split()
        if clothes[part] == 0 :
            clothes[part] = ['None']
        
        clothes[part].append(cloth)
    
    # print(clothes)
    total = 1
    for part in clothes.keys() :
        total *= len(clothes[part])
    print(total-1)
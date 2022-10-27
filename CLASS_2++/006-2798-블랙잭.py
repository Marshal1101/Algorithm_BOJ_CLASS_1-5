import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))
cards = list(map(int, input().split(' ')))

# print(N, M, cards)

maxValue = 0
total = 0
for i in range(N) :
    total += cards[i]
    for j in range(i+1, N) :
        total += cards[j]
        for k in range(j+1, N) :
            total += cards[k]
            if (total <= M and total > maxValue) :
                maxValue = total
            total -= cards[k]
        total -= cards[j]
    total -= cards[i]
    
print(maxValue)
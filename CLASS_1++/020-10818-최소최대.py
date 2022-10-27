import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split(' ')))
maxNum = numbers[0]
minNum = numbers[0]
for num in numbers :
    if num > maxNum :
        maxNum = num
    elif num < minNum : 
        minNum = num

print(minNum, maxNum)
import sys

input = sys.stdin.readline()


total = 0
words = input.split('-')
total += sum(map(int, words[0].split('+')))
for word in words[1:] :
    total -= sum(map(int, word.split('+')))

print(total)
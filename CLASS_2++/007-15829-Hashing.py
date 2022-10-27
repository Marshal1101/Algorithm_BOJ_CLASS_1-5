import sys

input = sys.stdin.readline

L = int(input())
string = list(input())

# print(L, string)
hash = 0
for i in range(L) :
    hash += (ord(string[i]) - 96) * (31 ** i)

print(hash % 1234567891)
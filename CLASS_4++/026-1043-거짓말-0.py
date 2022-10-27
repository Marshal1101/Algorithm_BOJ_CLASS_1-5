## https://www.acmicpc.net/source/12927180

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

k = map(int, input().split())
num = next(k)
fact = list(k)
counted = set(fact)
linked = []
for _ in range(m):
    k = map(int, input().split())
    num = next(k)
    linked.append(set(k))
while fact and linked:
    i = fact.pop()
    new_linked = []
    for k in linked:
        if i in k:
            fact += list(k.difference(counted))
        else:
            new_linked.append(k)
    linked = new_linked

print(len(linked))




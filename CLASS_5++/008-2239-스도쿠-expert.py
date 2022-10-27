## https://www.acmicpc.net/source/18433291

path = []
n, m = 9, 81
rows = [{*range(j, j+n)} for j in range(0, m, n)]
cols = [{*range(i, m, n)} for i in range(n)]
square = [0, 1, 2, 9, 10, 11, 18, 19, 20]
square33s = []
for i in range(0, m, 27):
    for j in range(0, n, 3):
        k = i + j
        square33s.append({k + a for a in square})

import sys
input = sys.stdin.readline
for i in range(n):
    for j in range(n):
        path.append(rows[i].union(cols[j], square33s[j // 3 + i - i % 3])) # path[i*n+j]: ith row, jth col
        path[i*n+j].remove(i*n+j)
path2 = [[] for _ in range(m)]

bits = [1 << i for i in range(n)]
whole = (1 << n) - 1
tobit = lambda i: 1 << (i - 1) if i else whole
tobit2 = lambda i: 1 << (i - 1) if i else 0
tonum = {1 << i: i + 1 for i in range(9)}
tonum[0] = 0
option = []
current = []

for _ in range(n):
    new = list(map(int, input().rstrip()))
    option += [*map(tobit, new)]
    current += [*map(tobit2, new)]
zeroes, nonzeroes = [], set()
for i, j in enumerate(current):
    if not j:
        zeroes.append(i)

def compute_avail(zeroes):
    new_zeroes = []
    for i in zeroes:
        x = option[i]
        a = 0
        for y in path[i]:
            new = current[y]
            if new:
                a |= new
            elif y > i:
                path2[i].append(y)
        path[i].difference_update(path2[i], nonzeroes)
        x &= ~a
        assert x != 0
        if x in tonum:
            current[i] = x
        option[i] = x
    # Do it once more, insert it in reversed order
    for i in zeroes[::-1]:
        x = option[i]
        if x == current[i]:
            continue
        a = 0
        for y in path2[i]:
            a |= current[y]
        x &= ~a
        assert x != 0
        if x in tonum:
            current[i] = x
        else:
            new_zeroes.append(i)
        option[i] = x
    return new_zeroes

def check_unique(change, t = False):
    if t:
        for i in range(n):
            print(*[tonum[j] for j in current[i * n:(i + 1) * n]], sep = '')

        print('=' * 9)

    for row in rows:
        for bit in bits:
            tmp = [i for i in row if option[i] & bit]
            if len(tmp) == 1:
                j = tmp[0]
                if current[j] == 0:
                    change.remove(j)
                    current[j] = bit
                    option[j] = bit
    for col in cols:
        for bit in bits:
            tmp = [i for i in col if option[i] & bit]
            if len(tmp) == 1:
                j = tmp[0]
                if current[j] == 0:
                    change.remove(j)
                    current[j] = bit
                    option[j] = bit
    for sq in square33s:
        for bit in bits:
            tmp = [i for i in sq if option[i] & bit]
            if len(tmp) == 1:
                j = tmp[0]
                if current[j] == 0:
                    change.remove(j)
                    current[j] = bit
                    option[j] = bit
    if t:
        for i in range(n):
            print(*[tonum[j] for j in current[i * n:(i + 1) * n]], sep = '')
        print('='*9)
    return change
def dfs(index):
    if index == -1:
        for i in range(n):
            print(*[tonum[j] for j in current[i*n:(i+1)*n]], sep = '')
        sys.exit()
        return

    u = zeroes[index]
    val = option[u]
    anti = 0
    for j in path[u]:
        anti |= current[j]
    val &= ~anti
    index -= 1
    for bit in bits:
        if bit & val:
            current[u] = bit
            dfs(index)
    current[u] = 0

zeroes = compute_avail(zeroes)
zeroes = check_unique(zeroes)[::-1]
zeroes = compute_avail(zeroes)


dfs(len(zeroes) - 1)
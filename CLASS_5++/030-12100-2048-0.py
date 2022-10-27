## https://www.acmicpc.net/source/14377803

import sys
read = sys.stdin.readline

n = int(read())
r_q = [[] for _ in range(n)]
c_q = [[] for _ in range(n)]

for r in range(n):
    s = [*map(int, read().split())]
    for c in range(n):
        tmp = s[c]
        if tmp != 0:
            r_q[r].append(tmp)
            c_q[c].append(tmp)

def move(o, t= 1, b= True, n= n):
    o_r = []
    node = False

    for i in o:
        o_r.append(i.copy())
        k = 0
        while True:
            try:
                if i[k] == i[k+1]:
                    node = True
                    i[k] += i.pop(k+1)
                k += 1
            except: break

    if t == 5 or (node == False and b == False):
        tmp = 0
        for i in o:
            for j in i:
                if j > tmp:
                    tmp = j
        return tmp

    new_c = [[] for _ in range(n)]
    new_c_r = [[] for _ in range(n)]

    for i in o:
        k = 0
        for j in i:
            new_c[k].append(j)
            k += 1

    if node == False:
        for i in o:
            k = -1
            for j in i[::-1]:
                new_c_r[k].append(j)
                k -= 1

        return max(move(new_c, t+1, node),move(new_c_r, t+1, node))

    for i in o_r:
        k = -1
        while True:
            try:
                if i[k] == i[k-1]:
                    i[k] += i.pop(k-1)
                k -= 1
            except: break

    for i in o_r:
        k = -1
        for j in i[::-1]:
            new_c_r[k].append(j)
            k -= 1

    return max(move(o, t+1),move(o_r, t+1),move(new_c, t+1),move(new_c_r, t+1))

print(max(move(r_q), move(c_q)))
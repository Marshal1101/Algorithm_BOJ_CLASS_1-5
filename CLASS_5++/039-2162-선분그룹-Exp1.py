## https://www.acmicpc.net/source/15272711

from sys import stdin

def count_groups(g):
    h = dict()
    for i in range(n):
        t = i
        while t != g[t]:
            t = g[t]
        if t in h:
            h[t] = h[t] + 1
        else:
            h[t] = 1
    return h

def find_largest(h):
    mx = 0
    for e in h:
        mx = max(mx, h[e])
    return mx

def cross(i, j):
    x1, y1, x2, y2 = lines[i]
    _x1, _y1, _x2, _y2 = lines[j]
    
    a = y2-y1
    b = x1-x2
    c = -x1*y2+x2*y1

    if a*_x1 + b*_y1 + c == 0 and a*_x2 + b*_y2 + c == 0:
        if _x1 == _x2:
            if y2 < y1:
                tmp = y1
                y1 = y2
                y2 = tmp
            if _y2 < _y1:
                tmp = _y1
                _y1 = _y2
                _y2 = tmp
            if y1 > _y1:
                tmp1 = _y1
                tmp2 = _y2
                _y1 = y1
                _y2 = y2
                y1 = tmp1
                y2 = tmp2
            if y2 < _y1:
                return False
            else:
                return True
        else:
            if x2 < x1:
                tmp = x1
                x1 = x2
                x2 = tmp
            if _x2 < _x1:
                tmp = _x1
                _x1 = _x2
                _x2 = tmp
            if x1 > _x1:
                tmp1 = _x1
                tmp2 = _x2
                _x1 = x1
                _x2 = x2
                x1 = tmp1
                x2 = tmp2
            if x2 < _x1:
                return False
            else:
                return True
    elif (a*_x1 + b*_y1 + c) * (a*_x2 + b*_y2 + c) <= 0:
        return True
    else:
        return False
    

def overlap(i, j):
    if cross(i, j) and cross(j, i):
        return True
    else:
        return False
    
    

def assign(j, i):
    t = j
    while t != g[t]:
        tmp = g[t]
        g[t] = i
        t = tmp
    g[t] = i


def check_line(i):
    g[i] = i
    for j in range(i):
        if overlap(i, j) and g[j] != i:
            assign(j, i)


input = stdin.readline

g = dict()
lines = []
n = int(input())
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append([x1, y1, x2, y2])
    check_line(i)


h = count_groups(g)
print(len(h))
print(find_largest(h))

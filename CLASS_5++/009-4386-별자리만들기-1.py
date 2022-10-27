## 크루스칼 알고리즘

import sys, math


def union(parent, a, b) :
    a = find(parent, a)
    b = find(parent, b)
    if a < b : parent[b] = a
    else : parent[a] = b


def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]


def distance_xy(x1, y1, x2, y2) :
    return math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)


def main() :
    input = sys.stdin.readline
    N = int(input())
    node_list = []
    for _ in range(N) :
        node_list.append(list(map(float, input().split())))
    
    adj_list = []
    for i in range(N-1) :
        x1, y1 = node_list[i]
        for j in range(i+1, N) :
            x2, y2 = node_list[j]
            dist = distance_xy(x1, y1, x2, y2)
            adj_list.append((dist, i, j))
    adj_list.sort()

    min_cost = 0
    parent = [i for i in range(N)]
    length = len(adj_list)
    for i in range(length) :
        dist, n1, n2 = adj_list[i]
        if find(parent, n1) != find(parent, n2) :
            union(parent, n1, n2)
            min_cost += dist

    print(round(min_cost, 2))


if __name__ == '__main__' :
    main()
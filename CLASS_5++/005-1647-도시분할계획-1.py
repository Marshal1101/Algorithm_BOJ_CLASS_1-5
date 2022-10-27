## 크루스칼 알고리즘

import sys

def union(parent_list, a, b) :
    a = find(parent_list, a)
    b = find(parent_list, b)
    if a < b : parent_list[b] = a
    else : parent_list[a] = b

def find(parent_list, x) :
    if parent_list[x] != x :
        parent_list[x] = find(parent_list, parent_list[x]) 
    return parent_list[x]

def main() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    adj_list = []
    for _ in range(M) :
        A, B, C = map(int, input().split())
        adj_list.append((C, A, B))
    adj_list.sort()

    total_dist = 0
    pre_dist = 0
    parent_list = [i for i in range(N+1)]
    for i in range(M) :
        C, A, B = adj_list[i]
        if find(parent_list, A) != find(parent_list, B) :
            union(parent_list, A, B)
            pre_dist = C
            total_dist += C
    
    print(total_dist - pre_dist)

if __name__ == '__main__' :
    main()
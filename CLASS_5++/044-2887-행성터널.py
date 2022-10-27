import sys


def union(parent_list, a, b):
    a = find(parent_list, a)
    b = find(parent_list, b)
    if a < b : parent_list[b] = a
    else : parent_list[a] = b

def find(parent_list, x):
    if parent_list[x] != x:
        parent_list[x] = find(parent_list, parent_list[x]) 
    return parent_list[x]

def main():
    input = sys.stdin.readline
    N = int(input())
    x_list = []
    y_list = []
    z_list = []
    for i in range(N):
        x, y, z = map(int, input().split())
        x_list.append((x, i))
        y_list.append((y, i))
        z_list.append((z, i))

    x_list.sort()
    y_list.sort()
    z_list.sort()

    edges = []
    for cur_list in x_list, y_list, z_list:
        for i in range(1, N):
            w1, p1 = cur_list[i-1]
            w2, p2 = cur_list[i]
            edges.append((abs(w1-w2), p1, p2))
    edges.sort()

    i, cnt = 0, 0
    total_dist = 0
    parent_list = [i for i in range(N)]
    while cnt < N-1 or i < len(edges):
        C, A, B = edges[i]
        if find(parent_list, A) != find(parent_list, B) :
            union(parent_list, A, B)
            # print('union:A, B, C:', A, B, C)
            total_dist += C
            cnt += 1
        i += 1

    print(total_dist)


if __name__ == '__main__' :
    main()
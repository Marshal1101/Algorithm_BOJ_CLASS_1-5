import sys

def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b) :
    a = find(parent, a)
    b = find(parent, b)
    if a < b : parent[b] = a
    else : parent[a] = b

def main() :
    input = sys.stdin.readline
    n, m = map(int, input().split())
    parent = [i for i in range(n)]
    for i in range(m) :
        s, e = map(int, input().split())
        if find(parent, s) != find(parent, e) :
            union(parent, s, e)
        else :
            print(i+1)
            break
    else : print(0)

if __name__ == '__main__' :
    main()
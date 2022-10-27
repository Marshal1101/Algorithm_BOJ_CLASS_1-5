import sys


def union(gate, a, b) :
    a = find(gate, a)
    b = find(gate, b)
    if a < b : gate[b] = a
    else : gate[a] = b


def find(gate, a) :
    if gate[a] != a :
        gate[a] = find(gate, gate[a])
    return gate[a]


def main() :
    input = sys.stdin.readline
    G = int(input())
    P = int(input())
    gate = [i for i in range(G+1)]
    flight = [int(i) for i in sys.stdin.readlines()]
    for i in range(P) :
        if (doc := find(gate, flight[i])) != 0 :
            gate[doc] -= 1
            union(gate, doc, flight[i])
        else : return i

    return P

if __name__ == '__main__' :
    print(main())
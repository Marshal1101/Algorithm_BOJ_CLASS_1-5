import sys
from bisect import bisect_right


def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b


def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    check_card = [i for i in range(M+1)]
    card_list = list(map(int, input().split()))
    card_list.sort()
    # print(card_list)
    for num in map(int, input().split()):
        i = bisect_right(card_list, num)
        used = find(check_card, i)
        print(card_list[used])
        check_card[used] += 1
        union(check_card, used, i)

if __name__ == '__main__':
    main()
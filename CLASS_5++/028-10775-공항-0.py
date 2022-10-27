## https://www.acmicpc.net/source/39628442


from sys import stdin

input = stdin.readline


def union_find(disjoint_set, gate):
    if disjoint_set[gate] != -1:
        disjoint_set[gate] = union_find(disjoint_set, disjoint_set[gate])
        return disjoint_set[gate]
    else:
        return gate


def solve():
    G = int(input())
    P = int(input())
    ans = 0
    # i번 게이트에 처음 넣으면 disjoint_set[i] = i-1
    disjoint_set = [-1] * (G + 1)
    for plane in range(P):
        gate = int(input())
        # 이미 들어가 있으면
        if disjoint_set[gate] != -1:
            # 3, 4번 들어가 있는 상태에서 gate = 4 -> next_gate = 2
            next_gate = union_find(disjoint_set, gate)
            if next_gate:
                # disjoin_set[2] = 1
                disjoint_set[next_gate] = union_find(disjoint_set, next_gate-1)
                # disjoint_set[4] = 1
                disjoint_set[gate] = disjoint_set[next_gate]
            else:
                break
        # 처음 넣는 경우
        else:
            disjoint_set[gate] = union_find(disjoint_set, gate - 1)

        ans += 1

    return ans


if __name__ == '__main__':
    print(solve())

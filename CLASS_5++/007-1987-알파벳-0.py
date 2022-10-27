## https://www.acmicpc.net/source/44322786

from sys import stdin


input = stdin.readline


def solve():

    R, C = map(int, input().split())
    length = R * C
    visited = [set() for _ in range(length)]

    arr = [0] * length
    for i in range(R):
        arr[i * C:(i+1) * C] = [*map(lambda char: 1 << (ord(char) - 65), input()[:-1])]

    ans = 0
    que = {0}
    visited[0].add(arr[0])
    for k in range(27):
        if k == 26 or not que:
            ans = k
            break
        new_que = set()
        new_visited = [set() for _ in range(length)]
        while que:
            cur_pos = que.pop()
            i, j = cur_pos // C, cur_pos % C
            adj = []
            if i > 0: adj.append(cur_pos-C)
            if j > 0: adj.append(cur_pos-1)
            if i < R - 1: adj.append(cur_pos+C)
            if j < C - 1: adj.append(cur_pos+1)
            for neighbor_pos in adj:
                neighbor_alpha = arr[neighbor_pos]
                flag = True
                for visited_alpha in visited[cur_pos]:
                    if not neighbor_alpha & visited_alpha:
                        new_visited[neighbor_pos].add(visited_alpha | neighbor_alpha)
                        if flag:
                            new_que.add(neighbor_pos)
                            flag = False

        que = new_que
        visited = new_visited

    return ans


if __name__ == '__main__':
    print(solve())

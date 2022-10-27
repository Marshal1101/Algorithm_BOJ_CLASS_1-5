## 백준 가장 빠른 풀이
## - Problem link: https://www.acmicpc.net/problem/17144
## - Solution link: http://www.teferi.net/ps/problems/boj/17144

import itertools

CLEANER = -1


def compute_diffusion(R, C, cleaner1, cleaner2):
    cycle1 = list(
        itertools.chain(
            range(cleaner1 - C, 0, -C),  # up
            range(C - 1),  # right
            range(C - 1, cleaner1 + C, C),  # down
            range(cleaner1 + C - 2, cleaner1 - 1, -1)  # left
        ))
    cycle2 = list(
        itertools.chain(
            range(cleaner2 + C, R * C, C),  # down
            range((R - 1) * C + 1, R * C - 1),  # right
            range(R * C - 1, cleaner2, -C),  # up
            range(cleaner2 + C - 2, cleaner2 - 1, -1)  # left
        ))
    return list(zip(cycle1[1:], cycle1)) + list(zip(cycle2[1:], cycle2))


def compute_adj_graph(R, C, cleaner1, cleaner2):
    adj_positions = []
    deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for row in range(R):
        for col in range(C):
            adj_positions.append([
                adj for dr, dc in deltas
                if (0 <= (nr := row + dr) < R and 0 <= (nc := col + dc) < C and
                    (adj := nr * C + nc) not in (cleaner1, cleaner2))
            ])
    return adj_positions


def main():
    R, C, T = [int(x) for x in input().split()]
    grid_cur = []
    for _ in range(R):
        grid_cur.extend(int(x) for x in input().split())

    cleaner1 = grid_cur.index(CLEANER)
    cleaner2 = cleaner1 + C
    grid_cur[cleaner1] = grid_cur[cleaner2] = 0
    diffusion = compute_diffusion(R, C, cleaner1, cleaner2)
    adj_positions = compute_adj_graph(R, C, cleaner1, cleaner2)

    for _ in range(T):
        grid_prev, grid_cur = grid_cur, [0] * (R * C)
        for pos, val, adj_pos in zip(range(R * C), grid_prev, adj_positions):
            if val == 0:
                continue
            dif = val // 5
            for p in adj_pos:
                grid_cur[p] += dif
                val -= dif
            grid_cur[pos] += val
        for prev, cur in diffusion:
            grid_cur[cur] = grid_cur[prev]

    print(sum(grid_cur))


if __name__ == '__main__':
    main()
"""Solution code for "BOJ 1865. 웜홀".

- Problem link: https://www.acmicpc.net/problem/1865
- Solution link: http://www.teferi.net/ps/problems/boj/1865

Tags: [SPFA]

(This code was generated by Import Inliner v0.3)
"""

import collections
import sys
from typing import List, Mapping, Optional, Sequence

INF = float('inf')
WGraph = Sequence[Mapping[int, float]]


# >>>[BEGIN] teflib.tgraph.spfa [v1.4] (Copied from teflib/tgraph.py)<<<
def spfa(wgraph: WGraph,
         source: int,
         prev: Optional[List[int]] = None) -> List[float]:
    size = len(wgraph)
    lengths = [0] * size
    is_in_queue = [False] * size
    is_in_queue[source] = True
    distances = [INF] * size
    distances[source] = 0
    if prev:
        prev[source] = None
    queue = collections.deque([source])
    while queue:
        u = queue.popleft()
        is_in_queue[u] = False
        length_u, dist_u = lengths[u], distances[u]
        if length_u == size:
            dist_u = distances[u] = -INF
        for v, dist_uv in wgraph[u].items():
            dist_v = dist_u + dist_uv
            if distances[v] <= dist_v:
                continue
            distances[v], lengths[v] = dist_v, length_u + 1
            if prev:
                prev[v] = u
            if not is_in_queue[v]:
                queue.append(v)
                is_in_queue[v] = True
    return distances
# >>>[END] teflib.tgraph.spfa [v1.4]<<<


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M, W = [int(x) for x in sys.stdin.readline().split()]
        wgraph = [{} for _ in range(N + 1)]
        wgraph[N] = {u: 0 for u in range(N)}
        for _ in range(M):
            S, E, T = [int(x) for x in sys.stdin.readline().split()]
            try:
                min_weight = wgraph[S - 1][E - 1]
                wgraph[S - 1][E - 1] = wgraph[E - 1][S - 1] = min(min_weight, T)
            except KeyError:
                wgraph[S - 1][E - 1] = wgraph[E - 1][S - 1] = T
        for _ in range(W):
            S, E, T = [int(x) for x in sys.stdin.readline().split()]
            try:
                min_weight = wgraph[S - 1][E - 1]
                wgraph[S - 1][E - 1] = min(min_weight, -T)
            except KeyError:
                wgraph[S - 1][E - 1] = -T

        dists = spfa(wgraph, N)
        print('YES' if -INF in dists else 'NO')


if __name__ == '__main__':
    main()

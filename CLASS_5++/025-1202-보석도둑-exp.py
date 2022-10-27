## https://www.acmicpc.net/source/40315104

from sys import stdin
from heapq import heappush, heappop

input = stdin.readline


def solve():
    N, K = map(int, input().split())
    jewels = [0] * N
    for i in range(N):
        jewels[i] = (*map(int, input().split()), )
    # print('jewels:', jewels)

    # bag[무게] = 해당 무게의 가방 개수
    bag = {}
    for i in range(K):
        w = int(input())
        bag[w] = bag.get(w, 0) + 1

    bag_weights = sorted(bag.keys())
    # print('bag:', bag)
    # print('bag_weights:', bag_weights)
    # 가방의 최대 허용 무게보다 무거운 보석 제외 (안 하는 게 조금 더 빠름)
    jewels = [jewels[i] for i in range(N) if jewels[i][0] <= bag_weights[-1]]
    # 무게를 기준으로 오름차순 정렬
    jewels.sort(key=lambda t: t[0])

    idx, ans = 0, 0
    heap = []
    # 가장 작은 무게의 가방부터
    for bag_weight in bag_weights:
        # 해당 가방이 허용할 수 있는 모든 보석들을 heap에 넣어준다
        while idx < len(jewels) and jewels[idx][0] <= bag_weight:
            w, v = jewels[idx]
            idx += 1
            heappush(heap, -v)
        # 해당 무게의 가방 개수만큼 보석을 가방에 넣어준다
        for _ in range(bag[bag_weight]):
            if heap:
                ans -= heappop(heap)

    return ans


if __name__ == '__main__':
    print(solve())

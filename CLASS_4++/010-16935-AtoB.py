import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

def bfs(start, end) :
    que = deque([start])
    cnt = 1
    while que :
        length = len(que)
        for _ in range(length) :
            num = que.popleft()

            # 숫자가 초과하면 스킵
            if num > end :
                continue
            
            # 같으면 리턴
            if num == end :
                return cnt

            # x2
            num_x2 = num * 2
            que.append(num_x2)
            # x10 + 1
            num_x10 = num * 10 + 1
            que.append(num_x10)

        cnt += 1
        # print('cnt:', cnt, 'que:', que)

    return -1

print(bfs(N, M))
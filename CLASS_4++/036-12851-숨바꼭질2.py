import sys; input = sys.stdin.readline
from collections import deque


N, K = map(int, input().split())

def bfs(start, end) :
    INF = sys.maxsize
    dp = [ INF for _ in range(2*end) ]
    cnt = 0
    dp[start] = 0
    que = deque([(start, 0)])
    # que = deque([(start, 0, [start])])
    
    arrived = False
    while que :
        length = len(que)
        for _ in range(length) :
            num, time = que.popleft()
            # num, time, path = que.popleft()
            
            if num == end :
                # if time < dp[num] :
                #     cnt = 1
                # elif time == dp[num] :
                # print(path)
                cnt += 1
                arrived = True

            if 0 <= num - 1 <= end and time + 1 <= dp[num-1]:
                dp[num-1] = time + 1
                que.append((num-1, time+1))
                # path.append(num-1)
                # que.append((num-1, time+1, path[:]))
                # path.pop()
            if num + 1 <= end and time + 1 <= dp[num+1] :
                dp[num+1] = time + 1
                que.append((num+1, time+1))
                # path.append(num+1)
                # que.append((num+1, time+1, path[:]))
                # path.pop()
            if 2*num < 2*(end-1) and time + 1 <= dp[2*num] :
                dp[2*num] = time + 1
                que.append((2*num, time+1))
                # path.append(2*num)
                # que.append((2*num, time+1, path[:]))
                # path.pop()

    if arrived :
        return (dp[end], cnt)

if N >= K :
    print(N - K)
    print(1)
else :
    time, cnt = bfs(N, K)
    print(time)
    print(cnt)
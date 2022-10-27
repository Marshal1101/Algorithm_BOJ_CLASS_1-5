## pypy

from collections import deque
import sys

input = sys.stdin.readline


def bfs(start, end) :
    past_cnt = [20000] * 10000
    visited =[False] * 10000

    cnt = 0
    visited[start] = True
    que = deque([(start, '')])

    while que :
        length = len(que)
        for _ in range(length) :
            cur_num, path = que.popleft()
            # End
            if cnt > past_cnt[cur_num] : 
                return

            # Main End
            if cur_num == end : 
                print(path)
                return

            #D
            Dnum = 2*cur_num % 10000
            if not visited[Dnum] :
                visited[Dnum] = True
                Dpath = path + 'D'
                que.append((Dnum, Dpath))

            #S
            Snum = cur_num - 1 if cur_num > 0 else 9999
            if not visited[Snum] :
                visited[Snum] = True
                Spath = path + 'S'
                que.append((Snum, Spath))

            #L
            head = cur_num // 1000
            Lnum = (cur_num - head*1000) * 10 + head
            if not visited[Lnum] :
                visited[Lnum] = True
                Lpath = path + 'L'
                que.append((Lnum, Lpath))

            #R
            tail = cur_num % 10
            Rnum = (cur_num // 10) + tail * 1000
            if not visited[Rnum] :
                visited[Rnum] = True
                Rpath = path + 'R'
                que.append((Rnum, Rpath))
        # print('forend que:', que, 'forend path:', path, 'forend cnt:', cnt)
        cnt += 1

T = int(input())
for _ in range(T) :
    start, end = map(int, input().split())
    bfs(start, end)
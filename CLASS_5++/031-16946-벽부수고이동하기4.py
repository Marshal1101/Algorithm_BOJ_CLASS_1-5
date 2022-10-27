import sys
from collections import deque

def set_cnt_bfs(i, N, M, ground, visited) :
    visited[i] = i
    T = N * M
    que = deque([i])
    rev_que = deque([i])
    while que :
        cur_i = que.popleft()
        if cur_i-M >= 0 and ground[cur_i-M] == '0' and visited[cur_i-M] == -1 :
            que.append(cur_i-M)
            rev_que.append(cur_i-M)
            visited[cur_i-M] = i
        if cur_i+M < T and ground[cur_i+M] == '0' and visited[cur_i+M] == -1 :
            que.append(cur_i+M)
            rev_que.append(cur_i+M)
            visited[cur_i+M] = i
        if cur_i-1 >= (cur_i//M)*M and ground[cur_i-1] == '0' and visited[cur_i-1] == -1 :
            que.append(cur_i-1)
            rev_que.append(cur_i-1)
            visited[cur_i-1] = i
        if cur_i+1 < (cur_i//M+1)*M and ground[cur_i+1] == '0' and visited[cur_i+1] == -1 :
            que.append(cur_i+1)
            rev_que.append(cur_i+1)
            visited[cur_i+1] = i
    
    cnt = len(rev_que)
    for i in rev_que :
        ground[i] = cnt


def get_cnt(i, N, M, ground, visited) :
    visited[i] = i
    chk_set = set()
    count = 1
    if i-M >= 0 and (cnt := ground[i-M]) != '1' and not visited[i-M] in chk_set :
        count += cnt
        chk_set.add(visited[i-M])
    if i+M < N*M and (cnt := ground[i+M]) != '1' and not visited[i+M] in chk_set :
        count += cnt
        chk_set.add(visited[i+M])
    if i-1 >= (i//M)*M and (cnt := ground[i-1]) != '1' and not visited[i-1] in chk_set :
        count += cnt
        chk_set.add(visited[i-1])
    if i+1 < (i//M+1)*M and (cnt := ground[i+1]) != '1' and not visited[i+1] in chk_set :
        count += cnt
        chk_set.add(visited[i+1])
    return count


def main() :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    T = N * M
    origin_ground = []
    for _ in range(N) :
        origin_ground += list(input().rstrip())
    
    visited = [-1] * T
    copy_ground = origin_ground[:]
    for i in range(T) :
        if visited[i] == -1 and copy_ground[i] == '0':
            set_cnt_bfs(i, N, M, copy_ground, visited)
    
    for i in range(T) :
        if visited[i] == -1 and origin_ground[i] == '1' :
            origin_ground[i] = str(get_cnt(i, N, M, copy_ground, visited) % 10)

    """
    이런 형식보다 아래 '# 출력'이 15% 빨라짐
    for i in range(T) :
        print(origin_ground[i], end="")
        if (i+1) % M == 0 :
            print()
    """
    
    # 출력
    for i in range(N):
        print(*origin_ground[i*M:(i+1)*M], sep='')


if __name__ == '__main__' :
    main()
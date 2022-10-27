import sys; input = sys.stdin.readline
from collections import defaultdict, deque


def get_chk_board(i, key_set, pos, door_pos, graph):
    ret = 0
    if 64 < ord(graph[i]) < 91:
        door_pos[graph[i]].append(i)
        # print('doorfound:', graph[i], i)
    else:
        if graph[i] == '$': ret += 1
        else: key_set.add(graph[i].upper())
        pos.append(i)
        graph[i] = '*'
    return ret


def set_open_door(key_set, pos, door_dict, graph):
    for door in door_dict.keys():
        if door in key_set:
            for i in door_dict[door]:
                if graph[i] != '*':
                    pos.append(i)
                    graph[i] = '*'
                    # print("door open:", door, i)


def bfs(R: int, C: int, key_set: set, pos: list, door_pos: dict, graph: list):
    # print(' pos: {p}\n key_set: {k}\n door: {d}\n'.format(p=pos, k=key_set, d=door_pos))
    set_open_door(key_set, pos, door_pos, graph)
    if not pos: return 0

    T = R * C + 1
    while pos:
        cur_i = pos.popleft()
        # print('bfs cur:', (cur_i-1)//C, (cur_i-1)%C)
        if cur_i % C != 1 and graph[cur_i-1] != '*':
            graph[0] += get_chk_board(cur_i-1, key_set, pos, door_pos, graph)
        if cur_i % C != 0 and graph[cur_i+1] != '*':
            graph[0] += get_chk_board(cur_i+1, key_set, pos, door_pos, graph)
        if cur_i - C > 0 and graph[cur_i-C] != '*':
            graph[0] += get_chk_board(cur_i-C, key_set, pos, door_pos, graph)
        if cur_i + C < T and graph[cur_i+C] != '*':
            graph[0] += get_chk_board(cur_i+C, key_set, pos, door_pos, graph)

        set_open_door(key_set, pos, door_pos, graph)
    
    return graph[0]

def main():
    test_cnt = int(input())
    for _ in range(test_cnt):
        R, C = map(int, input().split())
        T = R * C + 1
        # 지도
        graph = [0]
        for _ in range(R):
            graph += list(input().rstrip())

        # 시작 전부터 가지고 있는 열쇠
        init_key = input().rstrip()
        if init_key == '0':
            init_key = ''
        key_set = set(list(init_key.upper()))
        
        # 외곽을 돌며 입구 찾기
        pos = deque([])
        door_pos = defaultdict(list)
        for i in range(1, C+1):
            if graph[i] != '*':
                graph[0] += get_chk_board(i, key_set, pos, door_pos, graph)
        for i in range(1, T, C):
            if graph[i] != '*':
                graph[0] += get_chk_board(i, key_set, pos, door_pos, graph)
        for i in range(C, T, C):
            if graph[i] != '*':
                graph[0] += get_chk_board(i, key_set, pos, door_pos, graph)
        for i in range(T-C, T):
            if graph[i] != '*':
                graph[0] += get_chk_board(i, key_set, pos, door_pos, graph)

        print(bfs(R, C, key_set, pos, door_pos, graph))


if __name__ == '__main__':
    main()
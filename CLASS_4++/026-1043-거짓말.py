import sys; input = sys.stdin.readline

N, M = map(int, input().split())

possible_party = [True] * M
people_in_party = [[] for _ in range(M)]
party_by_person = [[] for _ in range(N+1)]
knowing_people = list(map(int, input().split()))

def dfs(person) :
    if not knowing_check[person] : 
        knowing_check[person] = True
        for party_num in party_by_person[person] :
            possible_party[party_num] = False
            for per in people_in_party[party_num] :
                dfs(per)

if knowing_people[0] == 0 :
    print(M)
else :
    for party_num in range(M) :
        person = list(map(int, input().split()))
        length = len(person)
        for j in range(1, length) :
            # print('j party_num', j, party_num)
            people_in_party[party_num].append(person[j])
            party_by_person[person[j]].append(party_num)

    knowing_check = [False] * (N+1)
    for person in knowing_people[1:] :
        dfs(person)

    possible_cnt = 0
    for bool in possible_party :
        if bool : possible_cnt += 1

    print(possible_cnt)
## 사이클의 시작지점을 찾는 알고리즘
## https://www.acmicpc.net/source/30464278


def solution(n, students):
    visited = [False] * (n + 1)
    count = 0

    for i in range(1, n+1):
        if not visited[i]:
            
            # From current student, move forward until it detects a cycle.
            current = i
            while not visited[current]:
                visited[current] = True
                current = students[current]
            
            # When former loop detects a cycle,
            # current value indicates a student from who a cycle formed.
            # So, from i'th student to the student, they cannot belong to any team.
            backtrack = i
            while backtrack != current:
                backtrack = students[backtrack]
                count += 1
            
    return count

T = int(input())

for _ in range(T):
    n = int(input())
    students = [0] + list(map(int, input().split()))

    print(solution(n, students))
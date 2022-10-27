# 91 1149 RGB거리 (참조, https://pacific-ocean.tistory.com/147)


import sys


input = sys.stdin.readline


n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
for i in range(1, len(p)): # n = len(p)
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))


# 0, 1, 2는 각각 빨강, 초록, 파랑을 뜻하고
# p[i][0]은 i번째집을 빨강으로 칠했을때의 최솟값을 나타낸다.
# p[i][1]과 p[i][2]도 마찬가지로 i번째집을 초록, 파랑으로 칠했을때의 최솟값을 나타낸다.
# 이 3개의 값중에서 가장 작은 값을 출력해주면 된다.
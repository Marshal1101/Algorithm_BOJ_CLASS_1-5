## https://www.acmicpc.net/source/42667741

from sys import stdin, setrecursionlimit as SRL
SRL(1_000_000)

input = stdin.readline


def solve():

    def dfs(cur):
        if dp[cur] != -1:
            return dp[cur]

        t = max([dp[i] if dp[i] != -1 else dfs(i) for i in indegree[cur]], default=0)
        dp[cur] = t + time[cur]
        return dp[cur]

    for _ in range(int(input())):
        N, K = map(int, input().split())
        time = [0, *map(int, input().split())]
        indegree = [[] for _ in range(N + 1)]
        for _ in range(K):
            before, after = map(int, input().split())
            indegree[after].append(before)

        W = int(input())
        dp = [-1] * (N + 1)
        print(dfs(W))


if __name__ == '__main__':
    solve()
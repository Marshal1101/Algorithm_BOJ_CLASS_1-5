## 위상정렬

"""Solution code for "BOJ 9466. 텀 프로젝트".

- Problem link: https://www.acmicpc.net/problem/9466
- Solution link: http://www.teferi.net/ps/problems/boj/9466
"""

import sys


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        selects = [int(x) for x in sys.stdin.readline().split()]

        indegrees = [0] * n
        for i in selects:
            indegrees[i - 1] += 1
        leaves = [i for i, indegree in enumerate(indegrees) if indegree == 0]
        while leaves:
            next_stu = selects[leaves.pop()] - 1
            indegrees[next_stu] -= 1
            if indegrees[next_stu] == 0:
                leaves.append(next_stu)

        print(n - sum(indegrees))


if __name__ == '__main__':
    main()

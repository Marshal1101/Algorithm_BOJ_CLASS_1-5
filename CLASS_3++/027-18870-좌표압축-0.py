## https://www.acmicpc.net/source/42016266

def solve(arr):
    sorted_arr = sorted(set(arr))
    d = {x: idx for idx, x in enumerate(sorted_arr)}
    return [d[x] for x in arr]


if __name__ == '__main__':
    N = input()
    arr = list(map(int, input().split()))
    print(' '.join(map(str, solve(arr))))
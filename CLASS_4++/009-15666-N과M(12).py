import sys; input = sys.stdin.readline

N, M = map(int, input().split())
arr = input().split()
arr.sort(key=lambda x:int(x))

def dfs(start, cnt, res) :
    if cnt == 0 :
        print(res)
        return

    back = -1
    for i in range(start, N) :
        if arr[i] != back :
            new_res = res + arr[i] + ' '
            dfs(i, cnt - 1, new_res)
            back = arr[i]

dfs(0, M, '')